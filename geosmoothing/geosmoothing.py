# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2016.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#


import numpy as np
import logging
import fiona
import shapely.wkt
from scipy.interpolate import splprep, splev
from shapely.geometry import LineString, Polygon, mapping, asShape


class Logger(object):

    def __init__(self, level=logging.INFO):
        logfmt = "[%(asctime)s - %(levelname)s] - %(message)s"
        dtfmt = "%Y-%m-%d %I:%M:%S"
        logging.basicConfig(level=level, format=logfmt, datefmt=dtfmt)

    def get(self):
        return logging.getLogger()

class Splines(object):

    def compSplineKnots(self, x, y, s, k, nest=-1):
        """
        Computed with Scipy splprep. Find the B-spline representation of
        an N-dimensional curve.

        Spline parameters:
        :s - smoothness parameter
        :k - spline order
        :nest - estimate of number of knots needed (-1 = maximal)
        """

        tck_u, fp, ier, msg = splprep([x,y], s=s, k=k, nest=nest, full_output=1)

        if ier > 0:
            print("{0}. ier={1}".format(msg, ier))

        return(tck_u, fp)


    def compSplineEv(self, x, tck, zoom=10):
        """
        Computed with Scipy splev. Given the knots and coefficients of
        a B-spline representation, evaluate the value of the smoothing
        polynomial and its derivatives

        Parameters:
        :tck - A tuple (t,c,k) containing the vector of knots,
             the B-spline coefficients, and the degree of the spline.
        """

        n_coords = len(x)
        n_len = n_coords * zoom
        x_ip, y_ip = splev(np.linspace(0, 1, n_len), tck)

        return(x_ip, y_ip)

class GeoSmoothing(object):

    def __init__(self, spl_smpar=0, spl_order=2, verbose=True):
        """
        spl_smpar: smoothness parameter
        spl_order: spline order
        """
        self.__spl_smpar = spl_smpar
        self.__spl_order = spl_order

        if not verbose:
            lg = Logger(level=logging.ERROR)
        else:
            lg = Logger()

        self.__logger = lg.get()

    def __getCoordinates(self, geom):
        """
        Getting x,y coordinates from geometry...
        """
        if isinstance(geom, LineString):
            x = np.array(geom.coords.xy[0])
            y = np.array(geom.coords.xy[1])

        elif isinstance(geom, Polygon):
            x = np.array(geom.exterior.coords.xy[0])
            y = np.array(geom.exterior.coords.xy[1])

        return(x, y)

    def __getWktFromGeom(self, geom):
        """
        Getting Well Known Text from input geometry.
        """
        return geom.wkt

    def __getGeomFromWkt(self, wkt):
        """
        Getting geometry from input Well Known Text.
        """
        return shapely.wkt.loads(wkt)

    def __getGeomIp(self, coords_ip, geom):
        """
        """
        if isinstance(geom, LineString):
            geom_ip = LineString(coords_ip.T)

        elif isinstance(geom, Polygon):
            geom_ip = Polygon(coords_ip.T)

        return geom_ip

    def __smoothGeom(self, geom):
        """
        Run smoothing geometries
        """
        x, y = self.__getCoordinates(geom)

        spl = Splines()

        tck_u, fp = spl.compSplineKnots(x, y, self.__spl_smpar, self.__spl_order)
        x_ip, y_ip = spl.compSplineEv(x, tck_u[0])

        coords_ip = np.array([x_ip, y_ip])

        return self.__getGeomIp(coords_ip, geom)

    def smoothShp(self, src_file, dst_file):
        """
        Smoothing Shapefiles
        """
        self.__logger.info("Smoothing SHP: Start process...")

        with fiona.open(src_file) as src_fl:
            src_schema = src_fl.schema.copy()
            src_driver = src_fl.driver
            src_crs = src_fl.crs
            src_vals = src_fl.values()

            with fiona.open(dst_file, "w", driver=src_driver,
                            crs=src_crs,schema=src_schema) as dst_fl:

                while True:
                    try:
                        val = src_vals.next()
                        geom = asShape(val['geometry'])
                        prop = val['properties']

                        geom_ip = self.__smoothGeom(geom)

                        dst_fl.write({
                                        'properties': prop,
                                        'geometry': mapping(geom_ip)
                                })

                    except StopIteration:
                        self.__logger.info("Smoothing SHP: finished process...")
                        break

                    except TypeError as tperr:
                        # self.__logger.error("Type error: {0}\n{1}".format(tperr, prop))

                        dst_fl.write({
                                        'properties': prop,
                                        'geometry': mapping(geom)
                                })

                    except Exception as err:
                        self.__logger.error("Error: {0}\n{1}".format(err, prop))

    def smoothWkt(self, wkt):
        """
        Smoothing Well Known Text
        """
        try:
            self.__logger.info("Smoothing WKT: Start process...")

            geom = self.__getGeomFromWkt(wkt)
            geom_ip = self.__smoothGeom(geom)

            self.__logger.info("Smoothing WKT: finished process...")

            return self.__getWktFromGeom(geom_ip)

        except Exception as err:
            self.__logger.error("Error: {0}".format(err))

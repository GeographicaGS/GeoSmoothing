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


import argparse
from geosmoothing import GeoSmoothing


def runWkt():
    descr = "Smoothing GIS features with B-Splines. Input format: Well Known Text. Builded on top of Numpy, Scipy, Shapely and Fiona."
    arg_parser = argparse.ArgumentParser(description=descr)

    arg_parser.add_argument('wkt_string', type=str, help='Input WKT string to smooth')

    args = arg_parser.parse_args()

    wkt_string = args.wkt_string

    gsm = GeoSmoothing()
    res_wkt = gsm.smoothWkt(wkt_string)

    print(res_wkt)

def runShp():
    descr = "Smoothing GIS features with B-Splines. Input format: ESRI Shapefile. Builded on top of Numpy, Scipy, Shapely and Fiona."
    arg_parser = argparse.ArgumentParser(description=descr)

    arg_parser.add_argument('src_file', type=str, help='source shapefile path')
    arg_parser.add_argument('dst_file', type=str, help='destiny shapefile path')

    args = arg_parser.parse_args()

    src_file = args.src_file
    dst_file = args.dst_file

    gsm = GeoSmoothing()
    res_wkt = gsm.smoothShp(src_file, dst_file)

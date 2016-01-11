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

from geosmoothing.geosmoothing import GeoSmoothing

def runShpTest():

    # src_file = "/home/cayetano/Documentos/capas/DERA/G03_Hidrografia/hd01_1_rio.shp"
    src_file = "data/dem_contours/test_contours.shp"
    dst_file = "/tmp/test_contours.shp"
    gsm = GeoSmoothing()
    gsm.smoothShp(src_file, dst_file)

if __name__ == "__main__":
    runShpTest()

#!/bin/env sh
#
#  Regenerate README reStructuredText for PYPI
#
#  Requirement: Pandoc
#  http://pandoc.org/
#
#  Author: Cayetano Benavent, 2015.
#  https://github.com/GeographicaGS
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

OUTRDM=README.rst
INRDM=README.md

if [ -f "$INRDM" ]; then
    pandoc --from=markdown --to=rst --output=$OUTRDM $INRDM;

    printf '%s\n' "Successfully process: $OUTRDM file generated."

else
    printf '%s\n' "Process can not run: $INRDM file does not exist."

fi

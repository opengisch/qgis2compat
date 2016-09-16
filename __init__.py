# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QGIScompat
           A PyQt5 compatibility layer for QGIS < 2.14

                              -------------------
        begin                : 2014-07-28
        git sha              : $Format:%H$
        copyright            : (C) 2016 OPENGIS.ch
        email                : info@opengis.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import sys
import qgis.utils


def log(message):
    print('QGIS2compat: %s' % message)

# qgis.utils.QGis is available in QGIS < 3
if hasattr(qgis.utils, 'QGis'):
    import qgis2compat.PyQt
    log('setting qgis.PyQt = qgis2compat.PyQt')
    sys.modules["qgis.PyQt"] = qgis2compat.PyQt


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    return QgisCompat()


class QgisCompat(object):
    def initGui(self):
        pass

    def unload(self):
        pass
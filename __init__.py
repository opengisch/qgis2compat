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

QGIS_VERSION = 0

def log(message):
    print('QGIS2compat: %s' % message)


def _qgis2_version():
    #QGIS enterprise uses a different versioning schema.
    # Let's remap their schema to the real API version
    qgis_enterprise_map = {21502: 20800}

    from qgis.PyQt.QtCore import QCoreApplication
    version = qgis.utils.QGis.QGIS_VERSION_INT
    if QCoreApplication.applicationName().startswith('QGIS Enterprise'):
        version = qgis_enterprise_map[qgis.utils.QGIS_VERSION_INT]
    return version


# qgis.utils.QGis is available in QGIS < 3
if hasattr(qgis.utils, 'QGis'):
    import qgis2compat.PyQt

    log('setting qgis.PyQt = qgis2compat.PyQt')
    sys.modules["qgis.PyQt"] = qgis2compat.PyQt

    QGIS_VERSION = _qgis2_version()
else:
    QGIS_VERSION = qgis.core.Qgis.QGIS_VERSION_INT


# FROM here is all needed to make QGIS's plugin manager happy
# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    return QgisCompat()


class QgisCompat(object):
    # noinspection PyPep8Naming
    def initGui(self):
        pass

    def unload(self):
        pass

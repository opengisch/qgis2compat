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
ORIGINAL_MODULE = None

def log(message):
    print('QGIS2compat: %s' % message)


def _qgis2_version():
    #QGIS enterprise uses a different versioning schema.
    # Let's remap their schema to the real API version
    qgis_enterprise_map = {21501: 20800,
                           21502: 20800,
                           21503: 20800}

    from qgis.PyQt.QtCore import QCoreApplication
    version = qgis.utils.QGis.QGIS_VERSION_INT
    if QCoreApplication.applicationName().startswith('QGIS Enterprise'):
        version = qgis_enterprise_map[version]
    return version


# qgis.utils.QGis is available in QGIS < 3
if hasattr(qgis.utils, 'QGis'):
    ORIGINAL_UIC = None
    if 'qgis2compat.PyQt' in sys.modules:
        del sys.modules['qgis2compat.PyQt']
    import qgis2compat.PyQt

    log('setting qgis.PyQt = qgis2compat.PyQt')
    if 'qgis.PyQt' in sys.modules:
        ORIGINAL_MODULE = sys.modules['qgis.PyQt']
    if 'qgis.PyQt.uic' in sys.modules:
        ORIGINAL_UIC = sys.modules['qgis.PyQt.uic']
    sys.modules["qgis.PyQt"] = qgis2compat.PyQt

    if ORIGINAL_UIC:
        sys.modules['qgis.PyQt.uic'] = ORIGINAL_UIC

    QGIS_VERSION = _qgis2_version()
else:
    QGIS_VERSION = qgis.core.Qgis.QGIS_VERSION_INT



# FROM here is all needed to make QGIS's plugin manager happy
# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    return QgisCompat(iface)


class QgisCompat(object):

    def __init__(self, iface):
        """Class constructor.

        On instantiation, the plugin instance will be assigned a copy
        of the QGIS iface object which will allow this plugin to access and
        manipulate the running QGIS instance that spawned it.

        :param iface:Quantum GIS iface instance. This instance is
            automatically passed to the plugin by QGIS when it loads the
            plugin.
        :type iface: QGisAppInterface
        """
        self.iface = iface

    # noinspection PyPep8Naming
    def initGui(self):
        pass

    def unload(self):
        self.iface.messageBar().pushWarning(
                "qgis2compat warning",
                "Due to the very special functionality provided by qgis2compat "
                "it cannot be loaded/unloaded ([un]checked in the plugin "
                "manager). If you don't need it anymore, please uninstall it.")
        if ORIGINAL_MODULE is not None:
            sys.modules['qgis.PyQt'] = ORIGINAL_MODULE

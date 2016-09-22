# coding=utf-8
import qgis.utils
from qgis2compat import log


# Dealing with a QGIS 2 version, monkey patch some things
# also guard with has_runned so monkeypatching happens only once
has_runned = False
if not has_runned and hasattr(qgis.utils, 'QGis'):
    has_runned = True
    log('Running apicompat')

    # Here import all the compatibility fixes modules
    import qgis2compat.apicompat.qgsvectorlayer
    import qgis2compat.apicompat.qgsrasterlayer

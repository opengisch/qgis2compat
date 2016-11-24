# coding=utf-8
import qgis.utils
from qgis2compat import log


# Dealing with a QGIS 2 version, monkey patch some things
# also guard with initialized so monkeypatching happens only once
initialized = False
if not initialized and hasattr(qgis.utils, 'QGis'):
    initialized = True
    log('Running apicompat')

    # Here import all the compatibility fixes modules
    import qgis2compat.apicompat.qgsvectorlayer
    import qgis2compat.apicompat.qgsrasterlayer
    import qgis2compat.apicompat.qgsmapthemecollection
    import qgis2compat.apicompat.qgsproject
    import qgis2compat.apicompat.qgsdatasourceuri

import qgis.utils


def log(message):
    print('QGIS2compat: %s' % message)


# Dealing with a QGIS 2 version, monkey patch some things
# also guard with has_runned so monkeypatching happens only once
has_runned = False
if not has_runned and hasattr(qgis.utils, 'QGis'):
    has_runned = True
    log('Running apicompat')
    import qgis2compat.apicompat.qgsvectorlayer



QGIS2compat
===========

A QGIS 3 compatibility layer for QGIS >= 2.8

Usage
-----
In your plugin's `__init__.py` you should put something like the example 
below. This will pick the QGIS PyQt compatibility layer which is 
available since QGIS 2.14 or fall back to qgis2compat. 

Also if you are in QGIS >= 2.14 and QGIS < 3 it will run the apicompat 
package which will take care of the Python api changes between QGIS 2 
and QGIS 3.

```Python
import os
import qgis.utils


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MyPlugin class from file MyPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """

    plugin_name = os.path.dirname(__file__).split(os.path.sep)[-1]
    plugin_name = qgis.utils.pluginMetadata(plugin_name, 'name')
    try:
        # qgis.PyQt is available in QGIS >=2.14
        from qgis.PyQt.QtCore import qVersion
        # qgis.utils.QGis is available in QGIS < 3
        if hasattr(qgis.utils, 'QGis'):
            import qgis2compat.apicompat
            qgis2compat.log('apicompat used in %s' % plugin_name)
    except ImportError:
        try:
            # we are in QGIS < 2.14
            import qgis2compat
            import qgis2compat.apicompat
            qgis2compat.log('PyQt and apicompat used in %s' % plugin_name)
        except ImportError:
            import traceback
            message = ('The Plugin %s uses the QGIS2compat plugin. '
                       'Please install it with the plugin manager it and '
                       'restart QGIS. For more information read '
                       'http://opengis.ch/qgis2compat' %
                       plugin_name)
            traceback.print_exc()
            raise ImportError(message)

    from .myplugin import MyPlugin
    return MyPlugin(iface)
```

in each module where you do PyQt imports you should use the following
structure. 

```Python
from qgis.PyQt.QtCore import QFileDialog
```

This will guarantee that the imports come from the most appropriate and 
up-to-date place and gives you PyQt4 and PyQt5 support for QGIS >= 2.8.


Updating your plugin
--------------------
This can be done automatically by the 2to3 tool included in QGIS sourcecode. 
Please note that it is not the plain 2to3 python tool and can be found
at https://github.com/qgis/QGIS/blob/master/scripts/2to3
This tool will fix many (probably not all) issues with your code and make it 
compatible with Python 3.

After running 2to3, update your `__init__.py` as explained above.

once done, it is time to run your tests (which you of course have written
before migrating) and fix the minor glitches that might have appeared.


Adding new apicompat fixes
--------------------------
To add a new api compatibility fix, just create (or add to an existing one) a
new module in apicompat and import it in `__init__.py__` like it is done for 
the [qgsvectorlayer.py](apicompat/qgsvectorlayer.py)

As QGIS2compat works on a fairly low level, we __require__ unit tests for each
fix to be included in each pull request.
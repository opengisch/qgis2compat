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

    try:
        # qgis.PyQt is available in QGIS >=2.14
        from qgis.PyQt.QtCore import qVersion
        # qgis.utils.QGis is available in QGIS < 3
        if hasattr(qgis.utils, 'QGis'):
            import qgis2compat.apicompat
        except ImportError:
            import traceback
            plugin_name = os.path.dirname(__file__).split(os.path.sep)[-1]
            plugin_name = qgis.utils.pluginMetadata(plugin_name, 'name')
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
try:
    from qgis.PyQt.QtCore import QFileDialog
except ImportError:
    from qgis2compat.PyQt.QtCore import QFileDialog
```

This will guarantee that the imports come from the most appropriate and 
up-to-date place and gives you PyQt4 and PyQt5 support for QGIS >= 2.8.

Of course if you want to avoid the try except you could just make QGIS2compat 
an hard dependency of your plugin by just importing like this:
```Python
from qgis2compat.PyQt.QtCore import QFileDialog
```
Be warned that importing this way, will prevent using the qgis.PyQt package 
available starting from QGIS 2.14. This is no problem for QGIS >= 2.14 and < 3
as QGIS2compat.PyQT is exactly the same package.
For QGIS 3 This shouldn't be a major problem as long as QGIS2compat gets 
updated. Just be warned.


Updating your plugin
--------------------
This Regexp is useful for a first step into converting your imports.
I used it quite sucessfully in PyCharm. 
Only caveat you first need to make sure that you don't have multiline
imports. If you have a better solution, please share :)

```Regexp
from qgis2compat\.(PyQt.*)
try:\n    from qgis.$1\nexcept ImportError:\n    from qgis2compat.$1
```


Adding new apicompat fixes
--------------------------
To add a new api compatibility fix, just create (or add to an existing one) a
new module in apicompat and import it in `__init__.py__` like it is done for 
the qgsvectorlayer.py

As QGIS2compat works on a fairly low level, we __require__ unit tests for each
fix
QGIS2compat
===========

A QGIS 3 compatibility layer for QGIS >= 2.8

Usage
-----
In your plugin's `__init__.py` you shoud put something like the example 
below. This will pick the QGIS PyQt compatibility layer which is 
available since QGIS 2.14 or fall back to qgis2compat.

```Python
# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load VeriSO class from file VeriSO.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """

    try:
        from qgis.PyQt.QtCore import Qt
    except ImportError:
        try:
            from qgis2compat.PyQt.QtCore import Qt
        except ImportError:
            plugin_name = os.path.relpath(".", "..")
            message = ('The Plugin %s uses the QGIS2compat plugin. '
                       'Please install it with the plugin manager it and '
                       'restart QGIS. For more information read '
                       'http://opengis.ch/qgis2compat' %
                       plugin_name)

            raise ImportError(message)

    from .veriso import VeriSO
    return VeriSO(iface)
```

in each module where you do PyQt imports you should use the following
structure. 

```Python
try:
    from qgis.PyQt.QtCore import QFileDialog
except ImportError:
    from qgis2compat.PyQt.QtCore import QFileDialog
```

This Regexp is useful for a first step into converting your imports.
I used it quite sucessfully in PyCharm. 
Only caveat you first need to make sure that you don't have multiline
imports. If you have a better solution, please share :)

```Regexp
from qgis2compat\.(PyQt.*)
try:\n    from qgis.$1\nexcept ImportError:\n    from qgis2compat.$1
```

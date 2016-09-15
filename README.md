QGIS2compat
===========

A QGIS 3 compatibility layer for QGIS >= 2.8

Usage
-----
```Python
try:
    from qgis.PyQtg.QtCore import QFileDialog
except ImportError:
    from qgis2compat.PyQt.QtCore import QFileDialog
```

```Regexp
from qgis2compat\.(PyQt.*)
try:\n    from qgis.$1\nexcept ImportError:\n    from qgis2compat.$1
```

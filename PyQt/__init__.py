# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : November 2015
    Copyright            : (C) 2015 by Marco Bernasocchi
    Email                : marco at opengis dot ch
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Marco Bernasocchi'
__date__ = 'September 2016'
__copyright__ = '(C) 2016, Marco Bernasocchi'
# This will get replaced with a git SHA1 when you do a git archive
__revision__ = '$Format:%H$'

is_from_qgis2compat = True
from QtCore import *
from Qsci import *
from Qt import *
from QtGui import *
from QtNetwork import *
from QtPrintSupport import *
from QtSql import *
from QtSvg import *
from QtTest import *
try:
    from QtWebKit import *
    from QtWebKitWidgets import *
except ImportError:
    # Some distros don't ship that (newer Ubuntu/Debian mainly)
    pass
from QtWidgets import *
from QtXml import *

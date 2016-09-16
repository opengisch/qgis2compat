import sys
import os

from unittest import TestCase


class TestQgis2Compat(TestCase):
    def test_import(self):
        # qgis.PyQt and qgis2compat.PyQt available
        try:
            from qgis.PyQt.QtCore import QDateTime
            print('using qgis.PyQt')
        except ImportError:
            from qgis2compat.PyQt.QtCore import QDateTime
            print('using qgis2compat.PyQt')

        # qgis.PyQt missing and qgis2compat.PyQt available
        try:
            from qgis.PyQtNOTEXISTING.QtCore import QDateTime
            print('using qgis.PyQt')
        except ImportError:
            from qgis2compat.PyQt.QtCore import QDateTime
            print('using qgis2compat.PyQt')

        # qgis.PyQt available and qgis2compat.PyQt missing
        try:
            from qgis.PyQt.QtCore import QDateTime
            print('using qgis.PyQt')
        except ImportError:
            from qgis2compatNOTEXISTING.PyQt.QtCore import QDateTime
            print('using qgis2compat.PyQt')

        # qgis.PyQt and qgis2compat.PyQt available
        with self.assertRaises(ImportError):
            try:
                from qgis.PyQtNOTEXISTING.QtCore import QDateTime
                print('using qgis.PyQt')
            except ImportError:
                from qgis2compatNOTEXISTING.PyQt.QtCore import QDateTime
                print('using qgis2compat.PyQt')

    def test_init_example_code(self):
        try:
            from qgis.PyQt.QtCore import Qt
        except ImportError:
            try:
                from qgis2compat.PyQt.QtCore import Qt
            except ImportError:
                raise

        try:
            from qgis.PyQtNOTEXISTING.QtCore import Qt
        except ImportError:
            try:
                from qgis2compat.PyQt.QtCore import Qt
            except ImportError:
                raise

        try:
            from qgis.PyQt.QtCore import Qt
        except ImportError:
            try:
                from qgis2compatNOTEXISTING.PyQt.QtCore import Qt
            except ImportError:
                raise

        with self.assertRaises(ImportError):
            try:
                from qgis.PyQtNOTEXISTING.QtCore import Qt
            except ImportError:
                try:
                    from qgis2compatNOTEXISTING.PyQt.QtCore import Qt
                except ImportError:
                    raise

    def test_new_init(self):
        #emulate QGIS path
        sys.path.append(os.path.abspath(__file__ + "/../../../"))

        import qgis
        qgis_package_path = sys.modules['qgis'].__file__
        pyqt_package_path = sys.modules['qgis.PyQt'].__file__

        #the qgis global package should have nothing to do with qgis2compat
        self.assertNotIn('qgis2compat', qgis_package_path)
        #the qgis.PyQt global package shouldcome from qgis2compat
        self.assertIn('/qgis2compat/PyQt/__init__.py', pyqt_package_path)

        # try importing a special member existing only in qgis2compat
        from qgis.PyQt import is_from_qgis2compat

        # try various imports
        from qgis.PyQt.QtCore import qVersion
        import qgis.PyQt
        import qgis.PyQt.QtGui
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

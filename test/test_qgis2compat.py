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

        import qgis2compat
        print dir(qgis2compat.qgis.PyQt)
        assert 'QGIS2Compat_exist' in dir(qgis2compat.qgis.PyQt)

        from qgis.PyQt.QtCore import qVersion
        from qgis2compat.qgis.PyQt.QGIS2Compat_test import QGIS2Compat_exist

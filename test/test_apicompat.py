from unittest import TestCase


class TestApicompat(TestCase):
    def test_import(self):
        import qgis.core
        with self.assertRaises(AttributeError):
            qgis.core.QgsVectorLayer.writeLayerXml
            qgis.core.QgsVectorLayer.writeLayerXML

        import apicompat
        qgis.core.QgsVectorLayer.writeLayerXml
        qgis.core.QgsVectorLayer.writeLayerXML


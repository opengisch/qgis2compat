import qgis.core
import qgis.utils
from qgis2compat import log


log('Monkeypatching QgsVectorLayer')

def QgsVectorLayer_writeLayerXML(self, XMLMapLayer, XMLDocument):
    self.writeLayerXML(XMLMapLayer, XMLDocument)

qgis.core.QgsVectorLayer.writeLayerXml = QgsVectorLayer_writeLayerXML


def QgsVectorLayer_readLayerXML(self, XMLMapLayer):
    self.readLayerXML(XMLMapLayer)

qgis.core.QgsVectorLayer.readLayerXml = QgsVectorLayer_readLayerXML

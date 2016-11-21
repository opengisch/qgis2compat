# coding=utf-8
import qgis.core
import qgis.utils
from qgis2compat import log


log('Monkeypatching QgsProject')

def visibilityPresetCollection(self):
    return self.visibilityPresetCollection()

qgis.core.QgsProject.mapThemeCollection = visibilityPresetCollection

# implement your custom callback methods here

import logging
import os
import sys
import de.bughome.python.power.images
import de.bughome.python.power.models

class PerformanceMode(object):
    
    def __init__(self, modeName, imageFactoryMethod, applyScript):
        self.modeName = modeName
        self.imageFactoryMethod = imageFactoryMethod
        self.applyScript = applyScript

    def createImage(self):
        return self.imageFactoryMethod()
    
    def applyPowerMode(self):
        logging.debug('Applying ' + self.modeName + ' power mode')
        os.system(self.applyScript)
    
performanceModels = [
    PerformanceMode(
        'performance',
        de.bughome.python.power.images.createPerformanceImage,
        'sudo power performance'
    ),
    PerformanceMode(
        'green',
        de.bughome.python.power.images.createGreenImage,
        'sudo power green'
    )
]

def getPerformanceMode(model):
    return performanceModels[model.powerMode]

def onSwitchClicked(widget):
    powerMode = de.bughome.python.power.models.model.powerMode + 1
    if(powerMode >= len(performanceModels)):
        powerMode = 0
        
    de.bughome.python.power.models.model.powerMode = powerMode

def onExitClicked(widget):
    sys.exit(0)
    
def onSwitchUpdate(widget, model, oldValue, newValue):
    widget.set_image(getPerformanceMode(model).createImage())

def performPowerModeChangeListener(model, oldValue, newValue):
    getPerformanceMode(model).applyPowerMode()

de.bughome.python.power.models.model.powerModeChangeListeners.append(performPowerModeChangeListener)
performPowerModeChangeListener(de.bughome.python.power.models.model, de.bughome.python.power.models.model.powerMode, de.bughome.python.power.models.model.powerMode)

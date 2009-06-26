# implement your custom callback methods here

import logging
import os
import sys
import de.bughome.python.locale_switch.images
import de.bughome.python.locale_switch.models

class KeyboardLayout(object):
    
    def __init__(self, layoutName, imageFactoryMethod, applyScript):
        self.layoutName = layoutName
        self.imageFactoryMethod = imageFactoryMethod
        self.applyScript = applyScript
        
    def createImage(self):
        return self.imageFactoryMethod()
    
    def applyLayout(self):
        logging.debug('Applying ' + self.layoutName + ' layout')
        os.system(self.applyScript)
    
keyboardLayouts = [
    KeyboardLayout(
        'en_US',
        de.bughome.python.locale_switch.images.createFlagUSImage,
        '/home/marook/apps/scripts/switch_kb_en'
    ),
    KeyboardLayout(
        'de_DE',
        de.bughome.python.locale_switch.images.createFlagGermanyImage,
        '/home/marook/apps/scripts/switch_kb_de'
    )
]

def getKeyboardLayout(model):
    if(model.keyboardLayout == None):
        model.keyboardLayout = 0
        
    return keyboardLayouts[model.keyboardLayout]
    
def performKeyboardLayoutChangeListener(model, oldValue, newValue):
    getKeyboardLayout(model).applyLayout()
    
de.bughome.python.locale_switch.models.model.keyboardLayoutChangeListeners.append(performKeyboardLayoutChangeListener)

def onSwitchUpdate(widget, model, oldValue, newValue):
    keyboardLayout = getKeyboardLayout(model)
    
    # widget.set_label(keyboardLayout.layoutName)
    widget.set_image(keyboardLayout.createImage())
    
def onSwitchClicked(widget):
    if(de.bughome.python.locale_switch.models.model.keyboardLayout == 0):
        de.bughome.python.locale_switch.models.model.keyboardLayout = 1
    else:
        de.bughome.python.locale_switch.models.model.keyboardLayout = 0

def onExitClicked(widget):
    sys.exit(0)

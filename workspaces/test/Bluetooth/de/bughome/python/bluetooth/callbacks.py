# implement your custom callback methods here

import bluetooth
import gtk
import sys
import de.bughome.python.bluetooth.composites

class Device(object):
    
    def __init__(self, name, macAddress):
        self.name = name
        self.macAddress = macAddress

def bluetoothEnabledToggledCallback(widget):
    pass

def devicesUpdateCallback(widget, model, oldValue, newValue):
    # TODO disconnect model before the updated
    listStore = widget.get_model()
    listStore.clear()
    
    for visibleDevice in model.visibleDevices:
        listStore.append([visibleDevice.name, visibleDevice.macAddress])

def refreshClickedCallback(widget):
    # TODO fetch devices in a separate thread
    model = de.bughome.python.bluetooth.models.model
    nearbyDevices = bluetooth.discover_devices(lookup_names = True)
    
    model.visibleDevices = [Device(name, addr) for name, addr in nearbyDevices]

def discoverDevicesActivateCallback(widget):
    composite = de.bughome.python.bluetooth.composites.DevicesList()
    composite.refreshClickedCallback = refreshClickedCallback
    composite.devicesUpdateCallback = devicesUpdateCallback
    
    w = gtk.Window()
    w.add(composite.rootWidget)
    w.show_all()

def bluetoothEnabledUpdateCallback(widget, model, oldValue, newValue):
    pass

def exitActivateCallback(widget):
    sys.exit(0)

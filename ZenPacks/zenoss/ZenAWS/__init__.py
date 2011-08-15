###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2009, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

import Globals
import os.path
import sys

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

libDir = os.path.join(os.path.dirname(__file__), 'lib')
if os.path.isdir(libDir):
    sys.path.append(libDir)
    
# add/remove zproperties

from Products.ZenModel.ZenPack import ZenPackBase

class ZenPack(ZenPackBase):
    "ZenPack Loader that loads zProperties used by ZenAWS"
    packZProperties = [
        ('zEC2Secret', '', 'password'),
        ]
    def install(self, app):
        ZenPackBase.install(self, app)
        dc = app.dmd.Devices.createOrganizer('/AWS/EC2')
        dc.setZenProperty('zCollectorPlugins', 
                            ('zenoss.aws.EC2InstanceMap',))
        dc.setZenProperty('zPythonClass', 'ZenPacks.zenoss.ZenAWS.EC2Manager')
        if dc.devices._getOb('EC2Manager', None): return
        ec2m = dc.createInstance('EC2Manager')
        ec2m.setPerformanceMonitor('localhost')


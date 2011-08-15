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

__doc__="""EC2InstanceMap
Model Amazon WS EC2 information
"""

from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin
from Products.ZenUtils.Utils import zenPath
from twisted.internet.utils import getProcessOutput
import re, os


class EC2InstanceMap(PythonPlugin):
    
    transport = "python"
    maptype = "EC2InstanceMap"

    deviceProperties = PythonPlugin.deviceProperties + ('access_id', 'zEC2Secret')
    
    def findPath(self):
        path = []
        for p in __file__.split(os.sep):
            if p == 'modeler': break
            path.append(p)
        return os.sep.join(path)
        
    def collect(self, device, log):
        path = self.findPath()
        log.info("running zenec2modeler plugin")
        cmd = path+'/libexec/zenec2modeler.py'
        py = zenPath("bin","python")
        args = (cmd,)
        os.environ['AWS_ACCESS_KEY_ID'] = device.access_id
        os.environ['AWS_SECRET_ACCESS_KEY'] = device.zEC2Secret
        ret = getProcessOutput(py, args, os.environ)
        return ret

    def process(self, device, results, log):
        om = self.objectMap()
        if results.startswith('ERROR:'):
            log.warn(results.replace('ERROR:', ''))
        else:
            om.setInstances = results
        return om

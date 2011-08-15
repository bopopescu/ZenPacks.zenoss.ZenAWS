###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.template import RRDDataSourceInfo
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info 

from ZenPacks.zenoss.ZenAWS.interfaces import ICWMonitorDataSourceInfo, \
                                              IEC2InstanceInfo, \
                                              IEC2InstanceTypeInfo


class CWMonitorDataSourceInfo(RRDDataSourceInfo):
    implements(ICWMonitorDataSourceInfo)
    timeout = ProxyProperty('timeout')
    cycletime = ProxyProperty('cycletime')

    @property
    def testable(self):
        """
        We can NOT test this datsource against a specific device
        """
        return False

class EC2InstanceTypeInfo(ComponentInfo):
    implements(IEC2InstanceTypeInfo)
    
    @property
    @info
    def name(self):
        return self._object.name()

class EC2InstanceInfo(ComponentInfo):
    implements(IEC2InstanceInfo)
    
    @property
    @info
    def instance_id(self):
        return self._object.titleOrId()
    
    @property
    @info
    def device(self):
        return {
            'uid': self._object.getDeviceLink(),
            'name': self._object.getDeviceName()
        } 
    
    @property
    @info
    def dns_name(self):
        return self._object.dns_name
    
    @property
    @info
    def placement(self):
        return self._object.placement
    
    @property
    @info
    def instance_type(self):
        return self._object.instance_type
    @property
    @info
    def image_id(self):
        return self._object.image_id

    @property
    @info
    def state(self):
        return self._object.state




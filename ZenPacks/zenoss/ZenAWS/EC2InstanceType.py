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

from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenRelations.RelSchema import ToOne, ToMany, ToManyCont
from Products.ZenModel.ZenossSecurity import ZEN_VIEW

class EC2InstanceType(DeviceComponent, ManagedEntity):
    """
    A DMD Device that represents a group of VMware hosts 
    that can run virtual devices.
    """

    meta_type = "EC2InstanceType"
    
    instLink = ""
    
    _properties = (
        {'id':'instLink', 'type':'string', 'mode':'w'},
        )


    _relations = (
        ('instances', ToMany(ToOne, 
            "ZenPacks.zenoss.ZenAWS.EC2Instance", "instanceType")),
        ('manager', ToOne(ToManyCont, 
            "ZenPacks.zenoss.ZenAWS.EC2Manager", "instanceTypes")),
        )

    factory_type_information = (
        {
            'immediate_view' : 'ec2InstanceTypeStatus',
            'actions'        :
            (
                { 'id'            : 'status'
                , 'name'          : 'Status'
                , 'action'        : 'ec2InstanceTypeStatus'
                , 'permissions'   : (ZEN_VIEW, )
                },
                { 'id'            : 'events'
                , 'name'          : 'Events'
                , 'action'        : 'viewEvents'
                , 'permissions'   : (ZEN_VIEW, )
                },
                { 'id'            : 'perfConf'
                , 'name'          : 'Template'
                , 'action'        : 'objTemplates'
                , 'permissions'   : ("Change Device", )
                },
            )
         },
        )
        
    def device(self):
        return self.manager()
        
        
    def name(self):
        return self.getId()
    
    def updateFromDict(self, propDict):
        for k, v in propDict.items():
            setattr(self, k, v)

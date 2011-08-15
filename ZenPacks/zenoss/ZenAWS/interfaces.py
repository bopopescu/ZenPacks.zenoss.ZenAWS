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
from Products.Zuul.interfaces import IRRDDataSourceInfo
from Products.Zuul.interfaces import IBasicDataSourceInfo, IFacade,\
                                     IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IAWSFacade(IFacade):
    """
    A facade for AWS
    """

    def configure(access_id, secret, devicePath='', devicePathForWindows=''):
        """
        @param access_id: AWS id
        @param secret: AWS secret for authentication
        @param devicePath: 
        @param devicePathForWindows: 
        """

class ICWMonitorDataSourceInfo(IRRDDataSourceInfo):
    timeout = schema.Int(title=_t(u'Timeout (seconds)'))
    cycletime = schema.Int(title=_t(u'Cycle Time (seconds)'))


class IEC2InstanceTypeInfo(IComponentInfo):
    """
    Info adapter for EC2InstanceType components.
    """
    name = schema.TextLine(title=u"Name", readonly=True)

class IEC2InstanceInfo(IComponentInfo):
    """
    Info adapter for C2Instance components.
    """
    instance_id = schema.TextLine(title=u"Instance ID", readonly=True)
    device = schema.Entity(title=u"Device", readonly=True)
    dns_name = schema.TextLine(title=u"DNS Name", readonly=True)
    placement = schema.TextLine(title=u"Placement", readonly=True)
    instance_type = schema.Entity(title=u"Instance Type", readonly=True)
    state = schema.TextLine(title=u"state", readonly=True)

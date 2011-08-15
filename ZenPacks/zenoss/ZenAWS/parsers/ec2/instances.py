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

"""
"""

from Products.ZenRRD.ComponentCommandParser import ComponentCommandParser

class instances(ComponentCommandParser):

    componentSplit = '\n'

    componentScanner = r'^\S+:(?P<component>\S+)'

    scanners = [
        r'.*CPUUtilization (?P<CPUUtilization>[\d\.]+).*',
        r'.*NetworkIn (?P<NetworkIn>[\d\.]+).*',
        r'.*NetworkOut (?P<NetworkOut>[\d\.]+).*',
        r'.*DiskReadBytes (?P<DiskReadBytes>[\d\.]+).*',
        r'.*DiskWriteBytes (?P<DiskWriteBytes>[\d\.]+).*',
        r'.*DiskReadOps (?P<DiskReadOps>[\d\.]+).*',
        r'.*DiskWriteOps (?P<DiskWriteOps>[\d\.]+).*'
        ]

    componentScanValue = 'id'
    

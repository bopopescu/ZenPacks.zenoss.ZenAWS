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
from Products.ZenRRD.CommandParser import CommandParser

class manager(CommandParser):

    def processResults(self, cmd, result):
        """
        """
        dps = dict([(dp.id, dp) for dp in cmd.points])
        
        parts = cmd.result.output.split()[1:]
        for i in range(0, len(parts), 2):
            dpname = parts[i]
            if dpname in dps:
                result.values.append((dps[parts[i]], float(parts[i+1])))
        return result

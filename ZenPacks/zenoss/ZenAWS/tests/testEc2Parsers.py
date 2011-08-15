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

import os

from Products.ZenRRD.tests.BaseParsersTestCase import BaseParsersTestCase

from ZenPacks.zenoss.ZenAWS.parsers.ec2.instances import instances
from ZenPacks.zenoss.ZenAWS.parsers.ec2.manager import manager


class Ec2ParsersTestCase(BaseParsersTestCase):

    def testEc2Parsers(self):
        """
        Test all of the parsers that have test data files in the data
        directory.
        """
        
        parserMap = {
            'instances' : instances,
            'list instances' : instances,
            'manager' : manager
                     }
        
        datadir = "%s/parserdata/ec2" % (
                        os.path.dirname(__file__))

        self._testParsers(datadir, parserMap)

        
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(Ec2ParsersTestCase))
    return suite

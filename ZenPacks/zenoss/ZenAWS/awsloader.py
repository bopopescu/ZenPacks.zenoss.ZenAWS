######################################################################
#
# Copyright 2010 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

import logging
log = logging.getLogger('zen.AWSLoader')

from zope.interface import implements
from transaction import commit

from Products.Zuul import getFacade
from Products.ZenModel.interfaces import IDeviceLoader

class AWSLoader(object):
    implements(IDeviceLoader)
    """
    Loader for the ZenAWS ZenPack
    """

    def load_device(self, dmd, access_id, secret,
                    path='', windowspath=''):
        getFacade('aws', dmd).configure(
                    access_id, secret, path, windowspath)
        commit()
        mgrPath = '/zport/dmd/Devices/AWS/EC2/devices/EC2Manager'
        mgr = dmd.restrictedTraverse(mgrPath)
        mgr.collectDevice()


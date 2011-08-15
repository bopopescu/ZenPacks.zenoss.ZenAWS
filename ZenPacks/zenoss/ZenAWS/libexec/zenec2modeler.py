#!/usr/bin/env python
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

import sys
import os
import pickle
import pprint
import logging
logging.basicConfig(level=logging.CRITICAL,)

libDir = os.path.join(os.path.dirname(__file__), '../lib')
if os.path.isdir(libDir):
    sys.path.append(libDir)

import boto
import boto.exception

class ZenEC2Modeler(object):
    
    keys = (
        "id",
        "dns_name",
        "public_dns_name",
        "image_id",
        "instance_type",
        "kernel",
        "key_name",
        "launch_time",
        "monitored",
        "placement",
        "ramdisk",
        "state",
        "region",
        )

    def __init__(self):
        self.getopts()
        try:
            if self.opts.file:
                self.conn_kwargs = {}
            else:
                if not self.opts.userkey:
                    print "ERROR:No access key ID has been provided"
                    sys.exit(1)
                elif not self.opts.privatekey:
                    print "ERROR:No secret access key has been provided"
                    sys.exit(1)
                self.conn_kwargs = {
                    'aws_access_key_id': self.opts.userkey,
                    'aws_secret_access_key': self.opts.privatekey,
                }
            conn = boto.connect_ec2(**self.conn_kwargs)
            self.regions = conn.get_all_regions()
            
            # create ami platform lookup
            self._amiPlatforms = {}
            for region in self.regions:
                self._amiPlatforms[region.name] = {}
        except boto.exception.EC2ResponseError, ex:
            print "ERROR:%s" % ex.error_message
            sys.exit(1)

    def getAmiPlatform(self, image_id, region, conn):
        if self._amiPlatforms[region].has_key(image_id) is False:
            images = conn.get_all_images(image_id)
            if images and len(images) == 1:
                self._amiPlatforms[region][image_id] = images[0]
            else:
                self._amiPlatforms[region][image_id] = None
        if self._amiPlatforms[region][image_id]:
            return self._amiPlatforms[region][image_id].platform
        return None
    
    def makeMaps(self):
        ec2instances = []
        try:
            for region in self.regions:
                conn = region.connect(**self.conn_kwargs)
                amiPlatforms = {}
                for reservation in conn.get_all_instances():
                    for instance in reservation.instances:
                        if instance.state == 'terminated': continue
                        if not instance.monitored: instance.monitor()
                        ec2instance = self.buildProxyDict(instance)
                        ec2instance['platform'] = \
                            self.getAmiPlatform(str(instance.image_id),
                                           region.name, conn)
                        ec2instances.append(ec2instance)
        except boto.exception.EC2ResponseError, ex:
            print "ERROR:%s" % ex.error_message
            sys.exit(1)
        else:
            if self.opts.show:
                pprint.pprint(ec2instances)
            else:
                pickle.dump(ec2instances, sys.stdout)


    def buildProxyDict(self, inst):
        d = dict()
        for k in self.keys:
            d[k] = getattr(inst, k)
        # We need the id to be a String-type string, not unicode
        if d.has_key('id'):
            d['id'] = str( d['id'] )
        if d.has_key('region'):
            d['region'] = str( d['region'].name )
        return d


    def getopts(self):
        from optparse import OptionParser
        parser = OptionParser()
        parser.add_option("-f", "--file", action="store_true", dest="file",
            help="use the boto config file for authentication")
        parser.add_option("-s", "--show", action="store_true", dest="show",
            help="use the boto config file for authentication")
        parser.add_option("-u","--userkey", dest="userkey",
                          default=os.environ.get('AWS_ACCESS_KEY_ID', None))
        parser.add_option("-p","--privatekey", dest="privatekey",
                          default=os.environ.get('AWS_SECRET_ACCESS_KEY', None))
        self.opts, self.args = parser.parse_args()


if __name__ == '__main__':
    zecm = ZenEC2Modeler()
    zecm.makeMaps()

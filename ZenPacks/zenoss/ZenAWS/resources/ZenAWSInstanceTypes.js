/*
###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2011, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
*/

(function() {
/*
* Custom component panels for UCS specific device components.
*/
var ZC = Ext.ns('Zenoss.component');

// EC2InstanceTypePanel: a ComponentGridPanel customization for ZenAWS EC2 Instance
// types.
ZC.EC2InstanceTypePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EC2InstanceType',
            autoExpandColumn: 'name',
            fields: [
                {name: 'uid'},
                {name: 'name'}
            ],
            columns: [{
                id: 'name',
                dataIndex: 'name',
                header: _t('Instance Type'),
                width: 80,
                sortable: true
            }]
        });
        ZC.EC2InstanceTypePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('EC2InstanceTypePanel', ZC.EC2InstanceTypePanel);
ZC.registerName('EC2InstanceType', _t('Instance Type'), _t('Instance Types'));

}());

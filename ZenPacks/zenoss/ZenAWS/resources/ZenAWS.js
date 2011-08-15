/*
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
*/

(function() {
/*
* Custom component panels for UCS specific device components.
*/
var ZC = Ext.ns('Zenoss.component');

function render_link(ob) { 
    if (ob && ob.uid) { 
        return Zenoss.render.link(ob.uid); 
    } else { 
        return ob;  
    } 
}

// EC2InstancePanel: a ComponentGridPanel customization for ZenAWS EC2 Instance
// components.
ZC.EC2InstancePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EC2Instance',
            autoExpandColumn: 'state',
            fields: [
                {name: 'uid'},
                {name: 'instance_id'},
                {name: 'device'},
                {name: 'placement'},
                {name: 'instance_type'},
                {name: 'image_id'},
                {name: 'state'}
            ],
            columns: [{
                id: 'instance_id',
                dataIndex: 'instance_id',
                header: _t('Instance ID'),
                width: 80,
                sortable: true
            },{
                id: 'device',
                dataIndex: 'device',
                header: _t('Device'),
                renderer: Zenoss.render.default_uid_renderer,
                width: 280,
                sortable: true
            },{
                id: 'placement',
                dataIndex: 'placement',
                header: _t('Placement'),
                width: 80,
                sortable: true
            },{
                id: 'instance_type',
                dataIndex: 'instance_type',
                header: _t('Instance Type'),
                width: 80,
                sortable: true
            },{
                id: 'image_id',
                dataIndex: 'image_id',
                header: _t('AMI ID'),
                width: 80,
                sortable: true
            },{
                id: 'state',
                dataIndex: 'state',
                header: _t('State'),
                width: 80,
                sortable: true
            }]
        });
        ZC.EC2InstancePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('EC2InstancePanel', ZC.EC2InstancePanel);
ZC.registerName('EC2Instance', _t('Instance'), _t('Instances'));

}());

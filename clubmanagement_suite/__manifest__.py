# -*- coding: utf-8 -*-
{
    'name': "Clubmanagement Suite - Global",

    'summary': "Global settings and configurations",

    'description': """
        This module includes global settings and configuration for Clubmanagement Suite like general groups and permissions
    """,

    'author': "Michael Blickenstorfer <michi@blicki.ch>",
    'maintainer': "Michael Blickenstorfer <michi@blicki.ch>",
    'website': "https://blicki.ch",
    'license': 'LGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'CRM',
    'version': '18.0.0.1',
    'application': True,
    'installable': True,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'web',
        'account',
        'hr',
        'hr_contract',
    ],

    # always loaded
    'data': [
        'security/clubadministration_groups.xml',
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    
    # (Un-)installation control hooks
    # will be specified in hooks.py
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    
    'external_dependencies': {
        'python': [
        ],
        'bin': [
        ],
    },
    
}


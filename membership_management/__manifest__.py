# -*- coding: utf-8 -*-
{
    'name': "Membership Management",

    'summary': "Club Membership Management",

    'description': """
        =====================
        Membership Management
        =====================
        Description
        -----------
        Enabling business processes throughout whole Membership Lifecycle:
        - Member registration process
        - Member specification with additional fields (using *contract* module)
        - Member classification (Org management in *hr* module)
        - Member reporting
        - Member Leave
        
        Installation
        ------------
        - **Pre-Requisits**: nothing
        - **Installation**: Just activate the module
        
        Configure
        ---------
        See Clubmanagement => Configuration => Membership
        
        Roadmap / Known Issues
        ----------------------
        *no releases yet*
        
        Authors
        -------
        Michael Blickenstorfer <michi@blicki.ch>
        
        History
        -------
        18.0.0.1 Pre-Release
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
        'clubmanagement_suite'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
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


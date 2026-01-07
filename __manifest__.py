# -*- coding: utf-8 -*-
{
    'name': "Odoo Matrix",

    'summary': """Odoo企业版""",

    'description': """本模块仅供参考学习使用, 企业使用请购买官方正版License, 请在下载后24小时内删除, 因使用本模块引发的法律纠纷与作者无关。""",

    'author': "Odoo SA.",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '17.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    'assets':{
        # 'web.assets_backend':[
        #     'odoo_matrix/static/src/js/config.js'
        # ]
    },

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'auto_install': True
}

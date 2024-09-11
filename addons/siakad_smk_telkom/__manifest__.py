# -*- coding: utf-8 -*-
{
    'name': "siakad smk telkom",

    'summary': """
        Siakad telkom""",

    'description': """
        Siakad telkom
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.01',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/tahun_pelajaran.xml',
        'views/jurusan.xml',
        'views/kelas.xml',
        'views/kelas_tahun_ajaran.xml',
        'views/orang_tua.xml',
        'views/guru_karyawan.xml',
        'views/mata_pelajaran.xml',
        'views/ekstrakurikuler.xml',
        'views/organisasi.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

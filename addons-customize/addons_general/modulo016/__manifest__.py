# coding: utf-8


{
    'name': 'Wizard Hello',
    'version': '1.0.0',
    'author': 'Paula Ascaso',
    'maintainer': 'Paula Ascaso',
    'category': 'Extra Tools',
    'summary': 'Botón que lanza una ventana emergente.',
    'depends': ['base','sale','stock'],
    'data': [
        'views/view.xml',
        'wizard/wizard_hello_views.xml',
        'security/modulo016_security.xml',
        'security/ir.model.access.csv'
    ],
    'qweb': [
        'static/src/xml/qweb.xml',
    ]
}

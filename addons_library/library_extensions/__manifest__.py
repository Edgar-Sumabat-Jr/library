
{
    'name': 'Library Extensions',
    'version': '1.0',
    'category': 'Library',
    'summary': 'Extensions for the Library Management System',
    'depends': ['library'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_category_views.xml',
        'views/book_views.xml',
    ],
    'installable': True,
    'application': False,
}

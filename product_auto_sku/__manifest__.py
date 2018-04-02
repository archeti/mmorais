# -*- coding: utf-8 -*-
{
    'name': 'Auto SKU for products',
    'version': '8.0.0.1.0',
    'author': 'Loïc Faure-Lacroix',
    'maintainer': '',
    'website': 'http://archeti.ca',
    'license': 'AGPL-3',
    'category': 'Others',
    'summary': '',
    'description': """
""",
    'depends': [
        'product',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'data/ir_sequence.xml',
        'views/product_attribute_value.xml',
        'views/product_category.xml',
        'views/product_template.xml',
        'views/product_product.xml',
    ],
    'installable': True,
    'application': True,
}

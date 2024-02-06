{
    'name': 'Bank Management System',
    'version': '1.0.0',
    'category': 'Administration',
    'author': 'Alay Shah',
    'sequence': 1,
    'summary': 'Bank  management system ',
    'description': """This module contains all the common features of Bank Management System """,
    'depends': ['purchase', 'mail', 'board', 'website', 'sale', 'report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'data/cron.xml',
        'data/mail_template.xml',
        'views/bank_view.xml',
        'views/feedback.xml',
        'views/netbanking.xml',
        'views/department.xml',
        'views/list.xml',
        'views/purchase_order.xml',
        'views/withdraw.xml',
        'views/deposit.xml',
        'wizard/cancel_transfer_view.xml',
        'views/dashboard.xml',
        'views/sale_order.xml',
        'views/sale_product_url.xml',
        'views/inherit_res_partner.xml',
        'wizard/customer_report.xml',
        'report/customer_card.xml',
        'report/bank_report.xml',
        'report/t.xml',
        'report/t_action.xml',
        'controllers/template.xml',
        'controllers/website_menu.xml',
        'wizard/customer_details_wizard.xml',
        'wizard/switch_user.xml',
        'wizard/invoice_inherit_menu.xml',

    ],
    'demo': [],
    'application ': True,
    'auto_install': True,
    'assets': {
        'web.assets_backend': [
            'bank/static/src/js/tree_button.js',
        ],
        'web.assets_qweb': [
            'bank/static/src/xml/tree_button.xml',
        ],
    },

}

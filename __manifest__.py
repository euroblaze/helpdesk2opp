{
    'name': 'Enveseur Helpdesk to Opportunity Link',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'Adds button to connect Helpdesk tickets to CRM Opportunities',
    'sequence': '10',
    'license': 'AGPL-3',
    'author': 'simplify-m109',
    'website': 'https://simplify-erp.com',
    'depends': ['base', 'crm', 'helpdesk'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_ticket_button.xml',
        'views/helpdesk_to_crm_button.xml',
        'wizards/create_crm_wizard.xml',
        'wizards/link_crm_wizard.xml',
        'wizards/open_tickets_wizard.xml',

    ],
    'installable': True,
    'auto_install': False,
}


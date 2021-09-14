from odoo import api, fields, models


class OpenCRMWizard(models.TransientModel):
    _name = 'open.crm.wizard'
    _description = 'Open CRM Wizard'

    def _default_partner_ids(self):
        """ Get tickets """
        caller = self.env.context.get('active_id')
        crm_link = self.env['crm.lead'].sudo().search([('id', '=', caller)])
        target = crm_link.crmTohelp_id
        return target

    ticket_ids = fields.Many2many('helpdesk.ticket', string='Tickets', default=_default_partner_ids)


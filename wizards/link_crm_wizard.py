from odoo import api, fields, models


class LinkCRMWizard(models.TransientModel):
    _name = 'link.crm.wizard'
    _description = 'Link CRM Wizard'

    opportunity_ids = fields.Many2one('crm.lead', string='CRM Opportunities')

    def action_apply(self):
        caller = self.env.context.get('active_id')
        helpdesk = self.env['helpdesk.ticket'].sudo().search([('id', '=', caller)])
        helpdesk.link_crm(self.opportunity_ids)
        return


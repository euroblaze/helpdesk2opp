from odoo import api, fields, models


class CreateCRMWizard(models.TransientModel):
    _name = 'create.crm.wizard'
    _description = 'Create CRM Wizard'

    def _default_partner_ids(self):
        """ Gives default partner_ids """
        caller = self.env.context.get('active_id')
        helpdesk_link = self.env['helpdesk.ticket'].sudo().search([('id', '=', caller)])
        target = helpdesk_link.partner_id.id
        return target

    name = fields.Char(string='Opportunity name')
    user_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string='Customer', default=_default_partner_ids)

    def action_apply(self):
        caller = self.env.context.get('active_id')
        helpdesk = self.env['helpdesk.ticket'].sudo().search([('id', '=', caller)])
        data = {
            'name': self.name,
            'user_id': self.user_id.id,
            'partner_id': self.partner_id.id,
        }
        helpdesk.create_crm(data)
        return


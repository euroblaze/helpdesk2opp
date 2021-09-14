from odoo import api, fields, models


class CRMHelpdesk(models.Model):
    _inherit = "crm.lead"

    ticket_count = fields.Integer(string='Count', compute='get_ticket_count')
    crmTohelp_id = fields.One2many('helpdesk.ticket', 'helpTocrm_id', string="Tickets")

    def ticket_button(self):
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'open.crm.wizard',
            'target': 'new'
        }

    def get_ticket_count(self):
        count = 0
        for line in self.crmTohelp_id:
            count += 1
        self.ticket_count = count


class HelpdeskCRM(models.Model):
    _inherit = "helpdesk.ticket"

    helpTocrm_id = fields.Many2one('crm.lead', string='CRM Opportunity')
    opp_flag = fields.Boolean(string='What button is viewable')

    def call_create_crm_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'create.crm.wizard',
            'target': 'new'
        }

    def call_link_crm_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'link.crm.wizard',
            'target': 'new'
        }

    def create_crm(self, data):
        created = self.env['crm.lead'].sudo().create(data)
        created.write({
            'crmTohelp_id': [
                (4, self.id)
            ]
        })

    def link_crm(self, to_write):
        to_write.write({
            'crmTohelp_id': [
                (4, self.id)
            ]
        })

    def view_opportunity(self):
        return {
                'name': 'Opportunity View',
                'domain': [('crmTohelp_id', '=', self.id)],
                'view_mode': 'tree',
                'res_model': 'crm.lead',
                'type': 'ir.actions.act_window',
                'context': {'create': False},
            }
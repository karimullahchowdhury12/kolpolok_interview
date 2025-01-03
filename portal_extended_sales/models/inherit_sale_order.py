from odoo import fields, models, api, _


class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    portal_customer_id = fields.Many2one(
        'res.partner',
        string="Customer",
        domain="[('customer_rank', '>', 0)]",
        help="The customer on behalf of whom the portal user is placing this order."
    )

    @api.model
    def create(self, vals):
        # If the portal user selects a different customer, set that customer
        if 'portal_customer_id' in vals:
            vals['partner_id'] = vals['portal_customer_id']
        return super(InheritSaleOrder, self).create(vals)

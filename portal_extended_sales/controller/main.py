from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request


class CustomPortalSale(CustomerPortal):

    @property
    def _sale_order_customer_domain(self):
        """Define domain for the customer dropdown based on the portal user's access."""
        return [('customer_rank', '>', 0)]

    def _prepare_portal_layout_values(self):
        values = super(CustomPortalSale, self)._prepare_portal_layout_values()
        # Add customers accessible to the portal user
        values['available_customers'] = request.env['res.partner'].search(
            self._sale_order_customer_domain
        )
        return values

    def _get_order_values(self):
        """Include additional values for the sales order form."""
        values = super(CustomPortalSale, self)._get_order_values()
        values['available_customers'] = request.env['res.partner'].search(
            self._sale_order_customer_domain
        )
        return values

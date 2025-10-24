# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class Event(models.Model):
    _inherit = 'event.event'

    def _get_printing_sponsor_text(self):
        """Override to remove 'Powered by Odoo' from event badge printing"""
        sponsor_text = self.env['ir.config_parameter'].sudo().get_param('event.badge_printing_sponsor_text')
        # Return custom sponsor text if set, otherwise return empty string instead of "Powered by Odoo"
        return sponsor_text or ""


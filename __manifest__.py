# -*- coding: utf-8 -*-
{
    'name': 'Remove Odoo Branding',
    'version': '1.1.0',
    'category': 'Technical',
    'summary': 'Remove "Powered by Odoo" branding and add custom email footers',
    'author': 'Eventiva',
    'website': 'www.eventiva.com',
    'description': """
Remove Odoo Branding & Custom Email Footer
===========================================
This module removes "Powered by Odoo" footer text from various modules including:
- Email templates (mail, auth_signup, crm, digest, gamification, hr_expense, im_livechat, lunch, mass_mailing, portal, etc.)
- Web interfaces (web, portal)
- Point of Sale receipts and customer display
- HR Attendance public kiosk
- Marketing cards
- Website forms and profiles

Additionally, this module allows you to add a standardized custom footer to all transactional emails:
- Configure footer in Settings > General Settings > Email Footer
- Applies to helpdesk, CRM, sales, event tracks, and all other transactional emails
- Does not affect mass mailing/marketing campaigns
- Supports HTML formatting for disclaimers, legal text, or custom branding
    """,
    'depends': [
        'mail',
        'web',
        'portal',
        'auth_signup',
        'crm',
        'digest',
        'event',
        'gamification',
        'hr_attendance',
        'hr_expense',
        'im_livechat',
        'lunch',
        'marketing_card',
        'mass_mailing',
        'mass_mailing_crm',
        'mass_mailing_sale',
        'point_of_sale',
        'pos_sale',
        # Commented out modules that may not be installed:
        # 'website_crm_partner_assign',
        # 'website_profile',
        # 'website_slides',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'data/mail_template_layouts.xml',
        'data/mail_templates.xml',
        'data/web_templates.xml',
        'data/portal_templates.xml',
        'data/pos_templates.xml',
        'data/hr_attendance_templates.xml',
        'data/marketing_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'Other proprietary',
}


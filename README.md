# Remove Odoo Branding & Custom Email Footer

This module removes "Powered by Odoo" branding from various parts of the system and adds the ability to configure custom email footers for all transactional emails.

## Features

### Custom Email Footer (NEW!)

Add a standardized footer to all transactional emails:

- **Easy Configuration**: Set up your footer in Settings > General Settings > Email Footer
- **Wide Coverage**: Applies to helpdesk, CRM, sales, event tracks, and all other transactional emails
- **Marketing Safe**: Does not affect mass mailing/marketing campaigns
- **HTML Support**: Full HTML formatting for disclaimers, legal text, or custom branding
- **Multi-company**: Each company can have its own custom footer

### Removed Odoo Branding

This module removes Odoo branding from:

### Email Templates

- **mail**: Base email notification layouts (both standard and light versions)
- **auth_signup**: Password reset and set password emails
- **portal**: Portal invitation emails
- **im_livechat**: Livechat transcript emails
- **gamification**: Badge received emails
- **lunch**: Lunch order confirmation emails
- **hr_expense**: Expense approval emails
- **digest**: Digest emails
- **website_slides**: Course completion emails
- **website_crm_partner_assign**: Partner assignment emails
- **website_profile**: User profile notification emails
- **mass_mailing**: Mass mailing layouts

### Web Interfaces

- **web**: Login page and database manager
- **portal**: Portal footer

### Point of Sale

- **point_of_sale**: Receipt footer and customer display

### Other Modules

- **hr_attendance**: Public kiosk interface
- **marketing_card**: Marketing card frontend
- **im_livechat**: Livechat channel script
- **event**: Badge printing sponsor text
- **crm**: Demo email templates
- **mass_mailing_crm**: Demo mailing templates
- **mass_mailing_sale**: Demo mailing templates

## Installation

1. Copy this module to your Odoo addons directory
2. Update the app list: Go to Apps → Update Apps List
3. Search for "Remove Odoo Branding"
4. Click Install

## Configuration

### Branding Removal

After installation, the module automatically inherits and modifies the relevant templates to remove Odoo branding. No additional configuration is required.

Some templates are marked as `active="False"` and `customize_show="True"`, which means they can be activated/customized from the technical menu if needed.

### Custom Email Footer

To add your custom email footer:

1. Go to **Settings > General Settings**
2. Scroll down to the **Email Footer** section (below Email Templates)
3. Enter your custom footer content (HTML supported)
4. Click **Save**

**Example footer content:**

```html
<p style="margin-top: 4px; font-size: 10px; color: #777;">
  <strong>Confidentiality Notice:</strong> This email and any attachments are
  confidential and may be privileged. If you are not the intended recipient,
  please notify us immediately and delete this message.
</p>
```

Your custom footer will appear in all transactional emails after the company contact details.

## Notes

- This module uses XPath inheritance to surgically remove only the branding elements from templates
- Python model overrides are used for dynamic branding (e.g., event badge printing)
- The module does not affect the functionality of any features
- Company information in email footers is preserved; only the "Powered by Odoo" text is removed
- For the event module, the badge printing sponsor text will be empty by default unless set via system parameters

## Author

Eventiva (www.eventiva.com)

## License

Other proprietary

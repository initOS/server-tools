# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2017 initOS GmbH (<http://www.initos.com>).
#    Author: Andreas Zöllner <andreas.zoellner at initos.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Email Template: Filter "Currency"',
    'version': '10.0.1',
    'author': 'initOS GmbH, Odoo Community Association (OCA)',
    'website': 'https://initos.com',
    'license': 'AGPL-3',
    'description': u"""
Email Template: Filter "Currency"
=================================

This module adds an extra filter for email templates:

*currency(currency_obj=None, lang=None, use_symbol=False)*

Formats a currency value.
The optional parameter `currency_obj` allows specifying the currency browse
record, which will be used to also display the currency symbol (default: none).
The optional parameter `lang` allows specifying the language to be used for
formatting the numerical value, e.g. for displaying the decimal separator
(e.g., point or comma) (example: 'de_DE'; default: 'lang' of the context).
The optional Boolean parameter `use_symbol` indicates that the currency symbol
(or: sign, e.g. "€") should be displayed instead of the short name (or: code,
e.g. "EUR") (default: False).

Example
-------

${object.amount_total|currency(currency_obj=object.currency_id,lang=object.partner_id.lang)}

Contributors
------------
* Andreas Zöllner <andreas.zoellner@initos.com>

Acknowledgments
---------------
This module has been inspired by the module "email_template_dateutil".
     """,
    'depends': [
        'mail',
    ],
    'external_dependencies': {
        'python': [
            'jinja2',
        ],
    },
    'data': [
    ],
    'installable': True,
    'auto_install': False,
}

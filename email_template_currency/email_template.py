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
from jinja2 import contextfilter

from odoo.addons.mail.models import mail_template
from odoo.report.report_sxw import rml_parse


@contextfilter
def currency(context, value, currency_obj=None, lang=None, use_symbol=False):
    if not value and value != 0:
        return value

    user = context.get('user')
    if not user:
        return value

    cr, uid, ctx = user._cr, user._uid, context.get('ctx', {})
    if lang:
        ctx = dict(ctx)  # make a copy
        ctx['lang'] = lang
    rml_obj = rml_parse(cr, uid, '', context=ctx)
    result = rml_obj.formatLang(
        value, monetary=True, currency_obj=currency_obj)
    if currency_obj and not use_symbol:
        # HACK: replace currency symbol by name
        result = result.replace(currency_obj.symbol, currency_obj.name)
    return result


mail_template.mako_template_env.filters.update(
    currency=currency,
)

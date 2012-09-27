# -*- coding: utf-8 -*-
from hyde.plugin import Plugin
from jinja2 import contextfunction, Markup

import locale

@contextfunction
def datetime(context, val, fmt=False):
    import locale, datetime
    fmt = fmt if fmt else locale.nl_langinfo(locale.D_T_FMT)
    result = val.strftime(fmt)
    return Markup(result.decode('utf-8'))

class SiteDefaults(Plugin):

    def template_loaded(self, template):
        self.template = template
        template.env.globals['datetime'] = datetime

    def begin_text_resource(self, resource, text):
        if (resource.meta.lc):
            self.default_locale = locale.getlocale()
            locale.setlocale(locale.LC_ALL,
                (resource.meta.lc, resource.meta.encoding))
        return text

    def end_text_resource(self, resource, text):
        if (resource.meta.lc):
            locale.setlocale(locale.LC_ALL, self.default_locale)
        return text

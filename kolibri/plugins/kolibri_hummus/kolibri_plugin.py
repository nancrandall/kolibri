from __future__ import absolute_import, print_function, unicode_literals
from kolibri.core.webpack import hooks as webpack_hooks
from kolibri.plugins.base import KolibriPluginBase
from . import hooks, urls


class Hummus(KolibriPluginBase):
    def url_module(self):
        return urls

    def url_slug(self):
        return "^kolibri_hummus/"


class HummusAsset(webpack_hooks.WebpackBundleHook):
    unique_slug = "kolibri_hummus_module"
    src_file = "assets/src/app.js"


class HummusInclusionHook(hooks.HummusSyncHook):
    bundle_class = HummusAsset

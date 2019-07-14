from collections import OrderedDict
from textwrap import dedent

from .constants import UssdServiceOp


class UssdView(OrderedDict):
    name = ''
    action = ''
    ussdServiceOp = None
    message = ''
    options = None
    back = False
    home = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = self.get('name') or ''
        self.action = self.get('action') or ''
        self.ussdServiceOp = self.get('ussdServiceOp') or UssdServiceOp.PROMPT
        self.message = self.get('message') or ''
        self.options = self.get('options') or None
        self.back = self.get('back') or False
        self.home = self.get('home') or False
        
        if self.options:
            for k, v in self.options.items():
                self.options[k] = UssdView(v) if type(v) != type(UssdView()) else v


    class Meta:
        home_verbose_name = 'Main Menu'
        back_verbose_name = 'back'

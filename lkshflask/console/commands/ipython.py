# -*- coding: utf-8 -*-

try:
    import IPython
except ImportError:
    pass
else:
    from lkshflask.console.manager import manager
    from flask import _request_ctx_stack
    @manager.command
    def ipython():
        """Run interactive shell via IPython"""
        context = dict(app=_request_ctx_stack.top.app)
        IPython.embed(user_ns=context)

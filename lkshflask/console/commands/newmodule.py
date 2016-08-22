# -*- coding: utf-8 -*-

import os
import sys

from flask_script import Command, Manager, Option

from lkshflask.console.manager import manager
from lkshflask import app, APPNAME

class NewModule(Command):
    """Create new module"""

    option_list = (
        Option('--module', '-m', dest='module', required=True),
    )

    def run(self, module):
        models_path = os.path.join(app.config['WORKDIR'], 'models', *module.lower().split('::'))
        views_path = os.path.join(app.config['WORKDIR'], 'views', *module.lower().split('::'))


        if os.path.exists(models_path):
            app.logger.warning("Directory %s already exists" % models_path)
        else:
            os.makedirs(models_path)
            open(os.path.join(models_path, "__init__.py"), "w").close()

        if os.path.exists(views_path):
            app.logger.warning("Directory %s already exists" % views_path)
        else:
            os.makedirs(views_path)
            open(os.path.join(views_path, "__init__.py"), "w").close()

        app.logger.info("Successfully created module %s" % module)

manager.add_command('newmodule', NewModule())

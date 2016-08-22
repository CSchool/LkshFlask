# -*- coding: utf-8 -*-

MODEL_TEMPLATE = '''# -*- coding: utf-8 -*-

from {project_name} import db

class {class_name}(db.Model):
    """Write your docstring here"""
    id = db.Column(db.Integer(primary_key=True))

    def __init__(self):
        # Write your init code here
        pass

    def __str__(self):
        # Write your string representation code here
        pass

'''

import os
import sys

from flask_script import Command, Manager, Option

from lkshflask.console.manager import manager
from lkshflask import app, APPNAME

class NewModel(Command):
    """Create new SQLAlchemy model"""

    option_list = (
        Option('--module', '-m', dest='module', required=True),
    )

    def run(self, module):
        class_name = module.split('::')[-1]
        module_path = os.path.join(app.config['WORKDIR'], 'models', *module.lower().split('::')) + ".py"

        repl = { "project_name": APPNAME, "class_name": class_name }

        if not os.path.exists(os.path.dirname(module_path)):
            app.logger.error("Module %s not found. Directory does not exist" % '::'.join(module.split('::')[:-1]))
            sys.exit(1)

        if os.path.exists(module_path):
            app.logger.error("File %s already exists" % module_path)
            sys.exit(1)

        with open(module_path, "w") as module_file:
            module_file.write(MODEL_TEMPLATE.format(**repl))

        app.logger.info("Successfully created model %s at %s" % (module, module_path))

manager.add_command('newmodel', NewModel())

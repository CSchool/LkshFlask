# -*- coding: utf-8 -*-

import sys

from lkshflask.console.manager import manager
import lkshflask.console.commands

def main():
    try:
        result = manager.handle('', sys.argv[1:])
    except SystemExit as exception:
        result = exception.code
        sys.exit(result or 0)

if __name__ == "__main__":
    main()

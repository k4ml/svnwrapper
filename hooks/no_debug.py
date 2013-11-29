#!/usr/bin/env python

import os
import sys
import commands

hooks_disabled = os.environ.get('HOOKS_DISABLED', False) in (1, '1', True)
if hooks_disabled:
    sys.exit(0)

status, output = commands.getstatusoutput("grep -r --exclude-dir='.svn' --include='*.py' 'import pdb;pdb.set_trace()' .")
if output != '':
    print "DEBUG STATEMENT(s) found:"
    print output
    sys.exit(1)

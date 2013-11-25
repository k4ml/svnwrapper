#!/usr/bin/env python

import os
import sys
import commands

status, output = commands.getstatusoutput("grep -r --exclude-dir='.svn' --include='*.py' 'import pdb;pdb.set_trace()' .")
if output != '':
    print "DEBUG STATEMENT(s) found:"
    print output
    sys.exit(1)

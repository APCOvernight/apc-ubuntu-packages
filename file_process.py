#!/usr/bin/env python

import logging
import argparse
from deb_pkg_tools import control

parser = argparse.ArgumentParser()
parser.add_argument("-f","--file", help="Update this debian file.")
parser.add_argument("-v", "--version", help="Update to this version number.")


args = parser.parse_args()

if ( (args.file is not None) and  (args.version is not None)):
    control_fields = {
    "version" : args.version
    }
    control.patch_control_file(args.file,control_fields)
else:
    print "Need version and file set."

from __future__ import print_function
import glob
import yaml
from pprint import pprint
import sys
import re
import os

makes = glob.glob("S*/report/Makefile")

for make in makes:
    d = make.replace("/Makefile", "")
    print (70 * "=")
    print (d)
    print (70 * "=")
    os.system("cd " + d + "; make > ~/all.log")

#!/usr/bin/env python

import subprocess

res = subprocess.run(['echo', 'this is for testing this script'], capture_output=True)
print(res)
#print(res.returncode)

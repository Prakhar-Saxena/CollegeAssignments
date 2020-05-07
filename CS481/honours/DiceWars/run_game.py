#!/usr/bin/env python

import sys
import os
try:
    path_main = os.path.abspath(os.path.join(os.path.dirname(__file__), 'source'))
    sys.path.insert(0, path_main)
    os.chdir(path_main)
except:
    pass
    
import singleoptions

if '-profile' in sys.argv:
    import profile
    profile.run('singleoptions.main()')
else:
    singleoptions.main()


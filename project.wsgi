activate_this = '/srv/project/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/srv/project')


from project import app as application

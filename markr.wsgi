activate_this = '/srv/markr/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/srv/markr')


from project import app as application

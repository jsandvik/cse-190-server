from fabric.api import *

# the user to use for the remote commands
env.user = 'david'

# the servers where the commands are executed
env.hosts = ['54.219.169.26']
env.keyfile = ['$HOME/.ssh/id_rsa.pub']

def pack():
    # create a new source distribution as tarball
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    # figure out the release name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    # upload the source tarball to the temporary folder on the server
    put('dist/%s.tar.gz' % dist, '/tmp/markr.tar.gz')
    # create a place where we can unzip the tarball, then enter
    # that directory and unzip it
    sudo('rm -rf /tmp/markr')
    run('mkdir /tmp/markr')
    with cd('/tmp/markr'):
        run('tar xzf /tmp/markr.tar.gz')
        # now setup the package with our virtual environment's
        # python interpreter
        run('mv ' + dist + '/* .')
                
        run('/srv/markr/venv/bin/python setup.py install')
        
        sudo('chmod 775 /srv/markr/venv/bin/easy_install* /srv/markr/venv/bin/fab* /srv/markr/venv/bin/pip*')
        
        # seed the database
        run('ln -s /srv/markr/config.py config.py')
        run('/srv/markr/venv/bin/python seed_db.py')
         
        
    # now that all is set up, delete the folder again
    run('rm -rf /tmp/markr /tmp/markr.tar.gz')
    
    # and finally touch the .wsgi file so that mod_wsgi triggers
    # a reload of the application
    run('touch /srv/markr/markr.wsgi')
    
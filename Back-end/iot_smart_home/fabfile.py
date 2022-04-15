from fabric.api import env, sudo, cd, task, run
import os


env.hosts = ['192.168.1.2']
env.password = 'ubuntu'
site_root = os.getcwd()
print(site_root)
venv = 'source %s/venv/bin/activate' % site_root.rsplit('/', 3)[0]

def _install_deps():
    sudo('%s && pip install -r %s/requirements.txt' % (venv, site_root.rsplit('/', 2)[0]))

def _migrate():
    sudo('%s && python %s/manage.py migrate' % (venv, site_root))

def _get_code():
    sudo('git pull origin main')

def _update_file():
    sudo('git fetch')
    sudo('git checkout origin/main -- %s/device_cntrl' % (os.getcwd()))

def _restore_code():
    sudo('git restore --staged -- %s/device_cntrl' % (os.getcwd()))
    sudo('git restore -- %s/device_cntrl' % (os.getcwd()))

def _reload():
    sudo('touch rebuild')

# command: fab deploy
@task(alias='deploy')
def basic_deploy():
    with cd(site_root):
        _get_code()
        _install_deps()
        _reload()

# command: fab deploy_migrations
@task(alias='deploy_migrations')
def deploy():
    with cd(site_root):
        _get_code()
        _install_deps()
        _reload()

# command: fab partially_update
@task(alias='partially_update')
def update():
    with cd(site_root):
        _update_file()
        _reload()

# command: fab restore_update
@task(alias='restore_update')
def restore():
    with cd(site_root):
        _restore_code()
        _reload()

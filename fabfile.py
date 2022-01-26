from fabric.api import env, sudo, cd, task, run
import os


env.hosts = ['192.168.1.4']
site_root = os.getcwd()
print(site_root)
venv = 'source %s/venv/bin/activate' % site_root.rsplit('/', 1)[0]

def _install_deps():
    sudo('%s && pip install -r %s/requirements.txt' % (venv, site_root))

def _migrate():
    sudo('%s && python %s/Back-end/iot_smart_home/manage.py migrate' % (venv, site_root))

def _get_code():
    sudo('git pull origin main')

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
        _migrate()
        _reload()

# JupyterHub configuration
#
## If you update this file, do not forget to delete the `jupyterhub_data` volume before restarting the jupyterhub service:
##
##     docker volume rm jupyterhub_jupyterhub_data
##
## or, if you changed the COMPOSE_PROJECT_NAME to <name>:
##
##    docker volume rm <name>_jupyterhub_data
##

import os

## Generic
c.JupyterHub.admin_access = True
c.Spawner.default_url = '/lab'

## Authenticator
## Configure authentication (delagated to GitLab)
#from oauthenticator.github import GitHubOAuthenticator
from oauthenticator.generic import GenericOAuthenticator

#c.JupyterHub.authenticator_class = GitHubOAuthenticator
#c.Authenticator.admin_users = { 'pwhitetj' }
#c.GitHubOAuthenticator.oauth_callback_url = 'https://'+os.environ.get('HOST')+'/hub/oauth_callback'
#c.GitHubOAuthenticator.client_id = os.environ.get('CLIENT_ID')
#c.GitHubOAuthenticator.client_secret = os.environ.get('CLIENT_SECRET')

c.JupyterHub.authenticator_class = GenericOAuthenticator
c.GenericOAuthenticator.userdata_url="https://ion.tjhsst.edu/api/profile"
c.GenericOAuthenticator.token_url="https://ion.tjhsst.edu/oauth/token/"
c.GenericOAuthenticator.extra_params=dict(
	client_id=os.environ.get('CLIENT_ID'),
	client_secret=os.environ.get('CLIENT_SECRET'),
        scope="read")
c.GenericOAuthenticator.oauth_callback_url = 'https://'+os.environ.get('HOST')+'/hub/oauth_callback'
c.GenericOAuthenticator.username_key="ion_username"
#c.GenericOAuthenticator.userdata_params=
c.GenericOAuthenticator.client_id = os.environ.get('CLIENT_ID')
c.GenericOAuthenticator.client_secret = os.environ.get('CLIENT_SECRET')
c.GenericOAuthenticator.basic_auth = False
c.GenericOAuthenticator.tls_verify = True

## Docker spawner
#c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
#c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
#c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
#c.JupyterHub.hub_ip = os.environ['HUB_IP']


c.JupyterHub.spawner_class = 'dockerspawner.SwarmSpawner'
# The Hub should listen on all interfaces,
# so user servers can connect
c.JupyterHub.hub_ip = '0.0.0.0'
# this is the name of the 'service' in docker-compose.yml
c.JupyterHub.hub_connect_ip = 'jupyterhub'
# this is the network name for jupyterhub in docker-compose.yml
# with a leading 'swarm_' that docker-compose adds
c.SwarmSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.SwarmSpawner.extra_host_config = {'network_mode': c.SwarmSpawner.network_name}

# start jupyterlab
c.Spawner.cmd = ["jupyter", "labhub"]

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# Other stuff
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '10G'


## Services
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]

# JupyterHub at TJHSST

Provides containerized JupyterHub spawning docker container JupyterLab notebooks. 
This is a fork of the repository described below. So far the changes have been

- Upgrade to JupyterHub 1.0.0
- Downgrade Traefik to 1.7
- Fix Traefik backend specifications
- Upload pewhitetj/* images to docker hub for deployment
- Remove some libraries from jupyterlab image
- Change Auth to Github OAuth
- Remove SSL certs since provided by nginx

### To deploy on campus

- I think you just need to edit the HOST in .env and (for now) the oAuth client_id and client_secret
since each machine has its own oauth callback (which will be removed when this is swarm based)
```{shell}
$ docker-compose build
$ docker-compose up -d
```
And make sure nginx/dns are set up appropriately

### Roadmap
This needs several edits before going live

- Should oAuth against ion (DONE)
- Should match userID to system users and mount homedir
- change jupyterLab image to something we actually use (MADE SKINNIER)
- ultimately implement docker swarm spawner for multi-server deployment
- get rid of nginx front end and add SSL certs to traefik

### References
- [Traefik](https://www.digitalocean.com/community/tutorials/how-to-use-traefik-as-a-reverse-proxy-for-docker-containers-on-ubuntu-18-04)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Docker Swarm Spawner](https://github.com/jupyterhub/dockerspawner/blob/master/examples/swarm/jupyterhub_config.py)
- [Generic OAuth](https://github.com/jupyterhub/oauthenticator/issues/107)
----------------------

# Original File: JupyterHub deployment in use at Université de Versailles

This is a [JupyterHub](https://jupyter.org/hub) deployment based on
Docker currently in use at [Université de
Versailles](https://jupyter.ens.uvsq.fr/).

## Features

- Containerized single user Jupyter servers, using
  [DockerSpawner](https://github.com/jupyterhub/dockerspawner);
- Central authentication to the University CAS server;
- User data persistence;
- HTTPS proxy.

## Learn more

This deployment is described in depth in [this blog
post](https://opendreamkit.org/2018/10/17/jupyterhub-docker/).

### Adapt to your needs

This deployment is ready to clone and roll on your own server. Read
the [blog
post](https://opendreamkit.org/2018/10/17/jupyterhub-docker/) first,
to be sure you understand the configuration.

Then, if you like, clone this repository and apply (at least) the
following changes:

- In [`.env`](.env), set the variable `HOST` to the name of the server you
  intend to host your deployment on.
- In [`reverse-proxy/traefik.toml`](reverse-proxy/traefik.toml), edit
  the paths in `certFile` and `keyFile` and point them to your own TLS
  certificates. Possibly edit the `volumes` section in the
  `reverse-proyx` service in
  [`docker-compose.yml`](docker-compose.yml).
- In
  [`jupyterhub/jupyterhub_config.py`](jupyterhub/jupyterhub_config.py),
  edit the *"Authenticator"* section according to your institution
  authentication server.  If in doubt, [read
  here](https://jupyterhub.readthedocs.io/en/stable/getting-started/authenticators-users-basics.html).

Other changes you may like to make:

- Edit [`jupyterlab/Dockerfile`](jupyterlab/Dockerfile) to include the
  software you like. Do not forget to change
  [`jupyterhub/jupyterhub_config.py`](jupyterhub/jupyterhub_config.py)
  accordingly, in particular the *"user data persistence"* section.

### Run!

Once you are ready, build and launch the application with

```
docker-compose build
docker-compose up -d
```

Read the [Docker Compose manual](https://docs.docker.com/compose/) to
learn how to manage your application.

## Acknowledgements

<img src="https://opendreamkit.org/public/logos/Flag_of_Europe.svg" height="20"> Work partially funded by the EU H2020 project
[OpenDreamKit](https://opendreamkit.org/).

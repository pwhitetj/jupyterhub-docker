FROM jupyterhub/jupyterhub:1.0.0

COPY jc.py ./jupyterhub_config.py

RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/1.0.0/examples/cull-idle/cull_idle_servers.py

RUN pip install \
    dockerspawner==0.10.0 \
    oauthenticator==0.8.0

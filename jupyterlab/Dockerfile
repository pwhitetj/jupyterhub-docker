FROM jupyter/scipy-notebook:137a295ff71b

LABEL maintainer="Patrick White <pewhite@tjhsst.edu>"

USER root

# APT packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

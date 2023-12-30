# For more information, please refer to https://aka.ms/vscode-docker-python
FROM mcr.microsoft.com/devcontainers/python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install updates
RUN \
    apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y upgrade \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install requirements
COPY requirements.txt .
RUN \
    python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt \
    && rm requirements.txt

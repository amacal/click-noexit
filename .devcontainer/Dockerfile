ARG PYTHON_VERSION
FROM mcr.microsoft.com/vscode/devcontainers/python:${PYTHON_VERSION}

ARG POETRY_VERSION
ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install pipx -y
RUN pipx ensurepath && pipx install poetry==${POETRY_VERSION}

USER vscode
RUN poetry completions bash >> ~/.bash_completion

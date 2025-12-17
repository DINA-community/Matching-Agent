FROM python:3-slim-bookworm AS build

SHELL ["sh", "-exc"]

ENV DEBIAN_FRONTEND=noninteractive

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1

WORKDIR /app

# System deps for building wheels and PostgreSQL driver, plus curl for uv install
RUN apt update \
    && apt install -y --no-install-recommends build-essential gcc libpq-dev ca-certificates default-jdk \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv

RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv venv

RUN --mount=type=cache,target=/root/.cache \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=plugins/asset_source/netbox/pyproject.toml,target=plugins/asset_source/netbox/pyproject.toml \
    --mount=type=bind,source=plugins/asset_source/isduba/pyproject.toml,target=plugins/asset_source/isduba/pyproject.toml \
    --mount=type=bind,source=plugins/asset_source/sample/pyproject.toml,target=plugins/asset_source/sample/pyproject.toml \
    --mount=type=bind,source=plugins/preprocessing/identity/pyproject.toml,target=plugins/preprocessing/identity/pyproject.toml \
    --mount=type=bind,source=plugins/preprocessing/default/pyproject.toml,target=plugins/preprocessing/default/pyproject.toml \
    uv sync  \
      --locked  \
      --no-dev  \
      --no-install-project

COPY src src
COPY plugins plugins
COPY pyproject.toml pyproject.toml
COPY README.md README.md


# Install project and required local plugins (preprocessors) using uv
RUN --mount=type=cache,target=/root/.cache \
    uv build
RUN --mount=type=cache,target=/root/.cache \
    uv build --package dina.plugins.datasource.netbox_fetcher
RUN --mount=type=cache,target=/root/.cache \
    uv build --package dina.plugins.datasource.isduba_fetcher
RUN --mount=type=cache,target=/root/.cache \
    uv build --package dina.plugins.preprocessing.default
RUN --mount=type=cache,target=/root/.cache \
    uv build --package dina.plugins.preprocessing.identity

FROM python:3.13-bookworm
SHELL ["sh", "-exc"]

# Runtime user (non-root)
RUN groupadd -r appuser
RUN useradd -r -d /app -g appuser -N appuser
STOPSIGNAL sigint

COPY --from=build --chown=appuser:appuser /app/dist /app/dist

RUN pip install --find-links=/app/dist dina-matcher[netbox-fetcher,preprocessing-identity,preprocessing-default]
RUN rm -rf /app/dist
COPY --chown=appuser:appuser docker/assets /app/assets

USER appuser

WORKDIR /app

RUN echo "JWT_SECRET_KEY=$(openssl rand -hex 32)" >> .env

## Default command can be overridden in docker-compose
CMD ["assetsync", "--config", "/app/assets/assetsync.toml"]
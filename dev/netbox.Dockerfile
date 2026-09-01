FROM netboxcommunity/netbox:v4.5

COPY ./docker-entrypoint-plugins.sh /opt/netbox/docker-entrypoint-plugins.sh
RUN chmod +x /opt/netbox/docker-entrypoint-plugins.sh \
    # The container runs as the unprivileged 'netbox' user,
    # but plugins are installed into the venv at container start.
    # That requires write access to the whole venv
    && chown -R netbox:root /opt/netbox/venv

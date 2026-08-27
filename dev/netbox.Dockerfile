FROM netboxcommunity/netbox:v4.4

COPY nginx-unit.json /etc/unit/
COPY ./docker-entrypoint-plugins.sh /opt/netbox/docker-entrypoint-plugins.sh
RUN chmod +x /opt/netbox/docker-entrypoint-plugins.sh \
    # The container runs as unpriviledged 'unit' user,
    # but plugins are installed into the venv at container start.
    # That requires write access to the whole venv
    && chown -R unit:root /opt/netbox/venv

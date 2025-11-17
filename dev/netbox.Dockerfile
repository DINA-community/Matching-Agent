FROM netboxcommunity/netbox:v4.3.1

COPY nginx-unit.json /etc/unit/
COPY ./plugin_requirements.txt /opt/netbox/
RUN apt update && apt install -y git
RUN /usr/local/bin/uv pip install -r /opt/netbox/plugin_requirements.txt
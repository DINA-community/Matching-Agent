FROM nginx:1.27-alpine

RUN apk add --no-cache openssl bash

WORKDIR /etc/nginx

COPY nginx.conf /etc/nginx/nginx.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

VOLUME ["/etc/nginx/certs"]

EXPOSE 8443

ENTRYPOINT ["/entrypoint.sh"]

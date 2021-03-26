FROM nginx:1.17.0
COPY nginx.conf /etc/nginx/nginx.conf
COPY ./static /static

RUN chmod -R 777 /var/log/nginx /var/cache/nginx /var/run \
     && chgrp -R 0 /etc/nginx \
     && chmod -R g+rwX /etc/nginx \
     && rm /etc/nginx/conf.d/default.conf

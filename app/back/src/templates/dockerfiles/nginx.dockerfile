# syntax=docker/dockerfile:1.3-labs
FROM nginx:1.29-alpine
RUN <<EOF > /usr/share/nginx/html/index.html
{{html}}
EOF

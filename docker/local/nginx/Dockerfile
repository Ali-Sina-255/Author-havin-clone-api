FROM nginx:1.23.1-alpine

# Remove the default config
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom config
COPY ./default.conf /etc/nginx/conf.d/default.conf

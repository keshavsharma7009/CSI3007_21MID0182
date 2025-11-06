# Use lightweight Nginx image for static site
FROM nginx:stable-alpine
# Remove default nginx index (optional)
RUN rm -rf /usr/share/nginx/html/*
# Copy static site into nginx folder
COPY site /usr/share/nginx/html
# Expose default HTTP port
EXPOSE 80
# Start nginx (default CMD in image already runs nginx)

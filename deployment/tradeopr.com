server {
    listen 80;
    server_name tradeopr.com www.tradeopr.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/django/tradeopr.com;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}

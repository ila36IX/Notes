# Configuration

The Nginx decide which config to use by the link file in the directory `/etc/nginx/sites-enabled`
the is links to the config to use in the directory `/etc/nginx/sites-available/`.

```nginx

server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;
		add_header X-Served-By DESKTOP-KPN5RB6;

        location / {
                try_files $uri $uri/ =404;
        }

        location /redirect_me {
                return 301 https://exemple.com;
        }

        error_page 404 /not_found.html;

        location /not_found.html {
                internal;
        }
}
```

## Reload Nginx

```bash
sudo nginx -t # Check if syntax is right
sudo nginx -s reload
```

## Error file

```
cat /var/log/nginx/error.log
```


```nginx
server {
        listen 80;

        root /home/ubuntu/AirBnB_clone_v4/web_dynamic;

        location / {
                proxy_pass http://localhost:5003/2-hbnb;
                proxy_intercept_errors on;
        }

        location /static {
                try_files $uri $uri/ =404;
        }

        location = /airbnb-onepage/ {
                proxy_pass http://localhost:5000;
        }

        location /airbnb-dynamic/number_odd_or_even/ {
                proxy_pass http://localhost:5001/number_odd_or_even/;
        }

        location /api/ {
                proxy_pass http://localhost:5002/api/;
        }

        error_page 404 /404.html;

        location = /404.html{
                root /home/ubuntu/AirBnB_clone_v4/web_dynamic/static;
                internal;
        }

        add_header X-Served-By web-01;
}
```
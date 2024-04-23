# Configuration

The Nginx decide which config to use by the link file in the directory `/etc/nginx/sites-enabled`
the is links to the config to use in the directory `/etc/nginx/sites-available/`.

```nginx
# 
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
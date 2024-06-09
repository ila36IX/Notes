# I'm sick of localhost

![Imgur](https://i.imgur.com/CbY42Hg.gif)

Finally, the time for running the **web application** in a deployment environment has arrived!

_Haaave you met **WSGI**?_

When you access a website, your browser sends a request to the web server. The web server then forwards that request to the **application server** (WSGI container) where the actual web application code is running. The application server processes the request and generates the response (HTML), which is then sent back to the web server. Finally, the web server returns the response to your browser.
Sometimes the browser will use the HTML file to request more assets (JavaScript and CSS files). This approach is handled by the web server, as these file are often just a static files, in summery this is what happening: 

1. Invoking a request to a website
2. Web server receives the request
3. Web server forwards that request to the **application server** (WSGI container)
	1. **WSGI** is handling thousands of requests for dynamic content by queuing them to the framework
	2. Frameworks job is to handle every request that is passed to it by the **WSGI**.
4. WSGI forwards the request to framework (eg. Flask)
5. Framework processes the request and gives back the response (in the form of HTML)
7. **WSGI** forwards back the response of the framework to the the web server
8. The web server returns the response to the requester

![](https://i.imgur.com/QjfSGGm.png)

What you have to know about *WSGI* is:
- It stands for *Web server getaway interface*
- WSGI container is a separate running process that runs on a different port than the web server
- WSGI is where the actual web application code is running.
- Web server is configured to pass requests to the WSGI container which runs your web application, then pass the response (in the form of HTML) back to the requester

**WSGI** seems essential, but I'm not sure how to implement it?
OK! it's time for you to meet a friend!  His name is `gunicorn`.

## Gunicorn => WSGI, BOOM!

![](https://i.imgur.com/pcZPvdz.png)

```bash
pip3 install gunicorn
```

Now we will use `guncorn` to serve the `Flask` application as a `WSGI` entry point.

We do this by binding `Gunicorn` instance to localhost listening on port `5000` with the application object as the entry point.

```
guncorn_instance = localhost:5000 + framework_app (Flaks)
```

```bash
# Instead of running the application using the `python -m`
# We give this duty to gunicorn
gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app

# In another terminal
curl 127.0.0.1:5000/airbnb-onepage/
```

Next step is using the web server (`nginx`) to proxy the requests coming from outside the server to the process running in the port `5000` (`gunicorn`), the following is example of `nginx` configuration.

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://localhost:5000;
    }
    add_header X-Served-By web-01;
}
```

To run the multiple `gunicorn` instances in the background you can use the terminal multiplexer utility `tmux`, which will simplified running multiple `gunicorn` instances.

```bash
tmux new-session -d 'export VAR=VALUE; gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
```

You access running `gunicorn` PID by running one of those commands:

```bash
pgrep -f gunicor

sudo netstat -tlnp | python
```

Here is an example of the output:

![](https://i.imgur.com/D0Ft8sU.png)

Once you’re ready to end the process you can either run:

```bash
tmux a
tmux ls
tmux a -t 23
kill -9 <PID:int>
```
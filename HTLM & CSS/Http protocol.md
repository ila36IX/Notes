## Status codes

- `200 OK`: The request was completed successfully.|
- `201 Created`: A resource has been created (for example a new user or new blog post).
- `301 Moved Permanently`: This redirects the client's browser to a new webpage or tells search engines that the page has moved somewhere else and to look there instead.
- `302 Found`: Similar to the above permanent redirect, but as the name suggests, this is only a temporary change and it may change again in the near future.
- `400 Bad Request`: This tells the browser that something was either wrong or missing in their request. This could sometimes be used if the web server resource that is being requested expected a certain parameter that the client didn't send.
- `401 Not Authorised`: You are not currently allowed to view this resource until you have authorized with the web application, most commonly with a username and password.
- `403 Forbidden`: You do not have permission to view this resource whether you are logged in or not.
- `405  Method Not Allowed`: The resource does not allow this method request, for example, you send a GET request to the resource /create-account when it was expecting a POST request instead.
- `404 Page Not Found`: The page/resource you requested does not exist.
- `500 Internal Service Error`: The server has encountered some kind of error with your request that it doesn't know how to handle properly.
- `503 Service Unavailable`: This server cannot handle your request as it's either overloaded or down for maintenance.

## Common Request Headers


**Host:** Some web servers host multiple websites so by providing the host headers you can tell it which one you require, otherwise you'll just receive the default website for the server.  

**User-Agent:** This is your browser software and version number, telling the web server your browser software helps it format the website properly for your browser and also some elements of HTML, JavaScript and CSS are only available in certain browsers.  

**Content-Length:** When sending data to a web server such as in a form, the content length tells the web server how much data to expect in the web request. This way the server can ensure it isn't missing any data.

**Accept-Encoding:** Tells the web server what types of compression methods the browser supports so the data can be made smaller for transmitting over the internet.

**Cookie:** Data sent to the server to help remember your information (see cookies task for more information).  

## Common Response Headers

These are the headers that are returned to the client from the server after a request.

**Set-Cookie:** Information to store which gets sent back to the web server on each request (see cookies task for more information). 

**Cache-Control:** How long to store the content of the response in the browser's cache before it requests it again.  

**Content-Type:** This tells the client what type of data is being returned, i.e., HTML, CSS, JavaScript, Images, PDF, Video, etc. Using the content-type header the browser then knows how to process the data.  

**Content-Encoding:** What method has been used to compress the data to make it smaller when sending it over the internet.
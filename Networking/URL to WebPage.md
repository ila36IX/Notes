[**look at ⇾**](https://aws.amazon.com/fr/blogs/mobile/what-happens-when-you-type-a-url-into-your-browser/)

When you type a URL into your browser and press Enter, a series of steps occur to take you to the website you want to visit. Here's a high-level overview of the process:

1. **URL Parsing**: The browser parses the URL to identify the protocol, host, port, and path.
   
2. **DNS Lookup**: The browser performs a DNS (Domain Name System) lookup to translate the hostname into an IP address. If the IP address is cached locally, this step is skipped.
   
3. **TCP Connection**: The browser initiates a TCP (Transmission Control Protocol) connection with the server at the resolved IP address. If the protocol is HTTPS, TLS (Transport Layer Security) handshake will also occur to establish a secure connection.
   
4. **HTTP Request**: The browser sends an HTTP request to the server, asking for the page specified in the URL.
   
5. **Server Response**: The server processes the request and sends back an HTTP response, along with the requested data, which could be an HTML page, an image, etc.
   
6. *Rendering the Web Page*: The browser begins rendering the web page. It parses the HTML content, loads CSS to style the page, and executes JavaScript code if present.
   
7. *Resource Loading*: The browser makes additional requests for resources like images, scripts, and CSS files referenced in the HTML.

8. **Display**: Once all resources are loaded and scripts are executed, the browser displays the complete web page to the user.

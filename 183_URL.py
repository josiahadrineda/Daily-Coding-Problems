"""
When a user types in a URL into their browser and presses Enter,
an exchange of requests ensues, followed by an eventual (hopefully)
rendering of the page. The process goes as follows:

1. Attempt to locate the domain name from the IP address via host cache.
    1a. If not found in the host cache, request the DNS for the IP of the host.
2. Once an IP is found, send an HTTP request to the host.
3. The host sends an HTTP response back to the client.
4. The client's web browser begins rendering the HTML received.
5. The client's web browser then repeats 3-5, instead requesting additional information embedded in the HTML.
6. Once the page is fully loaded, the server and client still remain in contact to send requests as needed.
"""
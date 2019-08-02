# HTTP Logger

Simple Python HTTP server that prints out request headers.

Start the server running in one terminal:

    $ python server.py


Make a request the the server in another terminal:

    curl -H "X-MyHeader: It works" localhost:8000


Observe the output:

    $ python server.py
    ERROR:root:Host: localhost:8000
    User-Agent: curl/7.58.0
    Accept: */*
    X-MyHeader: It works
    127.0.0.1 - - [02/Aug/2019 10:09:35] "GET / HTTP/1.1" 200 - 

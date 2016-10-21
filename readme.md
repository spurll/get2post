GET to POST
===========

A web service that accpets GET requests and submits them to a specified URL as a POST.

Usage
=====

Requirements
------------

* flask
* flask-wtf

Starting the Server
-------------------

Start the server with `run.py`. By default it will be accessible at `localhost:9999`. To
make the server world-accessible or for other options, see `run.py -h`.

If you're having trouble configuring your sever, I wrote a
[blog post](http://blog.spurll.com/2015/02/configuring-flask-uwsgi-and-nginx.html)
explaining how you can get Flask, uWSGI, and Nginx working together.

Basic Usage
-----------

Submit a GET request to the service in the following form:

```
http://SERVICE/URL?NAME1=VALUE1&NAME2=VALUE2...
```

For example:

```
http://your.server:9999/https://www.skipthedishes.ca/fox-and-fiddle?delivery_or_pickup=Delivery&postalcode=R3T6A8&op=Start%20Your%20Order&form_id=skipthedishes_start_your_order_form
```

Originally, the URL was also supplied in a GET parameter. This syntax is still available:

```
http://SERVICE?url=URL&NAME1=VALUE1&NAME2=VALUE2...
```

For example:

```
http://your.server:9999?url=https://www.skipthedishes.ca/fox-and-fiddle&delivery_or_pickup=Delivery&postalcode=R3T6A8&op=Start%20Your%20Order&form_id=skipthedishes_start_your_order_form
```

All GET parameters (except `url`, if the target URL isn't supplied in the path) are
translated into hidden `<input>` tags in the form to be submitted, with the `name`
attribute set to the parameter name and the `value` attribute set to the parameter value.

Bugs and Feature Requests
=========================

Feature Requests
----------------

None

Known Bugs
----------

None

Special Thanks
==============

Some of the implementation details were suggested by [Curtis Vogt](https://github.com/omus). Thanks!

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).

Remember: [GitHub is not my CV.](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/)

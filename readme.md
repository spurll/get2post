GET to POST
===========

A web service that accpets GET requests and submits them to a specified URL as a POST.

Installation
============

Instructions
------------

Edit `config.py` and specify the desired hostname and port, then simply execute `run.py`. (By default, it will be externally accessible. For testing on localhost, use the `--test` flag.)

Requirements
------------

* flask
* flask-wtf

Usage
=====

Submit a GET request to the service in the following form:

```
http://SERVICE/URL?NAME1=VALUE1&NAME2=VALUE2...
```

For example:

```
http://your.server:9995/https://www.skipthedishes.ca/fox-and-fiddle?delivery_or_pickup=Delivery&postalcode=R3T6A8&op=Start%20Your%20Order&form_id=skipthedishes_start_your_order_form
```

Originally, the URL was also supplied in a GET parameter. This syntax is still available:

```
http://SERVICE?url=URL&NAME1=VALUE1&NAME2=VALUE2...
```

For example:

```
http://your.server:9995?url=https://www.skipthedishes.ca/fox-and-fiddle&delivery_or_pickup=Delivery&postalcode=R3T6A8&op=Start%20Your%20Order&form_id=skipthedishes_start_your_order_form
```

All GET parameters (except `url`, if the target URL isn't supplied in the path) are translated into hidden `<input>` tags in the form to be submitted, with the `name` attribute set to the parameter name and the `value` attribute set to the parameter value.

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

Written by Gem Newman. [GitHub](https://github.com/spurll/) | [Blog](http://www.startleddisbelief.com) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/).

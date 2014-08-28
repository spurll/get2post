GET to POST
===========

A web service that accpets GET requests and submits them to a specified URL as a POST.

Installation
============

Instructions
------------

Edit `config.py` and specify the desired hostname and port, then simply execute run.py. (By default, it will be externally accessible. For testing on localhost, use the `--test` flag.)

Requirements
------------

* flask
* flask-wtf

Usage
=====

Submit a GET request to the service in the following form:

```
http://SERVICE?url=URL&NAME1=VALUE1&NAME2=VALUE2...
```

For example:

```
http://your.server:9996?url=https://www.skipthedishes.ca/fox-and-fiddle&delivery_or_pickup=Delivery&postalcode=R3T6A8&op=Start%20Your%20Order&form_id=skipthedishes_start_your_order_form
```

All GET parameters (except `url`) are translated into hidden `<input>` tags in the form to be submitted, with the `name` attribute set to the parameter name and the `value` attribute set to the parameter value.

Bugs and Feature Requests
=========================

Feature Requests
----------------

* It might be nice to be able to submit in the form ```http://SERVICE/URL?NAME1=VALUE1&NAME2=VALUE2...```. (Cleaner, and allows posting to a service that itself requres a `url` parameter.)

Known Bugs
----------

None

License Information
===================

Written by Gem Newman, with contributions from Curtis Vogt.
http://www.startleddisbelief.com

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

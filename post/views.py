# Written by Gem Newman. This work is licensed under a Creative Commons         
# Attribution-NonCommercial-ShareAlike 3.0 Unported License.                    

# Syntax:
#   http://SERVICE/URL?NAME1=VALUE1&NAME2=VALUE2...
#   http://SERVICE?url=URL&NAME1=VALUE1&NAME2=VALUE2...


from flask import render_template, flash, redirect, session, url_for, request
from flask.ext.wtf import Form
from wtforms import HiddenField

from post import app


@app.route('/', defaults={'url': ''}, methods=['GET'])
@app.route('/<path:url>', methods=['GET'])
def index(url):
    args = dict(request.args)

    if not url:
        url = args.pop("url", [None])[0]

    class POSTForm(Form):
        pass

    if url and args:
        if "://" not in url:
            url = "http://{}".format(url)

        for f in args:
            field = HiddenField(f, default=args[f][0])
            setattr(POSTForm, f, field)

        print "Posting to {}...".format(url)

    form = POSTForm()

    return render_template("index.html", url=url, form=form, fields=args)


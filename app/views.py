# Written by Gem Newman. This work is licensed under a Creative Commons         
# Attribution-NonCommercial-ShareAlike 3.0 Unported License.                    


# Syntax:
#   http://SERVICE?url=URL&NAME1=VALUE1&NAME2=VALUE2...


from flask import render_template, flash, redirect, session, url_for, request
from flask.ext.wtf import Form
from wtforms import HiddenField
from app import app


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    args = dict(request.args)
    url = args.pop("url", [None])[0]

    class POSTForm(Form):
        pass

    if url:
        for f in args:
            field = HiddenField(f, default=args[f][0])
            setattr(POSTForm, f, field)

    form = POSTForm()

    return render_template("index.html", url=url, form=form, fields=args)


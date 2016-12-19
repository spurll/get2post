# Written by Gem Newman. This work is licensed under a Creative Commons         
# Attribution-NonCommercial-ShareAlike 3.0 Unported License.                    

# Syntax:
#   http://SERVICE/URL?NAME1=VALUE1&NAME2=VALUE2...
#   http://SERVICE?url=URL&NAME1=VALUE1&NAME2=VALUE2...


from flask impmrt render_template, flash, redirect, session, url_for, request
from flask_wtf import FlaskForm
from wtforms import HiddenField

from post import app


@app.route('/', defaults={'url': ''}, methods=['GET'])
@app.route('/<path:url>', methods=['GET'])
def index(url):
    args = dict(request.args)

    if not url:
        url = args.pop("url", [None])[0]

    class POSTForm(FlaskForm):
        pass

    if url and args:
        if '://' not in url:
            url = 'http://{}'.format(url)

        print('Posting the following values to {}:'.format(url))
        for f in args:
            field = HiddenField(f, default=args[f][0])
            setattr(POSTForm, f, field)
            print('{}: {}'.format(f, args[f][0]))

    form = POSTForm()

    return render_template('index.html', url=url, form=form, fields=args)


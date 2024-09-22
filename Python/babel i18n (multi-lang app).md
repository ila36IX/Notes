
# Materials

- [Flask-Babel docs](from flask_babel import Babel)
- [Flask-Babel tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)

First You need to have the `babel` module installed:

```sh
pip3 install flask_babel==2.0.0
```

Let's start with a basic `Flask` application:

```python
"""
Starts a Flash Web Application
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_i18n():
    """single page using flask"""
    print(app.config)
    return render_template('0-index.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
```

Inside you application instantiate the ``Babel`` object in your app.

```python
from flask_babel import Babel
babel = Babel(app)
```

In order to configure available languages in our app, create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]` and set default locale language to`"en"` and time zone to `"UTC"`,  just visit the `Flask-Babel` docs to learn more (see link above).

```python
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
```

Use that class as a  [config](https://flask.palletsprojects.com/en/2.3.x/config/) for your Flask app..

```python
app.config.from_object(Config)
```

Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

```python
import request

@babel.localeselector
def get_locale():
    request.accept_languages.best_match(app.config['LANGUAGES'])
```

Use `_` function in your code:

```python
from flask_babel import _

flash(f'not_found_id')
flash(_('User %(username)s not found.', username=username))
```

Create a `babel.cfg` file containing:

```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

Then initialize your translations To extract all the texts to a `.pot` file, this the file that will be used to generate the translation files:

```bash
pybabel extract -F babel.cfg -o messages.pot .
```

Create translations for each supported language (e.g., Spanish: `es`) using the following command:

```sh
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fr
```

Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. for example:

```
...More text above...

#: templates/3-index.html:7 templates/4-index.html:7
msgid "home_title"
msgstr "Welcome to Holberton"

#: templates/3-index.html:11 templates/4-index.html:11
msgid "home_header"
msgstr "Hello world!"
```

Then compile your dictionaries with

```bash
pybabel compile -d translations
```

You might need to reload your application.

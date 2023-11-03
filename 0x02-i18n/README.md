# 0x01-caching
An introductory project on:
- Parametrize Flask templates to display different languages
- Infer the correct locale based on URL parameters, user settings or request headers
- Localize timestamps

## Requirements
- All files should be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- The first line of all files is exactly #!/usr/bin/env python3
- All modules and functions are documented

## File Descriptions
### Mandatory
1. [0-app.py](./0-app.py) && [templates/0-index.html](./templates/0-index.html) - a single `/` route and an `index.html` template that simply outputs `“Welcome to Holberton”` as page title (`<title>`) and `“Hello world”` as header (`<h1>`).

2. [1-app.py](./1-app.py) && [templates/1-index.html](./templates/1-index.html) - creates a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.
   - Uses Config to set Babel’s default locale ("en") and timezone ("UTC").
   - Uses that class as config for the Flask app.

3. [2-app.py](./2-app.py) && [templates/2-index.html](./templates/2-index.html) - a `get_locale` function with the `babel.localeselector` decorator. Uses `request.accept_languages` to determine the best match with our supported languages.

4. [3-app.py](./3-app.py) && [templates/3-index.html](./templates/3-index.html) - Use the _ or gettext function to parametrize the templates.
   - create a [babel.cfg](./babel.cfg)
     ```
     [python: **.py]
     [jinja2: **/templates/**.html]
     ```
   - Using the message IDs home_title and home_header, initialise the transaction with:
      ```
      $ pybabel extract -F babel.cfg -o messages.pot .
      ```
   - and then the two dictionaries with
      ```
      $ pybabel init -i messages.pot -d translations -l en
      $ pybabel init -i messages.pot -d translations -l fr
      ```
   - Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:
     
      | msgid        | English                         | French                                |
      |--------------|---------------------------------|---------------------------------------|
      | home_title   | "Welcome to Holberton"          | "Bienvenue chez    Holberton"          |
      | home_header  | "Hello world!"                  | "Bonjour monde!"                      |


6. [4-app.py](./4-app.py) && [templates/4-index.html](./templates/4-index.html) - implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs.
   - In the `get_locale` function, detect if the incoming request contains `locale` argument and if its value is a supported locale, return it. 
   - If not or if the parameter is not present, resort to the previous default behavior.

   - Now you should be able to test different translations by visiting `http://127.0.0.1:5000?locale=[fr|en]`.
   - Visiting `http://127.0.0.1:5000/?locale=fr` should display this level 1 heading: _Bonjour monde_

7. [6-app.py](./6-app.py) - defines a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if `login_as` was not passed.
   - defines a `before_request` function and use the `app.before_request` decorator to make it be executed before all other functions. `before_request` should use `get_user` to find a user if any, and set it as a global on `flask.g.user`.
   - Use the dictionary to mock a database user table. 
      ```
      users = {
       1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
       2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
       3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
       4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
      }
      ```
   - In the [HTML template] && (./templates/6-index.html), if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

      | msgid           | English                                   | French                                       |
      |-----------------|-------------------------------------------|-----------------------------------------------|
      | logged_in_as    | "You are logged in as %(username)s."     | "Vous êtes connecté en tant que %(username)s." |
      | not_logged_in   | "You are not logged in."                 | "Vous n'êtes pas connecté."                   |
   - Then compile your dictionaries with
      ```
      $ pybabel compile -d translations
      ```
8. [7-app.py](./7-app.py) && [templates/7-index.html](./templates/7-index.html) - Defines a `get_timezone` function and use the `babel.timezoneselector` decorator.
   - The logic should be the same as get_locale:
      - Find `timezone` parameter in URL parameters
      - Find time zone from user settings
      - Default to UTC
   - Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use `pytz.timezone` and catch the `pytz.exceptions.UnknownTimeZoneError` exception.
  
9. [app.py](app.py) && [templates/index.html](./templates/index.html) - Based on the inferred time zone, display the current time on the home page in the default format. For example:
   `Jan 21, 2020, 5:55:39 AM` or `21 janv. 2020 à 05:56:28`
   - Use the following translations:
      | msgid            | English                                     | French                                |
      |------------------|---------------------------------------------|----------------------------------------|
      | current_time_is  | "The current time is %(current_time)s."   | "Nous sommes le %(current_time)s."   |

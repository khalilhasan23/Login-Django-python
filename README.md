# Login-Django-python

# Simple Django Login and Registration

An example of Django project with basic user functionality.

## Screenshots

| Log In | 
| -------|
| <img src="https://github.com/khalilhasan23/Login-Django-python/blob/main/screenshot/1.png" width="500"> | 

| Create an account | 
|-------------------|
|<img src="https://github.com/khalilhasan23/Login-Django-python/blob/main/screenshot/2.png" width="500"> | 


| User Page |
| ----------|
| <img src="https://github.com/khalilhasan23/Login-Django-python/blob/main/screenshot/3.png" width="500"> |

## Functionality

- Log in
    - via username & password
    - via email & password
    - via email or username & password
    - with a remember me checkbox (optional)
- Create an account
- Log out
- Profile activation via email
- Reset password
- Remind a username
- Resend an activation code
- Change password
- Change email
- Change profile
- Multilingual: English, French, Russian, Simplified Chinese and Spanish

If you need dynamic URLs with the language code, check out https://github.com/egorsmkv/simple-django-login-and-register-dynamic-lang

## Installing

### Clone the project

```bash
git clone https://github.com/egorsmkv/simple-django-login-and-register
cd simple-django-login-and-register
```

### Install dependencies & activate virtualenv

```bash
pip install poetry

poetry install
poetry shell
```

### Configure the settings (connection to the database, connection to an SMTP server, and other options)

1. Edit `source/app/conf/development/settings.py` if you want to develop the project.

2. Edit `source/app/conf/production/settings.py` if you want to run the project in production.

### Apply migrations

```bash
python source/manage.py migrate
```

### Collect static files (only on a production server)

```bash
python source/manage.py collectstatic
```

### Running

#### A development server

Just run this command:

```bash
python source/manage.py runserver
```

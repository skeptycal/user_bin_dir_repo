
## [Django Tutorial][1]

>Installing on macOS 10.14.6 Beta (18G48f)

>Darwin Kernel Version 18.7.0: Sun Jun  2 21:24:32 PDT 2019; root:xnu-4903.270.37~8/RELEASE_X86_64


```bash
# verify Python version

$ python --version
Python 3.7.3

$ python -VV
Python 3.7.3 (default, Mar 27 2019, 09:23:15)
[Clang 10.0.1 (clang-1001.0.46.3)]

$ pip -VV
pip 19.1.1 from /Volumes/Data/skeptycal/.virtualenvs/skepport/lib/python3.7/site-packages/pip (python 3.7)

# these are required for first time use

$ pip install virtualenvwrapper
Successfully installed pbr-5.3.0 stevedore-1.30.1 virtualenvwrapper-4.8.4

# (Add to ~/.bashrc)
$ export WORKON_HOME=$HOME/.virtualenvs
$ export PROJECT_HOME=$HOME/Devel
$ source /usr/local/bin/virtualenvwrapper.sh
$ reload
```

```bash

# For each project

$ mkvirtualenv <name>
Using base prefix '/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7'
...

$ pip install django
Successfully installed django-2.2.2 pytz-2019.1 sqlparse-0.3.0
```

project folder is created; subfolder of the same name
```bash
.
├── Pipfile
├── notes.md
└── skepport
    ├── manage.py
    └── skepport
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

`settings.py` For production, change `DEBUG = True` to `DEBUG = False`
***(SECURITY NOTE)*** this file also contains a secret key

`urls.py` maps pages to urls (routing)

`wsgi.py` app communications to server

`manage.py` never ever touch this ...

Use `python manage.py runserver` to start dev server

---

## Create a new app

python manage.py startapp genre







[1]: https://www.youtube.com/watch?v=BLrGJvFp75M&ab_channel=Simplilearn

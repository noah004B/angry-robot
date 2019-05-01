# What is the Angry Robot

This is a waring light that notifies alert.

# Setup (development)

```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -e .
$ export FLASK_ENV=development
$ FLASK_APP=main.py flask run
```

# Setup (production)

## Start uWSGI server

```
$ . venv/bin/activate
$ uwsgi --ini uwsgi.ini
```

## Install and start nginx

```
$ sudo apt-get install nginx
$ vim /etc/nginx/sites-enabled/wusgi.conf
(Input followings)
server {
  listen 8080;
  error_log /var/log/nginx/uwsgi.error warn;

  location / {
    include uwsgi_params;
    uwsgi_pass unix:///home/pi/Projects/angry-robot/uwsgi.sock;
  }
}
$ sudo service nginx start
```


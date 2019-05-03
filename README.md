# What is the Angry Robot

This is a waring light that notifies alert.

# Setup (development)

Install dependencies

```
sudo apt-get install nginx
sudo apt-get install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev
sudo apt-get install libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev
```

Set sound device to analougue(year phone jack)
0: Auto
1: Analogue
2: HDMI

```
$ amixer cset numid=3 1
```

venv and install packages

```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -e .
```

Start dev server

```
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


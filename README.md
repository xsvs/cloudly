Cloudly
=======

Project Cloudly is an award winning "The Easiest To Setup" software to monitor and control your servers in the world!  It's also the ultimate Management Dashboard for your Cloud.
It saves you money and energies by taking away most of the usual servers' monitoring complexities allowing you to focus on control and better use of your infrastructure. 

Cloudly also comes with more than 100+ ready to use services and various products plugins allowing you to monitor what you run off of your servers. 


Installation Instructions
-------------------------

1) Install MySQL server and Python MySQLdb

<pre>
$ apt-get install mysql-server python-mysqldb
</pre>

Optionally configure your MySQL server to meet your specific requirements.

As for the user/password, this one needs to match the entries in the cloudly/cloudly/settings.py file.

2) Create Cloudly Database

<pre>
$ mysql -u root -p
mysql> create database cloudly;
</pre>


3) Install various python packages

<pre>
$ apt-get install python-dev 
$ apt-get install python-simplejson 
$ apt-get install python-django
$ apt-get install python-pip
$ apt-get install python-openssl
</pre>

You'll also need the Python PIL with the JPEG support:

<pre>
$ apt-get install libjpeg-dev
$ pip install pillow
</pre>

4) Install MongoDB and it's python connector

<pre>
$ apt-get install mongodb
$ apt-get install python-pymongo
$ pip install pymongo --upgrade
</pre>

..and configure your server to meet your specific requirements.

5) Download the latest version of Cloudly

<pre>
$ apt-get install git
$ git clone https://github.com/jparicka/cloudly.git cloudly
</pre>

6) Create Cloudly ORM database tables

<pre>
$ cd cloudly
$ python manage.py syncdb
</pre>

If you get an error saying "Access denied for user 'root'@'localhost" then you'd need to edit the cloudly/settings.py and setup the DB section accordingly to your present DB settings.

Assuming this operation succeded, Django will ask you the following:

<pre>
You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no): no
</pre>

Answer "no" to this question.


7) Enable utf-8 characters on the database

<pre>
$ mysql -u root -p
mysql> use cloudly;
mysql> ALTER DATABASE cloudly charset=utf8;
mysql> ALTER TABLE userprofile_profile CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
</pre>

8) Install Amazon Boto - Python Interface to Amazon Web Services

<pre>
$ apt-get install python-boto
</pre>

9) Run MongoDB

<pre>
$ sudo mkdir /data
$ sudo mkdir /data/db
$ mongod
</pre>

..and configure your server to meet your specific requirements.

10) Run the development server

At this point you should be able to run the administration dashboard (Django App):

<pre>
$ echo Never run this as user root!
$ ./run_devel.sh
</pre>

Now that you have the User Interface (Admin Dashboard) up and running you'd need to get the API started.  You can do so by following the instructions in the next step.

11) Configuring the web server (NGINX without SSL support)

TBD...

12) Configuring NGINX (with SSL support)

You'd need to contact me about this one. You can reach me on jparicka@gmail.com, or Skype: jparicka

13) Run the API

API server runs off of Flask therefore you'd need to install Python Flask first.  To do so simply copy and paste the following into your terminal window:

<pre>
$ apt-get install python-flask
</pre>

Once you have the Flask installed, simply run the API like so:

<pre>
$ python api.py
</pre>


14) The Server Monitor Agent

To add a private server to monitor simply copy and paste the following into server's terminal window:

<pre>
curl https://raw.githubusercontent.com/jparicka/cloudly/master/agent.py > ~$USER/agent.py; sudo sh -c "while true; do python ~$USER/agent.py; sleep 3; done"
</pre>

15) ..and that's that!  :)

Enjoy!


Screenshots & Live Demo
-----------------------

![alt screen0](https://raw.githubusercontent.com/jparicka/cloudly/master/static/screenshots/screenshot0.png)

![alt screen1](https://raw.githubusercontent.com/jparicka/cloudly/master/static/screenshots/screenshot1.png)



More to come.  Stay tuned.

TBD...



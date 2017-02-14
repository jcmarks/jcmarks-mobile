# Imports
import os
import jinja2
import webapp2
import logging
import json
import urllib
import MySQLdb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
_INSTANCE_NAME = 'jcmarks-mobile:mobile-data'
_DB_NAME = 'mobile_data'
_USER = 'root'
_PSWD = 'staph-288'

_ACTIVITY = 'plugin_google_activity_recognition'
_LOCATIONS = 'locations'
_EPSILON = 1

from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

if (os.getenv('SERVER_SOFTWARE') and
    os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
    _DB = MySQLdb.connect(unix_socket='/cloudsql/' + _INSTANCE_NAME, db=_DB_NAME, user=_USER, charset='utf8')
else:
    _DB = MySQLdb.connect(host='127.0.0.1', port=3306, db=_DB_NAME, user=_USER, passwd=_PSWD, charset='utf8')

@app.route('/')
def index():
    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    cursor = _DB.cursor()
    cursor.execute('SHOW TABLES')    
    logging.info(cursor.fetchall())

    
    return template.render()

@app.route('/about')
def about():
    template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    return template.render()

@app.route('/quality')
def about():
    template = JINJA_ENVIRONMENT.get_template('templates/quality.html')
    return template.render()
    
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

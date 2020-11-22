from flask import Flask

# __name__ is so that flask knows where to look for templates and static files
app = Flask(__name__)
# protects against modifying cookies, cross site requests, forgery attacks, etc.
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

from hackPHS_2020 import routes
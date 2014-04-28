from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, make_response, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cse190ucsd@localhost/appDB'
db = SQLAlchemy(app)

# Import modules using blueprint handler variable
# (mod_auth)
from markr.mod_auth.controllers import mod_auth as auth_module
from markr.mod_vote.controllers import mod_vote as vote_module

# Register blueprints
app.register_blueprint(auth_module)
app.register_blueprint(vote_module)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)

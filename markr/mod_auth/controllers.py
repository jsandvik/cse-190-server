from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
                  
from markr import db

from markr.mod_auth.models import Student, Faculty

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/login/', methods=['GET', 'POST'])
def login():
    
    # login checks here
    
    return render_template("auth/login.html")
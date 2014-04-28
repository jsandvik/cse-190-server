from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, make_response
                  
from markr import db

from markr.mod_vote.models import Vote

mod_vote = Blueprint('vote', __name__, url_prefix='/vote')

@mod_vote.route('/', methods=['POST'])
def vote():
    
    # Get POST args
    student_vote = request.form.get('vote', None, str)
    pid = request.form.get('pid', None, int)

    # deny requests that don't send arguments
    if not student_vote or not pid:
        return make_response('error', 400)

    # Insert new vote
    vote = Vote(student_vote, pid, 0) 
    db.session.add(vote)
    db.session.commit()

    return make_response('done', 200)
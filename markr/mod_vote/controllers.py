from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, \
                  jsonify, make_response
                  
from markr import db

from markr.mod_vote.models import Vote

mod_vote = Blueprint('vote', __name__, url_prefix='/vote')

@mod_vote.route('/', methods=['GET'])
def index():
    return render_template('vote/vote.html')
    
@mod_vote.route('/cast', methods=['POST'])
def cast():
    data = {'status': 'error'}
    
    
    if 'vote' in request.form and 'pid' in request.form:
        vote = request.form['vote']
        pid = request.form['pid']
    
    if 'vote' in request.json and 'pid' in request.json:
        vote = request.json['vote']
        pid = request.json['pid']
    
    if vote and pid:
        vote = Vote(vote, pid, 0) 
        db.session.add(vote)
        db.session.commit()
    
        data['status'] = 'success'
    
    if request.json:
        return jsonify(**data)
    else:
        return redirect(url_for('vote.index'))
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, \
                  jsonify, make_response, abort
                  
from markr import db
from markr.models import Class, Question, Answer
from markr.mod_auth.models import Student

from markr.mod_vote.models import Vote

mod_vote = Blueprint('vote', __name__, url_prefix='/vote')

@mod_vote.route('/', methods=['GET'])
def index():
    return render_template('vote/vote.html')

@mod_vote.route('/<question_id>', methods=['GET'])
def vote_question(question_id):
    
    return_json = request.args.get('resp') == 'json'
    question = Question.query.get(question_id)
    if not question:
        return abort(404)
        
    answers = Answer.query.filter_by(question=question_id)
    
    if return_json:
        data = {
            'data': [a.serialize for a in answers],
            'is_multi_select': True if (question.answer_type == 'multi_select') else False
        }
        return jsonify(**data)
    
    return render_template('vote/vote.html', answers=answers, question=question)
    
@mod_vote.route('/cast/<question_id>', methods=['POST'])
def cast(question_id):
    data = {'status': 'error'}
    votes = None
    pid = None
    
    return_json = request.args.get('resp')
    
    if request.form and 'vote' in request.form and 'pid' in request.form:
        votes = request.form.getlist('vote')
        pid = request.form.get('pid')
    
    if request.json and 'vote' in request.json and 'pid' in request.json:
        votes = request.json.get('vote')
        pid = request.json.get('pid')
    
    if not votes:
        if return_json:
            return jsonify(**data)
        else:
            flash('Please enter a vote', 'danger')
            return redirect(url_for('vote.vote_question', question_id = question_id))
    
    if not pid or not Student.query.get(pid):
        if return_json:
            return jsonify(**data)
        else:
            flash('Invalid pid', 'danger')
            return redirect(url_for('vote.vote_question', question_id = question_id))
            
 
    question = Question.query.get(question_id)
    if not question:
        if return_json:
            return jsonify(**data)
        else:
            flash('Not a valid question', 'danger')
            return redirect(url_for('vote.vote_question', question_id = question_id, error = errors))
    

    for vote in votes:
        vote = Vote(vote, pid, question_id) 
        db.session.add(vote)
    
    db.session.commit()

    data['status'] = 'success'
    
    if return_json:
        return jsonify(**data)
    else:
        flash('Vote submitted', 'success')
        return redirect(url_for('vote.vote_question', question_id = question_id))
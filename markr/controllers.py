from flask import render_template, request, redirect
from markr.mod_auth.models import Faculty
from . import app

@app.route('/', methods=['GET', 'POST'])
def index():
    """
        Index page for logging in.
    """
    if request.method == 'POST':
        teacher_id = request.form.get('id', "", str)

        teacher = Faculty.query.filter_by(ucsd_id=teacher_id).all()

        if teacher:
            return redirect("admin/classes/{0}".format(teacher_id))


    return render_template("index.html")

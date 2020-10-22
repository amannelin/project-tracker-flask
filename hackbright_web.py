"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html

    #return "{} is the GitHub account for {} {}".format(github, first, last)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/add-student", methods =['GET'])
def add_student():

    return render_template("add_student.html")

@app.route("/student-add", methods=["POST"])
def student_add():
    """Add a student."""

    first_name = request.form('first_name')
    last_name = request.form('last_name')
    github = request.form('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template ("student_added.html")
    # print("student added", github)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")



from flask import Flask, render_template, redirect, request

import data_manager

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    return render_template('list.html')



@app.route('/question/<question_id>')
def display_question(question_id):
    return render_template('question.html', question_id =question_id)

@app.route('/add-question', methods=['GET', 'POST'])
def route_add_question():
    if request.method == 'POST':
        return redirect('/list')
    return render_template('add_question.html')

@app.route("/question/<question_id>/new-answer", methods=["GET", "POST"])
def route_post_answer(question_id):
    if request.method == 'POST':
        return redirect("/list")
    return render_template("post_amswer.html")


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
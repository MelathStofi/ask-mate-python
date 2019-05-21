from flask import Flask, render_template, redirect, request
import data_manager
import connection

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    every_questions = connection.get_all_questions()

    return render_template('list.html', every_questions=every_questions)


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
    return render_template("post_answer.html", question_id=question_id)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
    )
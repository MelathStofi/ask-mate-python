from flask import Flask, render_template, redirect, request, url_for
import data_manager

app = Flask(__name__)


@app.route('/')
def route_list():
    every_question = data_manager.first_five_questions()
    show = 1
    return render_template('list.html', every_question=every_question,show=show)


@app.route('/list')
def route_full_list():
    order_by = request.args.get('order_by')
    order_in = request.args.get('order_in')
    every_question = data_manager.sorting_table(order_by,order_in)
    show = None
    return render_template('list.html', every_question=every_question, show=show)


@app.route('/question/<question_id>', methods=['GET', 'POST'])
def route_display_question(question_id):
    question = data_manager.get_question_by_id(question_id)
    answers = data_manager.get_answers_by_id(question_id)
    # data_manager.count_views(question_id, 1)
    return render_template('question.html',
                           question=question, answers=answers
                           )


@app.route('/add-question', methods=['GET', 'POST'])
def route_add_question():
    if request.method == 'POST':
        question = {'title': request.form['title'],
                    'message': request.form['message'],
                    'image': request.form['image']}
        data_manager.add_question(question)
        return redirect('/list')
    return render_template('add_question.html')
#
#
@app.route("/question/<question_id>/new-answer", methods=["GET", "POST"])
def route_add_answer(question_id):
    if request.method == 'POST':
        answer = {'message': request.form['answer'],
                  'image': request.form['image']}
        data_manager.add_answer(answer, question_id)
        return redirect("/")
    return render_template("add_answer.html",
                            question_id = question_id)


@app.route("/answer/<answer_id>/edit", methods=["GET","POST"])
def edit_answer(answer_id):
    if request.method == "POST":
        answer = {'id': answer_id,
                  'message': request.form['answer'],
                  'image': request.form['image']}
        data_manager.update_answer(answer,answer_id)
        return redirect('/')
    answer_row = data_manager.get_answer_row(answer_id)
    return render_template("update_answer.html",answer_id=answer_id,answer_row=answer_row)


@app.route("/question/<question_id>/vote-up", methods=["GET", "POST"])
@app.route("/question/<question_id>/vote-down", methods=["GET", "POST"])
def route_voting(question_id):
    question = data_manager.get_question_by_id(question_id)
    if 'vote-up' in str(request.url_rule):
        data_manager.voting(question_id, 1)
    elif 'vote-down' in str(request.url_rule):
        data_manager.voting(question_id, -1)
    data_manager.count_views(question_id, -1)
    return redirect(url_for("route_display_question", question_id=question['id']))


@app.route('/edit/<question_id>', methods=['GET','POST'])
def route_update_question(question_id):
    if request.method == 'POST':
        updated_question = {'id': question_id}
        updated_question.update(request.form)
        data_manager.update_story(updated_question,question_id)
        return redirect('/')
    update_question_row = data_manager.get_data_row(question_id)
    return render_template('edit.html', question_id=question_id, update_question_row=update_question_row)


@app.route('/delete_question/<question_id>')
def delete_question(question_id):
    data_manager.delete_question(question_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=3000,
        debug=True
    )

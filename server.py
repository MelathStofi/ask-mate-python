from flask import Flask, render_template, redirect, request

import data_manager

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    return render_template('list.html')


@app.route('/add-question', methods=['GET', 'POST'])
def route_add_question():
    if request.method == 'POST':
        return redirect('/list')
    return render_template('add_question.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
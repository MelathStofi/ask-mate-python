import connection
import time
from operator import itemgetter

timestamp = int(time.time())
questions_data = "sample_data/question.csv"
answers_data = "sample_data/answer.csv"
header = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']


def get_all_questions():
    return connection.get_all_data(questions_data)


def get_question_by_id(_id):
    questions = connection.get_all_data(questions_data)
    for question in questions:
        if question['id'] == _id:
            return question


def get_answers_by_id(_id):
    all_answers = connection.get_all_data(answers_data)
    answers_by_id = []
    for answer in all_answers:
        if answer['question_id'] == _id:
            answers_by_id.append(answer)
    return answers_by_id


def add_question(question):
    all_questions = connection.get_all_data(questions_data)
    question['id'] = len(all_questions) + 1
    question['submission_time'] = timestamp
    all_questions.append(question)
    connection.write_data_to_file(questions_data, all_questions, header)


def add_answer(answer, question_id):
    answer_header = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
    all_answers = connection.get_all_data(answers_data)
    answer['id'] = len(all_answers) + 1
    answer['question_id'] = question_id
    answer['submission_time'] = timestamp
    all_answers.append(answer)
    connection.write_data_to_file(answers_data, all_answers, answer_header)


def count_data_lines(data_file):
    all_data = connection.get_all_data(data_file)
    for i in range(len(all_data)):
        data_lines = i
        return data_lines


def update_story(updated_question):
    questions = get_all_questions()

    for row in range(len(questions)):
        if questions[row]['id'] == updated_question['id']:
            questions[row]['title'] = updated_question['title']
            questions[row]['message'] = updated_question['message']
            questions[row]['image'] = updated_question['image']
    return connection.write_data_to_file('sample_data/question.csv', questions, header)


def get_data_row(row_id):
    questions = get_all_questions()
    for row in range(len(questions)):
        if questions[row]['id'] == row_id:
            return questions[row]


def voting(question_id, vote_act):
    k = 0
    questions = get_all_questions()
    for question in questions:
        if question["id"] == question_id:
            v = question['vote_number']
            try:
                v = int(v)
            except:
                v = 0
            k = int(v)
            if vote_act == 1:
                k += 1
            elif vote_act == -1:
                k -= 1
        question['vote_number'] = str(k)

    return connection.write_data_to_file(questions_data, questions, header)


def count_views(question_id, increment):
    view = 0
    questions = get_all_questions()
    for question in questions:
        if question["id"] == question_id:
            view = question['view_number']
            view = int(view)
            view += increment
            question["view_number"] = str(view)

    return connection.write_data_to_file(questions_data, questions, header)


def sorting_table(order_by=None, order_in=None):
    print(itemgetter(order_by))
    questions = connection.get_all_data(questions_data)
    if order_by is None and order_in is None:
        return questions
    elif order_by == 'title':
        if order_in == "desc":
            sorted_questions = sorted(questions, key=lambda k: k[order_by].lower(), reverse=False)
            return sorted_questions
        elif order_in == "asc":
            sorted_questions = sorted(questions, key=lambda k: k[order_by].lower(), reverse=True)
            return sorted_questions
    elif order_by == 'submission_time' or order_by == 'view_number' or order_by == 'vote_number':
        if order_in == "desc":
            sorted_questions = sorted(questions, key=lambda k: int(k[order_by]), reverse=False)
            return sorted_questions
        elif order_in == "asc":
            sorted_questions = sorted(questions, key=lambda k: int(k[order_by]), reverse=True)
            return sorted_questions

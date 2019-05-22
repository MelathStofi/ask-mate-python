import connection

questions_data = "sample_data/question.csv"
answers_data = "sample_data/answer.csv"


def get_all_questions():
    return connection.get_all_data(questions_data)


def get_question_by_id(_id):
    questions = connection.get_all_data(questions_data)
    for question in questions:
        if question['id'] == _id:
            result = question

    return result


def get_answers_by_id(_id):
    all_answers = connection.get_all_data(answers_data)
    answers_by_id = []
    for answer in all_answers:
        if answer['id'] == _id:
            answers_by_id.append(answer)

    return answers_by_id


def add_question(question):
    header = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
    all_questions = connection.get_all_data(questions_data)
    question['id'] = len(all_questions) + 1
    all_questions.append(question)
    connection.write_question_to_file(all_questions, header)
    print(all_questions)

import connection

questions_data = "sample_data/question.csv"
answers_data = "sample_data/answer.csv"
header = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']


def get_all_questions():
    return connection.get_all_data(questions_data)


def get_question_by_id(_id):
    result = ''
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
    all_questions.append(question)
    connection.write_data_to_file(questions_data, all_questions, header)


def add_answer(answer, question_id):
    header = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
    all_answers = connection.get_all_data(answers_data)
    answer['question_id'] = question_id
    all_answers.append(answer)
    connection.write_data_to_file(answers_data, all_answers, header)


def count_data_lines(data_file):
    all_data = connection.get_all_data(data_file)
    for i in range(len(all_data)):
        data_lines = i
        return data_lines


def update_story(updated_question):
    questions = get_all_questions()

    for row in range(len(questions)):
        if questions[row]['id'] == updated_question['id']:
            questions[row] = updated_question
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
            v = int(question['vote_number'])
            k = int(v)
            if vote_act == 1:
                k += 1
            elif vote_act == -1:
                k -= 1
        question['vote_number'] = k


    return connection.write_data_to_file(questions_data, questions, header)


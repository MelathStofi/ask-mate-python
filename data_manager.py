import connection


def get_question_by_id(id):
    questions = connection.get_all_questions()
    for question in questions:
        if question['id'] == id:
            result = question

    return result


def add_question(question):
    header = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
    all_questions = connection.get_all_questions()
    question['id'] = len(all_questions) + 1
    all_questions.append(question)
    connection.write_question_to_file(all_questions, header)
    print(all_questions)

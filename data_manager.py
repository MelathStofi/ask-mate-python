import connection

def get_question_by_id(id):
    questions = connection.get_all_questions()
    for question in questions:
        if question['id'] == id:
            result = question

    return result


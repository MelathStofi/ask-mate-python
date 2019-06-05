import connection
from operator import itemgetter

questions_data = "sample_data/question.csv"
answers_data = "sample_data/answer.csv"
header = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']


@connection.connection_handler
def get_all_questions(cursor):
    cursor.execute("""
                        SELECT * FROM question;
                        
                       """)
    questions = cursor.fetchall()
    return questions

# @connection.connection_handler
# def get_every_question(cursor):
#     cursor.execute("""
#                         SELECT title FROM question
#                         ORDER BY submission_time DESC ;
#                             """)
#     every_question = cursor.fetchall()
#     return every_question


@connection.connection_handler
def get_question_by_id(cursor,question_id):
    cursor.execute("""
                        SELECT * FROM question
                        where %(question_id)s = id;
                        """,
                   {'question_id':question_id})
    question = cursor.fetchone()
    return question


@connection.connection_handler
def get_answer_by_id(cursor, question_id):
    cursor.execute("""
                        SELECT * FROM answer
                        where %(question_id)s = question_id;
                        """,
                   {'question_id': question_id})
    answer = cursor.fetchall()
    return answer

#     all_answers = connection.get_all_data(answers_data)
#     answers_by_id = []
#     for answer in all_answers:
#         if answer['question_id'] == _id:
#             answers_by_id.append(answer)
#     return answers_by_id
#
#
@connection.connection_handler
def add_question(cursor, question):
    question_title = question['title']
    question_message = question['message']
    question_image = question['image']

    cursor.execute("""
                        INSERT INTO question (submission_time, view_number, vote_number, title, message, image)
                        VALUES (CURRENT_TIMESTAMP, 0, 0, %(question_title)s, %(question_message)s, %(question_image)s)""",
                   {'question_title': question_title,
                    'question_message': question_message,
                    'question_image': question_image})

#     all_questions = connection.get_all_data(questions_data)
#     question['id'] = len(all_questions) + 1
#     question['submission_time'] = timestamp
#     all_questions.append(question)
#     connection.write_data_to_file(questions_data, all_questions, header)
#
#
# def add_answer(answer, question_id):
#     answer_header = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
#     all_answers = connection.get_all_data(answers_data)
#     answer['id'] = len(all_answers) + 1
#     answer['question_id'] = question_id
#     answer['submission_time'] = timestamp
#     all_answers.append(answer)
#     connection.write_data_to_file(answers_data, all_answers, answer_header)
#
#
# def count_data_lines(data_file):
#     all_data = connection.get_all_data(data_file)
#     for i in range(len(all_data)):
#         data_lines = i
#         return data_lines
#
#
# def update_story(updated_question):
#     questions = get_all_questions()
#
#     for row in range(len(questions)):
#         if questions[row]['id'] == updated_question['id']:
#             questions[row]['title'] = updated_question['title']
#             questions[row]['message'] = updated_question['message']
#             questions[row]['image'] = updated_question['image']
#     return connection.write_data_to_file('sample_data/question.csv', questions, header)
#
#
# def get_data_row(row_id):
#     questions = get_all_questions()
#     for row in range(len(questions)):
#         if questions[row]['id'] == row_id:
#             return questions[row]
#
#
# def voting(question_id, vote_act):
#     v = 0
#     questions = get_all_questions()
#     for question in questions:
#         if question["id"] == question_id:
#             v = question['vote_number']
#             try:
#                 v = int(v)
#             except:
#                 pass
#             if vote_act == 1:
#                 v += 1
#             elif vote_act == -1:
#                 if v == 0:
#                     pass
#                 else:
#                     v -= 1
#         question['vote_number'] = str(v)
#
#     return connection.write_data_to_file(questions_data, questions, header)
#
#
# def count_views(question_id, increment):
#     view = 0
#     questions = get_all_questions()
#     for question in questions:
#         if question["id"] == question_id:
#             view = question['view_number']
#             try:
#                 view = int(view)
#             except:
#                 view = 0
#             view += increment
#             question["view_number"] = str(view)
#
#     return connection.write_data_to_file(questions_data, questions, header)
#
#
# def sorting_table(order_by=None, order_in=None):
#     print(itemgetter(order_by))
#     questions = connection.get_all_data(questions_data)
#     if order_by is None and order_in is None:
#         return questions
#     elif order_by == 'title':
#         if order_in == "desc":
#             sorted_questions = sorted(questions, key=lambda k: k[order_by].lower(), reverse=False)
#             return sorted_questions
#         elif order_in == "asc":
#             sorted_questions = sorted(questions, key=lambda k: k[order_by].lower(), reverse=True)
#             return sorted_questions
#     elif order_by == 'submission_time' or order_by == 'view_number' or order_by == 'vote_number':
#         if order_in == "desc":
#             sorted_questions = sorted(questions, key=lambda k: int(k[order_by]), reverse=False)
#             return sorted_questions
#         elif order_in == "asc":
#             sorted_questions = sorted(questions, key=lambda k: int(k[order_by]), reverse=True)
#             return sorted_questions

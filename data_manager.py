import connection
from psycopg2 import sql

from operator import itemgetter


@connection.connection_handler
def first_five_questions(cursor):
    cursor.execute("""
                        SELECT * FROM question
                        ORDER BY submission_time DESC
                        LIMIT 5;
                       """)
    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def get_every_question(cursor):
    cursor.execute("""
                        SELECT * FROM question
                        ORDER BY submission_time DESC;
                        """)
    every_questions = cursor.fetchall()
    return every_questions


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
def get_answers_by_id(cursor, question_id):
    cursor.execute("""
                        SELECT * FROM answer
                        where %(question_id)s = question_id;
                        """,
                   {'question_id': question_id})
    answers = cursor.fetchall()
    return answers


@connection.connection_handler
def get_answer_row(cursor,answer_id):
    cursor.execute("""
                    SELECT * FROM answer
                    WHERE %(answer_id)s = id;
                    """,
                   {'answer_id':answer_id})
    answer_row = cursor.fetchone()
    return answer_row

@connection.connection_handler
def add_question(cursor, question):
    cursor.execute("""
                        INSERT INTO question (submission_time, view_number, vote_number, title, message, image)
                        VALUES (CURRENT_TIMESTAMP, 0, 0, %(question_title)s, %(question_message)s, %(question_image)s)""",
                   {'question_title': question['title'],
                    'question_message': question['message'],
                    'question_image': question['image']})


@connection.connection_handler
def add_answer(cursor, answer, question_id):
    cursor.execute("""
                        INSERT INTO answer (submission_time, vote_number, question_id, message, image)
                        VALUES (CURRENT_TIMESTAMP, 0, %(question_id)s, %(answer_message)s, %(answer_image)s)""",
                   {'question_id': question_id,
                    'answer_message': answer['message'],
                    'answer_image': answer['image']})


@connection.connection_handler
def update_story(cursor,updated_question,question_id):
    cursor.execute(""" 
                        UPDATE question
                        SET title = %(title)s, message = %(message)s, image = %(image)s
                        WHERE %(question_id)s = id;""",
                   {'title':updated_question['title'],'message':updated_question['message'],'image':updated_question['image'],
                    'question_id':question_id})


@connection.connection_handler
def update_answer(cursor,answer,answer_id):
    cursor.execute(""" 
                    UPDATE answer
                    SET message = %(message)s, image = %(image)s
                    WHERE %(answer_id)s = id ;
                    """,
                   {'message':answer['message'],'image':answer['image'],
                    'answer_id':answer_id})


@connection.connection_handler
def get_data_row(cursor,row_id):
    cursor.execute("""
                        SELECT * FROM question
                        WHERE %(row_id)s = id;""",
                   {'row_id':row_id})
    question_row = cursor.fetchone()
    return question_row


@connection.connection_handler
def voting(cursor, question_id, vote_act):
    if vote_act == 1:
        cursor.execute("""
                            UPDATE question 
                            SET vote_number = vote_number + 1 
                            WHERE id = %(question_id)s;""",
                       {'question_id': question_id})
    else:
        cursor.execute("""
                            UPDATE question 
                            SET vote_number = vote_number - 1 
                            WHERE id = %(question_id)s AND vote_number > 0;""",
                       {'question_id': question_id})


@connection.connection_handler
def count_views(cursor, question_id, increment):
    cursor.execute("""
                        UPDATE question
                        SET view_number = view_number + %(increment)s
                        WHERE id = %(question_id)s""",
                   {'increment': increment,
                    'question_id': question_id})
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
@connection.connection_handler
def sorting_table(cursor, order_by, order_in):
    questions = get_every_question()

    if order_by is None and order_in is None:
        return questions
    else:
        if order_in == 'ASC':
            cursor.execute(
            sql.SQL("select * from question ORDER BY {order_by} ASC").
                format(order_by=sql.Identifier(order_by))
            )
            questions = cursor.fetchall()
            return questions
        if order_in == 'DESC':
            cursor.execute(
            sql.SQL("select * from question ORDER BY {order_by} DESC").
                format(order_by=sql.Identifier(order_by))
            )
            questions = cursor.fetchall()
            return questions

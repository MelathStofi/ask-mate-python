import connection
from psycopg2 import sql

from operator import itemgetter


@connection.connection_handler
def get_all_questions(cursor):
    cursor.execute("""
                        SELECT * FROM question;
                        
                       """)
    questions = cursor.fetchall()
    return questions


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
                    WHERE %(question_id)s = id ;
                    """,
                   {'title':updated_question['title'],'message':updated_question['message'],'image':updated_question['image'],
                    'question_id':question_id})

@connection.connection_handler
def get_data_row(cursor,row_id):
    cursor.execute("""
                    SELECT * FROM question
                    WHERE %(row_id)s = id;
                    """,
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

@connection.connection_handler
def sorting_table(cursor, order_by, order_in):
    questions = get_all_questions()

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

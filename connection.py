import csv


def get_all_questions():
    with open('sample_data/question.csv', "r") as file:
        data = list(csv.DictReader(file))

    return data


def write_question_to_file(questions, header):  # questions: name of the list with dictionaries; header: list of headers
    with open("sample_data/question.csv", "w") as file:
        csv_writer = csv.DictWriter(file, fieldnames=header, delimiter=',')
        csv_writer.writeheader()
        csv_writer.writerows(questions)

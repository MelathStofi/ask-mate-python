import csv


def get_all_questions():
    with open('sample_data/question.csv', "r") as file:
        data = list(csv.DictReader(file))

    return data

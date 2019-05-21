import csv


def get_all_questions():
    with open("sample_data/question.csv", "r") as questions:
        csv_reader = csv.DictReader(questions)
        return [row for row in csv_reader]

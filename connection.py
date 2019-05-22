import csv


def get_all_data(file_name):
    with open(file_name, "r") as file:
        data = list(csv.DictReader(file))

    return data


def write_data_to_file(file_name, data, header):  # data: name of list with dictionaries; header: list of headers
    with open(file_name, "w") as file:
        csv_writer = csv.DictWriter(file, fieldnames=header, delimiter=',')
        csv_writer.writeheader()
        csv_writer.writerows(data)

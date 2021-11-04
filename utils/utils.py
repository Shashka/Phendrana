import csv

def export_csv_dict(dict, fields, csv_name):
    with open(csv_name, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for key in dict:
            writer.writerow({fields[0]: key, fields[1]: dict[key]})


def export_csv_string(string, csv_name):
    with open(csv_name, 'w') as file:
        file.write(string)
        file.write('\n')


def export_csv_list(list, csv_name):
    tmplst = []

    for elem in list:
        tostr = elem.decode("utf-8")
        tmplst.append(tostr)

    with open(csv_name, 'w') as file:
        for x in tmplst:
            file.write(x)
            file.write('\n')
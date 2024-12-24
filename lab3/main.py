import pathlib
import csv
def load_table(file):
    table = {}
    test = pathlib.Path(file)
    if not test.is_file():
        raise FileNotFoundError("Файл не найден.")
     with open(file, 'r', newline = '', encoding = 'utf-8') as csvfile: 
    i = csv.DictReader(csvfile)
    for row in i:
        for key in row:
            if key not in table: table[key] = []
                table[key].append(row[key])
    return table

def save_table(table, file):
    test = pathlib.Path(file)
    if not test.is_file():
        raise FileNotFoundError("Файл не найден.")
    with open(file, 'w', newline = '', encoding = 'utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(table)

import pickle

def load_table(file):
    test = pathlib.Path(file)
    if not test.is_file():
        raise FileNotFoundError("Файл не найден.")
    with open(file, 'rb', encoding = 'utf-8') as picfile:
        table = pickle.load(picfile)
    return table

def save_table(table, file):
    test = pathlib.Path(file)
    if not test.is_file():
        raise FileNotFoundError("Файл не найден.")
    with open(file, 'wb', encoding = 'utf-8') as picfile:
        pickle.dump(table, picfile) 


def save_table(table, file):
    test = pathlib.Path(file)
    if not test.is_file():
        raise FileNotFoundError("Файл не найден.")
    with open(file, 'w', encoding = 'utf-8') as txtfile:
        for row in table:
            txtfile.write('\t'.join(row) + '\n')

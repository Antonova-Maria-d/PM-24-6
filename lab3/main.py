import pathlib
from pathlib import Path
import csv
import pickle
def load_table(file):
    test = pathlib.Path(file)
    if not test.is_file():
        raise FileNotFoundError("Файл не найден.")
    file_path = Path(file)
    if file_path.suffix.lower() == '.csv':
        with open(file, 'r', newline = '', encoding = 'utf-8') as csvfile: 
            table = []
            i = csv.reader(csvfile)
            for row in i:
                table.append(row)
        return table
    elif file_path.suffix.lower() == '.pkl':
        with open(file, 'rb', encoding = 'utf-8') as picfile:
        table = pickle.load(picfile)
        return table
    else:
        raise ValueError("Непредвиденное расширение файла.")
    
def save_table(table, file):
    test = pathlib.Path(file)
    if not test.is_file():
        raise FileNotFoundError("Файл не найден.")
    file_path = Path(file)
    if file_path.suffix.lower() == '.csv':
        with open(file, 'w', newline = '', encoding = 'utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(table)
    elif file_path.suffix.lower() == '.pkl':
        with open(file, 'wb', encoding = 'utf-8') as picfile:
            pickle.dump(table, picfile) 
    elif if file_path.suffix.lower() == '.txt':
        with open(file, 'w', encoding = 'utf-8') as txtfile:
            for row in table:
                txtfile.write('\t'.join(row) + '\n')
    else:
        raise ValueError("Непредвиденное расширение файла.")

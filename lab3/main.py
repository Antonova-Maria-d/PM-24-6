import pathlib
from pathlib import Path
import csv
import pickle

def load_table(*files):
    tables = []
    titles = None
    files = list(file)
    for file in files:    
        test = pathlib.Path(file)
        if not test.is_file():
            raise FileNotFoundError("Файл не найден.")
        file_path = Path(file)
        if file_path.suffix.lower() == '.csv':
            with open(file, 'r', newline = '', encoding = 'utf-8') as csvfile: 
                data = csv.reader(csvfile)
                lines = list(data)
                if titles is None:
                    titles = lines[0]
                    lines = lines[1:]
                else:
                    if titles != lines[0]:
                        raise ValueError("Столбцы в файле не совпадают с ожидаемыми")
                lines = lines[1:]
                tables.extend(rows)
    return [titles] + tables
        elif file_path.suffix.lower() == '.pkl':
            with open(file, 'rb', encoding = 'utf-8') as picfile:
                table = pickle.load(picfile)
                if headers is None:
                    headers = table[0]
                    table = table[1:]
                else:
                    if headers != table[0]:
                        raise ValueError("Столбцы в файле не совпадают с ожидаемыми")
                    table = table[1:]
                tables.extend(table)

    return [headers] + tables
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
    elif file_path.suffix.lower() == '.txt':
        with open(file, 'w', encoding = 'utf-8') as txtfile:
            for row in table:
                txtfile.write('\t'.join(row) + '\n')
    else:
        raise ValueError("Непредвиденное расширение файла.")

def get_rows_by_number(start, stop=None, copy_table=False):
    if stop is None:
        stop = start
    else:
        stop += 1
    if copy_table:
        return [row.copy() for row in table[start:stop]]
    else:
        return table[start:stop]

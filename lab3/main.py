import pathlib
from pathlib import Path
import csv
import pickle
import math
from datetime import datetime


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
                rows = list(data)
                if titles is None:
                    titles = rows[0]
                    lines = rows[1:]
                else:
                    if titles != rowa[0]:
                        raise ValueError("Столбцы в файле не совпадают с ожидаемыми")
                rowa = rows[1:]
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
    elif start > stop:
        raise IndexError("Границы заданы некорректно.")
    else:
        stop += 1
    if copy_table:
        return [row.copy() for row in table[start:stop]]
    else:
        return table[start:stop]


def get_rows_by_index(*vals, copy_table = False):
    try:
        new_table = []
        for row in table:
            if any(val in vals for val in row.values()):
                if copy_table:
                    new_table.append(row.copy())
                else:
                    new_table.append(row)
        return new_table
    except Exception as e:
        print("Произошла ошибка при получении данных.")
        
def get_column_types(by_number=True):
    column_types = {}
    for c_num, c_name in enumerate(table[0]):
        if by_number:
            column_type = table[c_num][c_name]
        else:
            column_type = table[0][c_name]
        if column_type == 'int':
            column_types[c_name] = 'int'
        elif column_type == 'float':
            column_types[c_name] = 'float'
        elif column_type == 'bool':
            column_types[c_name] = 'bool'
        elif column_type == 'str':
            column_types[c_name] = 'str'
        else:
            raise ValueError("Непредвиденный вид данных.")
    return column_types

def set_column_types(types_dict, by_number = True):
    if types_dict == {}:
        raise ValueError("Пустой словарь.")
    for c_num, c_name in types_dict.items():
        if by_number:
            table[c_num][c_name] = types_dict[c_num][c_name]
        else:
            table[0][c_name] = types_dict[c_num][c_name]
    return table

def get_values(column = 0):
    values = []
    if isinstance(column, int):
        for row in table:
            value = row[column]
            if isinstance(value, (int, str, float, bool)):
                values.append(value)
    elif isinstance(column, str):
        for row in table:
            if column == row[column]:
                value = row[column]
                if isinstance(value, (int, str, float, bool)):
                    values.append(value)
    else:
        raise ValueError("Тип столбца не int, str, float, bool")
    return values

def get_value(column = 0):
    table = data[1]
    if isinstance(column, int):
        answer = table[column]
    elif isinstance(column, str):
        column = table.index(column)
        answer = table[column]
    return (answer)

def get_value(column = 0):
    value = table[0][column]
    if isinstance(value, (int, str, float, bool)):
        return value
    else:
        raise ValueError("Тип столбца не int, str, float, bool.")


def set_values(values, column = 0):
    if isinstance(column, int):
        for i, row in range(len(values)):
            row[column] = values[i]
    elif isinstance(column, str):
        for i, row in range(len(values)):
            if column == row[column]:
                row[column] = values[i]
    else:
        raise ValueError("введённые данные некорректны.")
    return table

def set_value(value, column = 0):
    if isinstance(column, int):
        table[0][column] = value
    elif isinstance(column, str):
        if column == table[0][column]:
            table[0][column] = value
    else:
        raise ValueError("введённые данные некорректны.")
    return table

def print_table():
    for row in load_table():
        print('\t'.join(row) + '\n')


def concat(table1, table2):
    result_table = []
    for row in table1:
        result_table.append(row)
    for row in table2:
        result_table.append(row)
    return result_table

def split(table, row_number):
    first_part = table[:row_number]
    second_part = table[row_number:]
    return first_part, second_part


def conv_to_num(column):
    try:
        num = [float(x) for x in column]
        return num
    except ValueError:
        print("Ошибка преобразования значений к числам.")
        return None
        
def add(table, col_1, col_2):
    
    if not (0 <= col_1 < len(table[0]) and 0 <= col_2 < len(table[0])):
        raise IndexError("Индексы столбцов выходят за границы таблицы.")
    column_1 = [row[col_1] for row in table]
    column_2 = [row[col_2] for row in table]
    num_1 = conv_to_num(column_1)
    num_2 = conv_to_num(column_2)
    if num_1 is None or num_2 is None:
        raise ValueError("Не удалось преобразовать столбцы к числам.")
    sum = [a + b for a, b in zip(num_1, num_2)]

    return sum

def sub(table, col_1, col_2):
    if not (0 <= col_1 < len(table[0]) and 0 <= col_2 < len(table[0])):
        raise IndexError("Индексы столбцов выходят за границы таблицы.")
    column_1 = [row[col_1] for row in table]
    column_2 = [row[col_2] for row in table]
    num_1 = conv_to_num(column_1)
    num_2 = conv_to_num(column_2)
    if num_1 is None or num_2 is None:
        raise ValueError("Не удалось преобразовать столбцы к числам.")
    dif = [a - b for a, b in zip(num_1, num_2)]

    return dif

def mul(table, col_1, col_2):
    if not (0 <= col_1 < len(table[0]) and 0 <= col_2 < len(table[0])):
        raise IndexError("Индексы столбцов выходят за границы таблицы.")
    column_1 = [row[col_1] for row in table]
    column_2 = [row[col_2] for row in table]
    num_1 = conv_to_num(column_1)
    num_2 = conv_to_num(column_2)
    if num_1 is None or num_2 is None:
        raise ValueError("Не удалось преобразовать столбцы к числам.")
    product = [a * b for a, b in zip(num_1, num_2)]

    return product

def div(table, col_1, col_2):
    if not (0 <= col_1 < len(table[0]) and 0 <= col_2 < len(table[0])):
        raise IndexError("Индексы столбцов выходят за границы таблицы.")
    column_1 = [row[col_1] for row in table]
    column_2 = [row[col_2] for row in table]
    num_1 = conv_to_num(column_1)
    num_2 = conv_to_num(column_2)
    if num_1 is None or num_2 is None:
        raise ValueError("Не удалось преобразовать столбцы к числам.")
    if not all(element != 0 for element in num_2):
        raise ValueError("среди столбца есть число 0,. некорректная операция")
    quo = [a / b for a, b in zip(num_1, num_2)]

    return quo

def column_types(table):
    column_types = {}
    for col in range(len(table[0])):
        current_column = [row[col] for row in table]
        types_count = {
            'int': 0,
            'float': 0,
            'bool': 0,
            'str': 0,
            'datetime': 0
        }
        for value in current_column:
            if isinstance(value, int):
                types_count['int'] += 1
            elif isinstance(value, float):
                types_count['float'] += 1
            elif isinstance(value, bool):
                types_count['bool'] += 1
            elif isinstance(value, str):
                types_count['str'] += 1
            elif isinstance(value, datetime):
                types_count['datetime'] += 1
        most_used_type = max(types_count, key=types_count.get)
        column_types[col] = most_used_type
        
    return column_types

def compare_columns(table, col_1, col_2, operation):
    column_1 = [row[col_1] for row in table]
    column_2 = [row[col_2] for row in table]
    if operation == 'eq':
        result = [a == b for a, b in zip(column_1, column_2)]
    elif operation == 'gr':
        result = [a > b for a, b in zip(column_1, column_2)]
    elif operation == 'ls':
        result = [a < b for a, b in zip(column_1, column_2)]
    elif operation == 'ge':
        result = [a >= b for a, b in zip(column_1, column_2)]
    elif operation == 'le':
        result = [a <= b for a, b in zip(column_1, column_2)]
    elif operation == 'ne':
        result = [a != b for a, b in zip(column_1, column_2)]
    return result
    
def eq(table, col_1, col_2):
    column_1 = [row[col_1] for row in table]
    column_2 = [row[col_2] for row in table]
    result = [a == b for a, b in zip(column_1, column_2)]
    return result

def gr(table, col_1, col_2):
    column_1 = [row[col_1] for row in table]
    column_2 = [row[col_2] for row in table]
    result = [a > b for a, b in zip(column_1, column_2)]
    return result

def ls(table, col_1, col_2):
    column_1 = [row[col_1] for row in table]
    column_2 = [row[col_2] for row in table]
    result = [a < b for a, b in zip(column_1, column_2)]
    return result

def ge(table, col_1, col_2):
    column_1 = [row[col_1] for row in table]
    column_2 = [row[col_2] for row in table]
    result = [a  >= b for a, b in zip(column_1, column_2)]
    return result

def le(table, col_1, col_2):
    column_1 = [row[col_1] for row in table]
    column_2 = [row[col_2] for row in table]
    result = [a  <= b for a, b in zip(column_1, column_2)]
    return result

def ne(table, col_1, col_2):
    column_1 = [row[col_1] for row in table]
    column_2 = [row[col_2] for row in table]
    result = [a  != b for a, b in zip(column_1, column_2)]
    return result
    
def filter_rows(bool_list, table, by_number = False):
    filtered_table = table.copy() if by_number else table
    index = 0
    while index < len(filtered_table):
        if not bool_list[index]:
            del filtered_table[index]
        else:
            index += 1
    return filtered_table

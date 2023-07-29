import pyodbc


def print_hi():
    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=path where you stored the Access file\file name.accdb;')
    cursor = conn.cursor()
    cursor.execute('select * from table name')

    for row in cursor.fetchall():
        print(row)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sqlite3

# типы данных в ячейке
'''
text, blob->любое значение, real->float, integer, null
'''

base = sqlite3.connect("new.db")
# подключается таблица SQL
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS {}data(login, password text)'.format('data'))
# создает таблицу SQL
# IF NOT EXISTS отвечает за проверку на наличие данной таблицы
# text формат ячейки password
# base.execute('CREATE TABLE IF NOT EXISTS {}data(login PRIMARY KEY, password)'.format('data'))
# PRIMARY KEY означает, что в столбце не будет повторяющихся значений, в данном случае в столбце login

base.commit()
# создает таблицу

cur.execute('INSERT INTO data VALUES (?, ?)', ('johny123', '123456789'))
# вставляет в БД значения
base.commit()

x = [['a', '123'], ['b', '783']]
cur.executemany('INSERT INTO data VALUES (?, ?)', x)
base.commit()

info = cur.execute('SELECT * FROM data').fetchall()
# получает все значения из БД в списке кортежей
# * => ALL
# info = cur.execute('SELECT login FROM data').fetchall() все значения ячейки login

getData = cur.execute('SELECT password FROM data WHERE login == ?', 'johny123').fetchone()
# выводит значение ячейки столбца password, который соответсвует login johny123

cur.execute('UPDATE data SET password == ? WHERE login == ?', ('123456789', 'johny123'))
# изменяет ячейку password у johny123

cur.execute('DELETE FROM data WHERE login == ?', ('johny123',))
# удаляет запись про johny
base.commit()
# сохраняет изменения

base.execute('DROP TABLE IF EXISTS data')
base.commit()
# удаляет таблицу

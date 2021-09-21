from database import cursor, db


def add_log(text, user):
    sql = "INSERT INTO logs(text, user) VALUES (%s, %s)"
    cursor.execute(sql, (text, user, ))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))


def add_date(vid, date, user):
    sql = "INSERT INTO work(id, date, user) VALUES (%s, %s, %s)"
    cursor.execute(sql, (vid, date, user, ))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))


# add_log('This log one', 'Brad')
# add_log('This log two', 'Jeff')
# add_log('This log three', 'Jane')
add_date(7, '2021-09-10', 'Daisy')
add_date(8, '2021-09-11', 'Daisy')
add_date(9, '2021-09-12', 'Daisy')


from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:Honda300@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text(
        "insert into subject(\"subject_title\") values (:new_subject_title)"
    )
    connection.execute(sql, {"new_subject_title": ""})

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text(
        "UPDATE subject SET subject_title = :"
        "new_title WHERE subject_title = :old_title"
    )
    connection.execute(sql, {"new_title": "", "old_title": ""})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("delete from subject where subject_title = :new_title")
    connection.execute(sql, {"new_title": "", "old_title": ""})
    transaction.commit()
    connection.close()

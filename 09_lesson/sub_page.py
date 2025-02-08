from sqlalchemy import text


class SubjectPage:
    def __init__(self, connection):
        self.connection = connection
        self.sql_insert = text(
            "INSERT INTO subject (\"subject_title\") VALUES (:new_subject_title)")
        self.sql_select_by_title = text(
            "SELECT * FROM subject WHERE subject_title = :title")
        self.sql_count = text("SELECT COUNT(*) FROM subject")
        self.delete_sql = text("DELETE FROM subject WHERE subject_title = :title")
        self.sql_update = text("UPDATE subject SET subject_title = :new_title WHERE subject_title = :old_title")

    def insert_subject(self, title):
        self.connection.execute(self.sql_insert, {"new_subject_title": title})

    def count_subjects(self):
        return self.connection.execute(self.sql_count).scalar()

    def get_subject(self, title):
        return self.connection.execute(self.sql_select_by_title, {"title": title})

    def delete_subject(self, title):
        self.connection.execute(self.delete_sql, {"title": title})

    def update_subject(self, old_title, new_title):
        self.connection.execute(self.sql_update, {"old_title": old_title, "new_title": new_title})

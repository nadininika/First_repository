import pytest
from sqlalchemy import create_engine
from sub_page import SubjectPage


db_connection_string = "postgresql://postgres:Honda300@localhost:5432/QA"
db = create_engine(db_connection_string)


@pytest.fixture
def db_connection():
    connection = db.connect()
    transaction = connection.begin()
    yield connection, transaction
    transaction.rollback()
    connection.close()


def test_insert(db_connection):
    connection, transaction = db_connection
    subject_page = SubjectPage(connection)

    count_before = subject_page.count_subjects()
    subject_page.insert_subject("Applied Math II")
    count_after = subject_page.count_subjects()

    assert count_after == count_before + 1

    result = subject_page.get_subject("Applied Math II")
    assert result.fetchone() is not None

    subject_page.delete_subject("Applied Math II")
    result = subject_page.get_subject("Applied Math II")
    assert result.fetchone() is None

def test_update(db_connection):
    connection, transaction = db_connection
    subject_page = SubjectPage(connection)

    subject_page.insert_subject("Old Name")
    subject_page.update_subject("Old Name", "New Name")

    result = subject_page.get_subject("Old Name")
    assert result.fetchone() is None

    result = subject_page.get_subject("New Name")
    assert result.fetchone() is not None

    subject_page.delete_subject("New Name")

def test_delete(db_connection):
    connection, transaction = db_connection
    subject_page = SubjectPage(connection)

    subject_page.insert_subject("To Be Deleted")
    assert subject_page.get_subject("To Be Deleted").fetchone() is not None

    subject_page.delete_subject("To Be Deleted")
    assert subject_page.get_subject("To Be Deleted").fetchone() is None



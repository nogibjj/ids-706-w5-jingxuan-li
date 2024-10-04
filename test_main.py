import subprocess
import os

LOG_FILE = "database_operations.log"


def clear_log():
    """Helper function to clear the log file before each test."""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w"):
            pass


def test_create_tables():
    """Test creating students and classes tables."""
    clear_log()
    result = subprocess.run(
        ["python3", "main.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, "Table creation failed!"
    with open(LOG_FILE, "r") as log:
        log_content = log.read()
        assert (
            "Executed create_students command." in log_content
        ), "Students table creation not logged!"
        assert (
            "Executed create_classes command." in log_content
        ), "Classes table creation not logged!"
    print("test_create_tables passed.")


def test_insert_data():
    """Test inserting students and classes."""
    clear_log()
    result = subprocess.run(
        ["python3", "main.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, "Data insertion failed!"
    with open(LOG_FILE, "r") as log:
        log_content = log.read()
        assert (
            "Executed insert_students command." in log_content
        ), "Students insertion not logged!"
        assert (
            "Executed insert_classes command." in log_content
        ), "Classes insertion not logged!"
    print("test_insert_data passed.")


def test_read_students_with_grade():
    """Test reading students with grade 'A'."""
    clear_log()
    result = subprocess.run(
        ["python3", "main.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, "Reading students with grade A failed!"
    assert (
        "Students with grade A:" in result.stdout
    ), "Students with grade A not printed!"
    with open(LOG_FILE, "r") as log:
        log_content = log.read()
        assert (
            "Executed read_students_with_grade command." in log_content
        ), "Read students with grade A not logged!"
    print("test_read_students_with_grade passed.")


def test_update_student_age():
    """Test updating student age for 'Bob'."""
    clear_log()
    result = subprocess.run(
        ["python3", "main.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, "Updating Bob's age failed!"
    with open(LOG_FILE, "r") as log:
        log_content = log.read()
        assert (
            "Executed update_student_age command." in log_content
        ), "Update student age not logged!"
    print("test_update_student_age passed.")


def test_delete_student():
    """Test deleting 'David' from students."""
    clear_log()
    result = subprocess.run(
        ["python3", "main.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, "Deleting David failed!"
    with open(LOG_FILE, "r") as log:
        log_content = log.read()
        assert (
            "Executed delete_students command." in log_content
        ), "Delete student not logged!"
    print("test_delete_student passed.")


def test_join_students_and_classes():
    """Test join query between students and classes."""
    clear_log()
    result = subprocess.run(
        ["python3", "main.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, "Joining students and classes failed!"
    assert (
        "Student names and their classes:" in result.stdout
    ), "Joined data not printed!"
    with open(LOG_FILE, "r") as log:
        log_content = log.read()
        assert (
            "Executed join_students_and_classes command." in log_content
        ), "Join operation not logged!"
    print("test_join_students_and_classes passed.")


if __name__ == "__main__":
    test_create_tables()
    test_insert_data()
    test_read_students_with_grade()
    test_update_student_age()
    test_delete_student()
    test_join_students_and_classes()

    print("All tests passed successfully!")

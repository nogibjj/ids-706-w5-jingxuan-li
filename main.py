import mylib.lib as mylib
import logging
import os

log_file_path = os.path.join(os.getcwd(), "database_operations.log")
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,  # Ensure that previous logging configuration is overwritten
)

# Connect to the database
conn = mylib.connect_to_db("school.db")
cursor = conn.cursor()

# Create tables
mylib.create_students_table(cursor)
logging.info("Executed create_students command.")
mylib.create_classes_table(cursor)
logging.info("Executed create_classes command.")

# Insert data
students_data = [
    (1, "Alice", 20, "A"),
    (2, "Bob", 21, "B"),
    (3, "Charlie", 19, "A"),
    (4, "David", 22, "C"),
]
mylib.insert_students(cursor, students_data)
logging.info("Executed insert_students command.")
classes_data = [
    (1, 1, "Mathematics"),
    (2, 1, "Physics"),
    (3, 2, "Chemistry"),
    (4, 3, "Biology"),
]
mylib.insert_classes(cursor, classes_data)
logging.info("Executed insert_classes command.")

# Read data
students_with_grade_a = mylib.read_students_with_grade(cursor, "A")
print("Students with grade A:")
for student in students_with_grade_a:
    print(student)
logging.info("Executed read_students_with_grade command.")

# Update data
mylib.update_student_age(cursor, "Bob", 1)
logging.info("Executed update_student_age command.")
# Delete data
mylib.delete_student(cursor, "David")
logging.info("Executed delete_students command.")

# Perform a JOIN query
students_classes = mylib.join_students_and_classes(cursor)
print("\nStudent names and their classes:")
for row in students_classes:
    print(row)
logging.info("Executed join_students_and_classes command.")

# Commit changes and close the connection
conn.commit()
conn.close()

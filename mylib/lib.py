import sqlite3
import logging
logging.basicConfig(
    filename='database_operations.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def connect_to_db(db_name):
    """Connect to the SQLite database."""
    conn = sqlite3.connect(db_name)
    logging.info(f"Connected to database '{db_name}' successfully.")
    return conn

def create_students_table(cursor):
    """Create students table."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
    ''')
    logging.info("Students table created successfully.")

def insert_students(cursor, students_data):
    """Insert students into the students table."""
    cursor.executemany('''
        INSERT OR IGNORE INTO students (id, name, age, grade) 
        VALUES (?, ?, ?, ?)
    ''', students_data)
    logging.info(f"Inserted {len(students_data)} students into the table successfully.")

def read_students_with_grade(cursor, grade):
    """Read students with a specific grade."""
    cursor.execute('SELECT * FROM students WHERE grade = ?', (grade,))
    result = cursor.fetchall()
    logging.info(f"Retrieved {len(result)} students with grade '{grade}' successfully.")
    return result

def update_student_age(cursor, name, age_increment):
    """Update the age of a student by name."""
    cursor.execute('''
        UPDATE students 
        SET age = age + ? 
        WHERE name = ?
    ''', (age_increment, name))
    logging.info(f"Updated age for student '{name}' by {age_increment}.")

def delete_student(cursor, name):
    """Delete a student by name."""
    cursor.execute('''
        DELETE FROM students 
        WHERE name = ?
    ''', (name,))
    logging.info(f"Deleted student '{name}' successfully.")

def create_classes_table(cursor):
    """Create classes table."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classes (
            class_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            class_name TEXT,
            FOREIGN KEY (student_id) REFERENCES students (id)
        )
    ''')
    logging.info("Classes table created successfully.")

def insert_classes(cursor, classes_data):
    """Insert classes into the classes table."""
    cursor.executemany('''
        INSERT OR IGNORE INTO classes (class_id, student_id, class_name)
        VALUES (?, ?, ?)
    ''', classes_data)
    logging.info(f"Inserted {len(classes_data)} classes into the table successfully.")

def join_students_and_classes(cursor):
    """Perform a JOIN between students and classes."""
    cursor.execute('''
        SELECT students.name, classes.class_name 
        FROM students
        JOIN classes ON students.id = classes.student_id
    ''')
    result = cursor.fetchall()
    logging.info(f"Joined students & classes, retrieved {len(result)} records.")
    return result

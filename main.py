from pathlib import Path

import psycopg2

def initializeSchema(conn):
    """Create the students table and insert the initial records."""
    #gets the file path
    schema_file_path = Path(__file__).with_name("schemaInitialization.sql")

    try:
        #gets the sql file's query
        initialization_query = schema_file_path.read_text(encoding="utf-8")

        with conn.cursor() as cursor:
            #query
            cursor.execute(initialization_query)

        print("Successfully Initialized Database Schema.\n")

    #catching errors
    except (OSError, psycopg2.Error) as error:
        conn.rollback() #undo failed changes
        print(f"ERROR: Could not initialize database schema: {error}")


def getAllStudents(conn):
    """Retrieve and display all students."""
    try:
        with conn.cursor() as cursor:
            #query
            cursor.execute("SELECT * FROM students;") 

            students = cursor.fetchall()

            #loop through students and print student's fields
            print("Students List:")
            for student in students:
                print(
                    f"ID: {student[0]}, "
                    f"Name: {student[1]} {student[2]}, "
                    f"Email: {student[3]}, "
                    f"Enrollment Date: {student[4]}"
                )
            print("")

    #catching errors
    except psycopg2.Error as error:
        conn.rollback() #undo failed changes
        print(f"ERROR: {error}")


def addStudent(conn, first_name, last_name, email, enrollment_date):
    """Insert a new student record into the students table."""
    try:
        with conn.cursor() as cursor:
            #query
            cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", (first_name, last_name, email, enrollment_date))

        print("Successfully Added Student.\n")

    #catching errors
    except psycopg2.Error as error:
            conn.rollback() #undo failed changes
            print(f"ERROR: {error}")


def updateStudentEmail(conn, student_id, new_email):
    """Update the email address for a student."""
    try:
        with conn.cursor() as cursor:
            #query
            cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))

        print("Successfully Updated Student Email.\n")

    #catching errors
    except psycopg2.Error as error:
        conn.rollback() #undo failed changes
        print(f"ERROR: {error}")


def deleteStudent(conn, student_id):
    """Delete the record of a student with the specified student ID."""
    try:
        with conn.cursor() as cursor:
            #query
            cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))

        print("Successfully Deleted Student.\n")

    #catching errors
    except psycopg2.Error as error:
        conn.rollback() #undo failed changes
        print(f"ERROR: {error}")


if __name__=="__main__":
    #Connect to database (add personal database information)
    conn = None
    try:
        conn=psycopg2.connect(
            dbname="Assignment3Q1_DB",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )

        initializeSchema(conn)
        getAllStudents(conn)
        addStudent(conn, 'Alice', 'Smith', 'alice.smith@email.com', '2023-08-25')
        getAllStudents(conn)
        updateStudentEmail(conn, 1, "john.doe2@example.com")
        getAllStudents(conn)
        deleteStudent(conn, 3)
        getAllStudents(conn)

    #catching errors
    except psycopg2.Error as error:
        print(f"ERROR: {error}")

    #closes connection before end of program
    finally:
        if conn is not None:
            conn.close()
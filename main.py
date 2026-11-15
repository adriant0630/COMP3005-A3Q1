import psycopg2

def getAllStudents(conn):
    """Retrieve and display all students."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM students;")

            students = cursor.fetchall()

            for student in students:
                print(
                    f"ID: {student[0]}, "
                    f"Name: {student[1]} {student[2]}, "
                    f"Email: {student[3]}, "
                    f"Enrollment Date: {student[4]}"
                )
            print("\n")

    except psycopg2.Error as error:
        conn.rollback()
        print(f"ERROR: {error}")

def addStudent(conn, first_name, last_name, email, enrollment_date):
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", (first_name, last_name, email, enrollment_date))

        conn.commit()
        print("Student added successfully.\n")

    except psycopg2.Error as error:
            conn.rollback()
            print(f"ERROR: {error}")

if __name__=="__main__":
    conn = None
    try:
        conn=psycopg2.connect(
            dbname="Assignment3Q1_DB",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )

        getAllStudents(conn)
        addStudent(conn, 'Alice', 'Smith', 'alice.smith@email.com', '2023-08-25')
        getAllStudents(conn)

    except psycopg2.Error as error:
        print(f"ERROR: {error}")

    finally:
        if conn is not None:
            conn.close()
import psycopg2

# Connecting to the PostgreSQL database
conn = psycopg2.connect(
    dbname="A4LukaGrahek", 
    user="postgres", 
    password="098123", #dummy password
    host="localhost", 
    port="5432"
)

# cursor object to execute queries
cursor = conn.cursor()

# Function to retrieve and display all students
def getAllStudents():
    try:
        query = "SELECT * FROM students"
        cursor.execute(query)
        records = cursor.fetchall()
        for row in records:
            print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn is not None:
            conn.rollback()

# Function to add a new student
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, email, enrollment_date))
        conn.commit()
        print("Student added successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn is not None:
            conn.rollback()

# Function to update a student's email
def updateStudentEmail(student_id, new_email):
    try:
        query = "UPDATE students SET email = %s WHERE student_id = %s"
        cursor.execute(query, (new_email, student_id))
        conn.commit()
        print("Student email updated successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn is not None:
            conn.rollback()

# Function to delete a student
def deleteStudent(student_id):
    try:
        query = "DELETE FROM students WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        conn.commit()
        print("Student deleted successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn is not None:
            conn.rollback()


# Main function to interact with the user
def main():
    while(True):
        selection = int(input("Choose number from menu:\n 0 exit\n 1 delete student\n 2 add student\n 3 update stu email\n 4 display students\n"))
        if selection ==0:
            break # Exit the loop
        elif(selection ==1):
            selId = int(input("select the student id to delete: "))
            deleteStudent(selId) # Delete student
        elif(selection ==2):
            stuFName = input("student first Name: ")
            stuLName = input("student last Name: ")
            stuEmail = input("student Email: ")
            enrDate = input("enrollment date: ")
            addStudent(stuFName,stuLName,stuEmail,enrDate) # Add student
        elif(selection == 3):
            stuId = int(input("students ID for whom you want to update their email: "))
            stuEmail = input("updated email: ")
            updateStudentEmail(stuId,stuEmail) # Update student email
        else:
            getAllStudents() # Display all students

main()

# Closing the cursor and connection
cursor.close()
conn.close()
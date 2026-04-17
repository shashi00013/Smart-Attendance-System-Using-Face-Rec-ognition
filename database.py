import sqlite3
import os

DB_PATH = 'attendance.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Students table
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    roll_number TEXT UNIQUE NOT NULL,
                    course TEXT,
                    face_encoding BLOB NOT NULL
                )''')
    # Attendance table
    c.execute('''CREATE TABLE IF NOT EXISTS attendance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    date TEXT NOT NULL,
                    status TEXT DEFAULT 'present',
                    FOREIGN KEY(student_id) REFERENCES students(id),
                    UNIQUE(student_id, date)
                )''')
    conn.commit()
    conn.close()

def add_student(name, roll_number, course, face_encoding):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO students (name, roll_number, course, face_encoding) VALUES (?, ?, ?, ?)",
              (name, roll_number, course, face_encoding))
    conn.commit()
    conn.close()

def get_all_students():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, name, roll_number, course FROM students")
    students = c.fetchall()
    conn.close()
    return students

def get_student_by_id(student_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, name, roll_number, course, face_encoding FROM students WHERE id=?", (student_id,))
    student = c.fetchone()
    conn.close()
    return student

def mark_attendance(student_id, date):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO attendance (student_id, date, status) VALUES (?, ?, 'present')",
                  (student_id, date))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # already marked
    finally:
        conn.close()

def get_attendance_by_date(date):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''SELECT students.name, students.roll_number, attendance.status 
                 FROM attendance JOIN students ON attendance.student_id = students.id
                 WHERE attendance.date = ?''', (date,))
    records = c.fetchall()
    conn.close()
    return records

def get_all_attendance():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''SELECT students.name, students.roll_number, attendance.date, attendance.status 
                 FROM attendance JOIN students ON attendance.student_id = students.id
                 ORDER BY attendance.date DESC''')
    records = c.fetchall()
    conn.close()
    return records

-- Student Performance Predictor
-- Database Schema

CREATE DATABASE IF NOT EXISTS student_performance_db;

USE student_performance_db;


-- 1. Students Table
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_code VARCHAR(20) UNIQUE NOT NULL,
    Gender VARCHAR(1),
    age INT,
    address VARCHAR(10),
    studytime INT,
    failures INT
);


-- 2. Courses Table
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) UNIQUE NOT NULL
);


-- 3. Attendance Table
CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    absences INT,
    UNIQUE (student_id, course_id),

    FOREIGN KEY (student_id)
        REFERENCES students(student_id),

    FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
);


-- 4. Results Table
CREATE TABLE IF NOT EXISTS results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    G1 DECIMAL(5,2),
    G2 DECIMAL(5,2),
    G3 DECIMAL(5,2),
    pass_status TINYINT,
    UNIQUE (student_id, course_id),

    FOREIGN KEY (student_id)
        REFERENCES students(student_id),

    FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
);


-- Insert Mathematics Course
INSERT IGNORE INTO courses (course_name)
VALUES ('Mathematics');


-- Verify Database Tables
SHOW TABLES;

DESCRIBE students;
DESCRIBE courses;
DESCRIBE attendance;
DESCRIBE results;

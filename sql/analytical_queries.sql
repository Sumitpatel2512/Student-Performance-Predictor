
USE student_performance_db;

-- QUERY 1: Average grade by study time
SELECT
    s.studytime,
    COUNT(*) AS total_students,
    ROUND(AVG(r.G3), 2) AS average_grade
FROM students s
JOIN results r ON s.student_id = r.student_id
GROUP BY s.studytime
ORDER BY s.studytime;


-- QUERY 2: Effect of absences on student performance
SELECT
    CASE
        WHEN a.absences = 0 THEN 'No Absences'
        WHEN a.absences BETWEEN 1 AND 5 THEN '1-5 Absences'
        WHEN a.absences BETWEEN 6 AND 10 THEN '6-10 Absences'
        ELSE 'More than 10 Absences'
    END AS absence_group,
    COUNT(*) AS total_students,
    ROUND(AVG(r.G3), 2) AS average_grade
FROM attendance a
JOIN results r ON a.student_id = r.student_id
GROUP BY absence_group;


-- QUERY 3: Performance by previous failures
SELECT
    s.failures,
    COUNT(*) AS total_students,
    ROUND(AVG(r.G3), 2) AS average_grade,
    SUM(r.pass_status = 1) AS passed_students,
    SUM(r.pass_status = 0) AS failed_students
FROM students s
JOIN results r ON s.student_id = r.student_id
GROUP BY s.failures
ORDER BY s.failures;


-- QUERY 4: Pass and fail distribution by gender
SELECT
    CASE
        WHEN s.Gender = 'F' THEN 'Female'
        WHEN s.Gender = 'M' THEN 'Male'
    END AS Gender,
    COUNT(*) AS total_students,
    SUM(r.pass_status = 1) AS passed_students,
    SUM(r.pass_status = 0) AS failed_students,
    ROUND(AVG(r.G3), 2) AS average_grade
FROM students s
JOIN results r ON s.student_id = r.student_id
GROUP BY s.Gender;


-- QUERY 5: Top 10 students by final grade
SELECT
    s.student_code,
    s.studytime,
    s.failures,
    a.absences,
    r.G1,
    r.G2,
    r.G3,
    CASE
        WHEN r.pass_status = 1 THEN 'Pass'
        ELSE 'Fail'
    END AS result
FROM students s
JOIN attendance a ON s.student_id = a.student_id
JOIN results r ON s.student_id = r.student_id
ORDER BY r.G3 DESC
LIMIT 10;

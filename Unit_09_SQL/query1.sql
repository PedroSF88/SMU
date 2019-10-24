--List the following details of each employee:
--employee number, last name, first name, gender, and salary
SELECT 
	e.emp_no,
	e.last_name,
	e.first_name,
	e.gender,
	s.salary
FROM
	employees AS e
Left Join salaries AS s 
	ON e.emp_no=s.emp_no
ORDER BY
	e.last_name ASC
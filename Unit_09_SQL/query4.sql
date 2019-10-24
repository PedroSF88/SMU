--4) List the department of each employee with the following information: 
--employee number, last name, first name, and department name.
SELECT 
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
FROM 
employees e 
join dept_emp de
	on e.emp_no=de.emp_no
join departments d
	on de.dept_no=d.dept_no
ORDER BY
	e.last_name ASC;
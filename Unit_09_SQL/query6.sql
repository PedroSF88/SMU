--List all employees in the Sales department, including their 
--employee number, last name, first name, and department name.

SELECT 
	e.emp_no,
	e.last_name,
	e.first_name,
	de.dept_no,
	d.dept_no,
	d.dept_name,
	de.from_date,
	de.to_date
FROM 
employees e 
join dept_emp de
	on e.emp_no=de.emp_no
join departments d
	on de.dept_no=d.dept_no
	WHERE d.dept_name = 'Sales'
ORDER BY
	e.last_name ASC;
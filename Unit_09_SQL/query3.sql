--3) List the manager of each department with the following information: 
--department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT 
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_no,
	d.dept_name,
	dm.from_date,
	dm.to_date
FROM 
employees e 
join dept_manager dm
	on e.emp_no=dm.emp_no
join departments d
	on dm.dept_no=d.dept_no
ORDER BY
	e.last_name ASC;
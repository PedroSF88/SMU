--8) In descending order, list the frequency count of employee last names, 
--i.e., how many employees share each last name.
SELECT 
	last_name,
	COUNT (emp_no) AS LastNameCount
FROM
	employees
GROUP BY
	last_name
ORDER by
	LastNameCount DESC;
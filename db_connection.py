import sqlite3

connect_db = sqlite3.connect("minimalist_streamlit.db")
c = connect_db.cursor()


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS tasks(task_title TEXT(20), task_description TEXT, task_status TEXT, task_deadline DATE)')


def add_task(task_title, task_description, task_status, task_deadline):
	c.execute('INSERT INTO tasks(task_title, task_description, task_status, task_deadline) VALUES (?, ?, ?, ?)', (task_title, task_description, task_status, task_deadline))

	connect_db.commit()


def view_task():
	c.execute('SELECT * FROM tasks')
	task_data = c.fetchall()

	return task_data


def get_distinct_task():
	c.execute('SELECT DISTINCT task_title FROM tasks')
	task_data = c.fetchall()

	return task_data


def get_task(task_title):
	c.execute('SELECT * FROM tasks WHERE task_title="{}"'.format(task_title))
	task_data = c.fetchall()

	return task_data


def update_task(old_task_title, task_title, task_description, task_status, task_deadline):
	c.execute('UPDATE tasks SET task_title="{}", task_description="{}", task_status="{}", task_deadline="{}" WHERE task_title="{}"'.format(task_title, task_description, task_status, task_deadline, old_task_title))

	connect_db.commit()

	task_data = c.fetchall()
	return task_data
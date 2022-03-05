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
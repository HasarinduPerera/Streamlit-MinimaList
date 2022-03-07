import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import create_table, add_task, view_task, get_distinct_task, get_task, update_task, delete_task

 
def main():
	st.title("MinimaList")

	create_table()

	menu = ["Add Tasks", "See Tasks", "Update Tasks", "Delete Tasks"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice == "Add Tasks":
		st.subheader("Add Tasks")

		task_title = st.text_input("Task To Do")
		task_description = st.text_area("Describe")
		task_status = st.selectbox("Status", ["To Do", "In Progress", "Review", "Done"])
		task_deadline = st.date_input("Due On")

		if st.button("Add Task"):
			add_task(task_title, task_description, task_status, task_deadline)
			st.success("Task Successfully Added!")
			
	elif choice == "See Tasks":
		st.subheader("See Tasks")

		df = pd.DataFrame(view_task(), columns = ['Task Title', 'Description', 'Status', 'Deadline'])
		
		if len(df.index) > 1:
			st.info("You have {} tasks listed!".format(len(df.index)))
		else:
			st.info("You have {} task listed!".format(len(df.index)))

		with st.expander("Tasks List"):
			st.dataframe(df)

		status_count = df['Status'].value_counts().to_frame()
		status_count = status_count.reset_index()

		plot_status = px.pie(status_count, names='index', values='Status')
		st.plotly_chart(plot_status)

	elif choice == "Update Tasks":
		st.subheader("Update Tasks")

		list_of_tasks = [i[0] for i in get_distinct_task()]
		selected_task = st.selectbox("Select Task To Update", list_of_tasks)
		task_info_out = get_task(selected_task)

		if selected_task:

			old_task_title = task_info_out[0][0]
			task_title = st.text_input("Update Task Title", task_info_out[0][0])
			task_description = st.text_area("Update Description", task_info_out[0][1])
			task_status = st.selectbox("Change Status (Current Status: {})".format(task_info_out[0][2]), ["To Do", "In Progress", "Review", "Done"])
			task_deadline = st.date_input("Due on: {}".format(task_info_out[0][3]))

			if st.button("Update Task"):
				update_task(old_task_title, task_title, task_description, task_status, task_deadline)
				st.success("Task Successfully Updated!")

	elif choice == "Delete Tasks":
		st.subheader("Delete Tasks")

		list_of_tasks = [i[0] for i in get_distinct_task()]
		selected_task = st.selectbox("Select Task To Delete", list_of_tasks)
		task_info_out = get_task(selected_task)

		if selected_task:

			task_title = st.text("Task Title: {}".format(task_info_out[0][0]))
			task_description = st.text("Task Description: {}".format(task_info_out[0][1]))
			task_status = st.text("Task Status: {}".format(task_info_out[0][2]))
			task_deadline = st.text("Task Due Date: {}".format(task_info_out[0][3]))

			task_title = task_info_out[0][0]

			if st.button("Delete Task"):
					delete_task(task_title)
					st.success("Task Successfully Deleted!")


if __name__ == '__main__':
	main()

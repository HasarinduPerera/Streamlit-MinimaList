import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import create_table, add_task, view_task


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

		st.dataframe(df)

		status_count = df['Status'].value_counts().to_frame()
		status_count = status_count.reset_index()

		plot_status = px.pie(status_count, names='index', values='Status')
		st.plotly_chart(plot_status)

	elif choice == "Update Tasks":
		st.subheader("Update Tasks")

	elif choice == "Delete Tasks":
		st.subheader("Delete Tasks")


if __name__ == '__main__':
	main()

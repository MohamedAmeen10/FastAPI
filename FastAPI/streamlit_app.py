import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
BASE_URL = os.getenv('BACKEND_URL', 'http://127.0.0.1:8000')

st.title("Student Management System")

operation = st.sidebar.selectbox(
    "Choose an operation",
    ["Create Student", "Get Student by ID", "Get Student by Name", "Update Student", "Delete Student", "Get All Students"]
)

def make_request(method, url, **kwargs):
    try:
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        st.error(f"Request failed: {e}")
        return None

# Create a student
if operation == "Create Student":
    st.header("Create a New Student")
    stud_id = st.number_input("Student ID", min_value=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    
    if st.button("Create"):
        response = make_request("POST", f"{BASE_URL}/createstudent/{stud_id}", json={"name": name, "age": age})
        if response:
            if response.status_code == 200:
                st.success(f"Student {name} created successfully!")
            else:
                st.error(f"Error: {response.json().get('detail', 'Unknown error')}")

# Add similar handling for other operations...

# Example for getting all students
if operation == "Get All Students":
    st.header("All Students")
    
    if st.button("Get"):
        response = make_request("GET", f"{BASE_URL}/students/")
        if response:
            if response.status_code == 200:
                students = response.json()
                st.write(students)
            else:
                st.error(f"Error: {response.json().get('detail', 'Unknown error')}")

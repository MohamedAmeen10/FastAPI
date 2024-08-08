import streamlit as st
import requests

# Directly use the public deployment URL
BASE_URL = 'https://fastapi-hzcycy9nnfbqb6eeetzzqc.streamlit.app/'

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

# Get a student by ID
if operation == "Get Student by ID":
    st.header("Get Student by ID")
    stud_id = st.number_input("Student ID", min_value=1)
    
    if st.button("Get"):
        response = make_request("GET", f"{BASE_URL}/studentid/{stud_id}")
        if response:
            if response.status_code == 200:
                student = response.json()
                st.write(student)
            else:
                st.error(f"Error: {response.json().get('detail', 'Unknown error')}")

# Get a student by name
if operation == "Get Student by Name":
    st.header("Get Student by Name")
    name = st.text_input("Name")
    
    if st.button("Get"):
        response = make_request("GET", f"{BASE_URL}/getbyname", params={"name": name})
        if response:
            if response.status_code == 200:
                student = response.json()
                if "data" not in student:
                    st.write(student)
                else:
                    st.error("Student not found")
            else:
                st.error(f"Error: {response.json().get('detail', 'Unknown error')}")

# Update a student
if operation == "Update Student":
    st.header("Update Student")
    stud_id = st.number_in

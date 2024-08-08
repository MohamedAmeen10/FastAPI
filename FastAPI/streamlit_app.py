import streamlit as st
import requests

# Backend URL
BASE_URL = 'https://fastapi-hzcycy9nnfbqb6eeetzzqc.streamlit.app/'  # Replace with your actual FastAPI URL

st.title("Student Management System")

# Helper function to make API requests and handle errors
def make_request(method, url, **kwargs):
    try:
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()  # Raises HTTPError for bad responses
        
        # Check if the response is in JSON format
        if 'application/json' in response.headers.get('Content-Type', ''):
            return response.json()
        else:
            st.error(f"Expected JSON response, but got: {response.headers.get('Content-Type')}")
            st.write("Raw response content:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
        return None

# Select an operation
operation = st.sidebar.selectbox(
    "Choose an operation",
    ["Create Student", "Get Student by ID", "Update Student", "Delete Student"]
)

# Create a student
if operation == "Create Student":
    st.header("Create a New Student")
    stud_id = st.number_input("Student ID", min_value=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    
    if st.button("Create"):
        response = make_request("POST", f"{BASE_URL}/student/{stud_id}", json={"name": name, "age": age})
        if response:
            st.success(f"Student {name} created successfully!")

# Get a student by ID
if operation == "Get Student by ID":
    st.header("Get Student by ID")
    stud_id = st.number_input("Student ID", min_value=1)
    
    if st.button("Get"):
        response = make_request("GET", f"{BASE_URL}/student/{stud_id}")
        if response:
            st.write(f"Name: {response['name']}")
            st.write(f"Age: {response['age']}")

# Update a student
if operation == "Update Student":
    st.header("Update Student")
    stud_id = st.number_input("Student ID", min_value=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    
    if st.button("Update"):
        response = make_request("PUT", f"{BASE_URL}/student/{stud_id}", json={"name": name, "age": age})
        if response:
            st.success(f"Student {stud_id} updated successfully!")

# Delete a student
if operation == "Delete Student":
    st.header("Delete Student")
    stud_id = st.number_input("Student ID", min_value=1)
    
    if st.button("Delete"):
        response = make_request("DELETE", f"{BASE_URL}/student/{stud_id}")
        if response:
            st.success(f"Student {stud_id} deleted successfully!")

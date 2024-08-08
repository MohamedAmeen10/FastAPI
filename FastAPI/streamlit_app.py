import streamlit as st
import requests

# Backend URL
BASE_URL = "https://fastapi-hzcycy9nnfbqb6eeetzzqc.streamlit.app/"

st.title("Student Database")

# Select an operation
operation = st.sidebar.selectbox(
    "Choose an operation",
    ["Create Student", "Get Student by ID", "Get Student by Name", "Update Student", "Delete Student", "Get All Students"]
)

# Create a student
if operation == "Create Student":
    st.header("Create a New Student")
    stud_id = st.number_input("Student ID", min_value=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    
    if st.button("Create"):
        response = requests.post(f"{BASE_URL}/createstudent/{stud_id}", json={"name": name, "age": age})
        if response.status_code == 200:
            st.success(f"Student {name} created successfully!")
        else:
            st.error(f"Error: {response.json()['detail']}")

# Get a student by ID
if operation == "Get Student by ID":
    st.header("Get Student by ID")
    stud_id = st.number_input("Student ID", min_value=1)
    
    if st.button("Get"):
        try:
            response = requests.get(f"{BASE_URL}/student/{stud_id}")
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)
            
            # Attempt to parse the response as JSON
            student = response.json()
            st.write(student)
            
        except requests.exceptions.HTTPError as http_err:
            st.error(f"HTTP error occurred: {http_err}")
            try:
                # Show error details if available in the response
                error_detail = response.json().get('detail', 'No additional error details provided')
                st.error(f"Error: {error_detail}")
            except requests.exceptions.JSONDecodeError:
                st.error("Failed to parse the error response as JSON.")
                st.write("Raw response content:", response.text)
        
        except requests.exceptions.RequestException as req_err:
            st.error(f"Request error occurred: {req_err}")


# Get a student by name
if operation == "Get Student by Name":
    st.header("Get Student by Name")
    name = st.text_input("Name")
    
    if st.button("Get"):
        try:
            response = requests.get(f"{BASE_URL}/getbyname", params={"name": name})
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)
            
            # Attempt to parse the response as JSON
            student = response.json()
            if "data" not in student:
                st.write(student)
            else:
                st.error("Student not found")
                
        except requests.exceptions.HTTPError as http_err:
            st.error(f"HTTP error occurred: {http_err}")
            try:
                # Show error details if available in the response
                error_detail = response.json().get('detail', 'No additional error details provided')
                st.error(f"Error: {error_detail}")
            except requests.exceptions.JSONDecodeError:
                st.error("Failed to parse the error response as JSON.")
                st.write("Raw response content:", response.text)
        
        except requests.exceptions.RequestException as req_err:
            st.error(f"Request error occurred: {req_err}")


# Update a student
if operation == "Update Student":
    st.header("Update Student")
    stud_id = st.number_input("Student ID", min_value=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    
    if st.button("Update"):
        response = requests.put(f"{BASE_URL}/updatestudent/{stud_id}", json={"name": name, "age": age})
        if response.status_code == 200:
            st.success(f"Student {stud_id} updated successfully!")
        else:
            st.error(f"Error: {response.json()['detail']}")

# Delete a student
if operation == "Delete Student":
    st.header("Delete Student")
    stud_id = st.number_input("Student ID", min_value=1)
    
    if st.button("Delete"):
        response = requests.delete(f"{BASE_URL}/deletestudent/{stud_id}")
        if response.status_code == 200:
            st.success(f"Student {stud_id} deleted successfully!")
        else:
            st.error(f"Error: {response.json()['detail']}")

# Get all students
if operation == "Get All Students":
    st.header("All Students")
    
    if st.button("Get"):
        response = requests.get(f"{BASE_URL}/students/")
        if response.status_code == 200:
            students = response.json()
            st.write(students)
        else:
            st.error(f"Error: {response.json()['detail']}")

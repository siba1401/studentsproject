import streamlit as st
import pandas as pd
import numpy as np

def process_data(dfs):
    # Skip the first 11 rows and reset index
    student_number_row = dfs[dfs.iloc[:, 0] == 'Student Number'].index[0]
    df = dfs.iloc[student_number_row:]
    df.columns = df.iloc[0]
    df = df.iloc[1:].reset_index(drop=True)  # Remove the first row after assigning headers

    # Ensure "Percentage" is numeric
    df["Percentage"] = pd.to_numeric(df["Percentage"], errors="coerce")

    # Extract relevant data
    df1 = df["Result"]
    df2 = df[df["Result"] == "PASS"]

    # Calculate statistics
    Average_percentage = df2["Percentage"].mean()
    Total_students_pass = len(df2)
    Total_Number_of_students = len(df1)

    return Average_percentage, Total_Number_of_students, Total_students_pass

def main():
    st.title("Student Performance Analysis")

    # File uploader for Excel file

    uploaded_file1 = st.file_uploader("Upload Excel file", type=["xlsx"], key='df1')
    uploaded_file2 = st.file_uploader("Upload Excel file", type=["xlsx"], key='df2')
    if uploaded_file1 is not None and uploaded_file2 is not None:
        # Read the uploaded Excel file

        df1 = pd.read_excel(uploaded_file1)
        df2 = pd.read_excel(uploaded_file2)
        # Process data and get statistics
        avg_percentage1, total_students1, total_passed1 = process_data(df1)
        avg_percentage2, total_students2, total_passed2 = process_data(df2)

        # Display results
        st.subheader("Results:")
        st.write(f"**Average Percentage Marks for Even Sem:** {avg_percentage1:.2f}")
        st.write(f"**Total Number of Students for Even Sem:** {total_students1}")
        st.write(f"**Total Number of Students Passed for Even Sem:** {total_passed1}")

        st.subheader("Results:")
        st.write(f"**Average Percentage Marks for Odd Sem:** {avg_percentage2:.2f}")
        st.write(f"**Total Number of Students for Odd Sem:** {total_students2}")
        st.write(f"**Total Number of Students Passed for Odd Sem:** {total_passed2}")

        st.subheader('Year Aggregated Mean')
        aggregated_mean = (avg_percentage1*total_passed1 + avg_percentage2*total_passed2)/ (total_passed1+total_passed2)
        st.write(f"**Aggregated Year Mean :** {aggregated_mean:.2f}")

if __name__ == "__main__":
    main()
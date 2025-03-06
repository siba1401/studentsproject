import streamlit as st
import pandas as pd
import numpy as np

def process_data(dfs):
    # Skip the first 11 rows and reset index
    df = dfs.iloc[11:, :].reset_index(drop=True)

    # Assign column names correctly
    df.columns = df.iloc[0]  # First row becomes column headers
    df = df[1:].reset_index(drop=True)  # Remove the first row after assigning headers

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
    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

    if uploaded_file is not None:
        # Read the uploaded Excel file
        dfs = pd.read_excel(uploaded_file)

        # Process data and get statistics
        avg_percentage, total_students, total_passed = process_data(dfs)

        # Display results
        st.subheader("Results:")
        st.write(f"**Average Percentage Marks:** {avg_percentage:.2f}")
        st.write(f"**Total Number of Students:** {total_students}")
        st.write(f"**Total Number of Students Passed:** {total_passed}")

if __name__ == "__main__":
    main()
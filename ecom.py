import streamlit as st
import pandas as pd
import numpy as np
def main():
    st.title("This is a app for ecom i am creating")
    st.sidebar.title("You can upload your file here")
    upload_file = st.sidebar.file_uploader("upload your file", type=['csv', 'xlsx'])
    
    data = None  # Initialize data variable
    
    if upload_file is not None:
        try:
            if upload_file.name.endswith('.csv'):
                data = pd.read_csv(upload_file)
            else:
                data = pd.read_excel(upload_file)
            st.sidebar.success("file uploaded successfully")
            st.subheader("Showing you a Data Analysis")
            st.dataframe(data.head())
        except Exception as e:
            st.error(f"Error loading file: {e}")
    
    # Only proceed if data is loaded
    if data is not None:
        st.subheader("Let's see some more details in data")
        st.write("shape of the data", data.shape)
        st.write("columns name in the data", data.columns)
        st.write("Checking missing values in data", data.isnull().sum())
        st.subheader("Analysing descriptive summary of the data")
        st.write(data.describe())
    else:
        st.info("Please upload a file to see data details.")
if __name__ == "__main__":
    main()

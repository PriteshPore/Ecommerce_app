import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

def main():
   st.title("This is a app for ecom i am creating")
   st.sidebar.title("You can upload your file here")
   upload_file = st.sidebar.file_uploader("upload your file",type=['csv','xlsx'])
   
   if upload_file is not None:
    try:
        if upload_file.name.endswith('.csv'):
            data = pd.read_csv(upload_file)
        else:
           data = pd.read_excel(upload_file)
        st.sidebar.success("file uploaded sucessfully")
        st.subheader("Showing you a Data Analysis")
        st.dataframe(data.head())
    except Exception as e:
       print(e)
    st.subheader("Let's see some more details in data")
    st.write("shape of the data",data.shape)
    st.write("columns name in the data",data.columns)
    st.write("Checking missing values in data",data.isnull().sum())
    
    st.subheader("Analysing descriptive summary of the data")
    st.write(data.describe())


if __name__ == "__main__":
   main()


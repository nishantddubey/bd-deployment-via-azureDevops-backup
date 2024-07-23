import streamlit as st
import pandas as pd
from datetime import datetime
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from io import StringIO

# Azure Blob Storage connection details
connection_string = ""
container_name = "testbd"
blob_name = "Complaints_data_1000.csv"

def get_blob_data(connection_string, container_name, blob_name):
    # Initialize the BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # Get the BlobClient
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    
    # Download the blob content as a string
    blob_data = blob_client.download_blob().readall()
    return blob_data

def main_app():
    # Get data from Azure Blob Storage
    blob_data = get_blob_data(connection_string, container_name, blob_name)
    df = pd.read_csv(StringIO(blob_data.decode('utf-8')))
    
    # Streamlit app
    st.title("AI-Assisted Case Classification")
    st.markdown('</div>', unsafe_allow_html=True)

    # Filters section
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        case_no = st.multiselect("Case No.", options=df['Case: Case Number'].unique(), key="case_no")
    with col2:
        time = st.time_input("Time", datetime.strptime("20:00", "%H:%M").time(), key="time")
    with col3:
        recent_model_run_date = st.date_input("Recent Model Run Date", datetime(2022, 12, 5), key="recent_model_run_date")
    with col4:
        business_unit = st.multiselect("Business Unit (BU)", options=df['Business'].unique(), key="business_unit")
    with col5:
        ai_tag_status = st.multiselect("AI Tag Status", options=df['Tag'].unique(), key="ai_tag_status")

    # Filter the DataFrame based on the selections
    if st.button("Search"):
        filtered_df = df.copy()
        
        if case_no:
            filtered_df = filtered_df[filtered_df['Case: Case Number'].isin(case_no)]
        if business_unit:
            filtered_df = filtered_df[filtered_df['Business'].isin(business_unit)]
        if ai_tag_status:
            filtered_df = filtered_df[filtered_df['Tag'].isin(ai_tag_status)]
    else:
        # Show full DataFrame if Search button is not clicked
        filtered_df = df

    st.markdown('</div>', unsafe_allow_html=True)

    # Case & Classification Overview section
    st.header("Case & Classification Overview")
    st.write("A descriptive body text comes here")

    # Display the table
    st.dataframe(filtered_df)

    # Option to download the table
    st.download_button(label="Download Table", data=filtered_df.to_csv(index=False), file_name="filtered_cases.csv")

if __name__ == "__main__":
    main_app()

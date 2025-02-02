import streamlit as st
import pandas as pd

if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=["client_name", "amcfms", "type", "note", "total_amount", "s_date", "e_date", "billing"])

st.header("Form AMC")

client_name = st.text_input("Client Name")

amcfms_col, type_col = st.columns(2)
selected_amcfms = amcfms_col.selectbox("AMC/FMS", options=["AMC", "FMS", "AMC+FMS", "SFMS", "WIFI AMC"])
selected_type = type_col.selectbox("Type", options=["Comprehensive", "Non-Comprehensive", "Comprehensive+Non_Comprehensive", "AMC", "FMS", "Renewal"])

note = st.text_area("Extra Specification")
total_amount = st.text_input("Total Amount")

s_date_col, e_date_col = st.columns(2)
start_date = s_date_col.date_input("Start Date")
end_date = e_date_col.date_input("End Date")

billing_col, upload_col = st.columns(2)
billing = billing_col.selectbox("Billing", options=["Yearly", "Half Yearly", "Quarterly", "Monthly"])

uploaded_file = upload_col.file_uploader("Upload File")

if st.button("Save"):
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    new_entry = pd.DataFrame({
        "client_name": [client_name],
        "amcfms": [selected_amcfms],
        "type": [selected_type],
        "note": [note],
        "total_amount": [total_amount],
        "s_date": [start_date_str],
        "e_date": [end_date_str],
        "billing": [billing]
    })

    st.session_state['data'] = pd.concat([st.session_state['data'], new_entry], ignore_index=True)
    st.success("Data saved!")

if not st.session_state['data'].empty:
    st.write("### Saved Data")
    st.dataframe(st.session_state['data'])

def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

if not st.session_state['data'].empty:
    csv = convert_df(st.session_state['data'])
    st.download_button(
        label="Press to Download",
        data=csv,
        file_name='saved_data.csv',
        mime='text/csv'
    )

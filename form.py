import streamlit as st 
import pandas as pd 


if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=["client_name", "amcfms", "type", "note", "total_amount", "s_date", "e_date", "billing"])
    
st.header("Save AMC")
client_name = st.text_input("Client Name")

amcfms,type = st.columns(2)
amcfms.selectbox("AMC/FMS",options=["AMC","FMS","AMC+FMS","SFMS","WIFI AMC"])
type.selectbox("Type",options=["Comprehensive","Non-Comprehensive","Comprehensive+Non_Comprehensive","AMC","FMS","Renewal"])

note = st.text_area("Extra Specification")
total_amount =st.text_input("Total Amount")

s_date,e_date = st.columns(2)
s_date.date_input("Start Date")
e_date.date_input("End Date")

billing = st.selectbox("Billing", options=["Yearly", "Half Yearly", "Quarterly", "Monthly"])

if st.button("Save"):
    new_entry = pd.DataFrame({
        "client_name": [client_name],
        "amcfms": [amcfms],
        "type": [type],
        "note": [note],
        "total_amount": [total_amount],
        "s_date": [s_date],
        "e_date": [e_date],
        "billing": [billing]
    })
    
    st.session_state['data'] = pd.concat([st.session_state['data'], new_entry], ignore_index=True)
    st.success("Data saved!")

# Display the table if there is any data
if not st.session_state['data'].empty:
    st.write("### Saved Data")
    st.dataframe(st.session_state['data'])

# Button to download the data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(st.session_state['data'])

st.download_button(
    label="Press to Download",
    data=csv,
    file_name='saved_data.csv',
    mime='text/csv',
)



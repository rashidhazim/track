import streamlit as st
import pandas as pd
import snowflake.connector

st.title('Snowflake Data Viewer')

# Define connection parameters
CONN_PARAMS = {
    "user": "Hazim.Rashid@mckesson.com",
    "account": "mckesson.east-us-2.azure",
    "authenticator": "EXTERNALBROWSER",
    "role": "Sbx_ea_general_fr",
    "warehouse": "Sbx_ea_general_fr_wh",
    "database": "SBX_PSAS_DB",
    "schema": "ANALYTICS",
}

# Create a Snowflake connection
conn = snowflake.connector.connect(**CONN_PARAMS)

# Execute a query
query = "SELECT * FROM CURRENT_DISCREPANCIES"
df = pd.read_sql(query, conn)

# Display the results in a table
st.dataframe(df)

# Close the connection
conn.close()

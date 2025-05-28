
import streamlit as st
import pandas as pd
import sqlite3
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="Test")  # Replace with your actual OpenAI API key

# Connect to SQLite database
conn = sqlite3.connect("logistics.db")
df = pd.read_sql_query("SELECT * FROM deliveries", conn)

# --- Page Styling ---
st.set_page_config(page_title="Logistics AI Assistant", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
        body {
            background-color: #0f1117;
            color: #e0e0e0;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextInput > div > div > input {
            background-color: #1c1f26;
            border: 1px solid #444;
            padding: 10px;
            color: white;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            padding: 8px 20px;
            border-radius: 5px;
            border: none;
        }
        .stCodeBlock {
            background-color: #1e1e1e !important;
        }
        .stDataFrame {
            background-color: #1c1f26;
        }
    </style>
""", unsafe_allow_html=True)

# --- UI Header ---
st.markdown("<h1 style='text-align:center;'>🚚 AI-Powered Logistics Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:16px;'>Ask smart operational questions. Get instant SQL + results.</p>", unsafe_allow_html=True)

# --- Load Data ---
df = pd.read_sql_query("SELECT * FROM deliveries", conn)

query = st.text_input("🔍 Enter your logistics question:")

if query:
    with st.spinner("Generating SQL and running query..."):
        # GPT prompt to return SQL ONLY
        sql_prompt = f"""You are a logistics SQL assistant.

Given this exact SQLite schema from the `deliveries` table:

truck_id, origin, destination, departure_time, arrival_time, delay_minutes, distance_km, status

Convert the user's question into a valid SQL query.
Use the table name: `deliveries`. 
Only return the SQL code (no markdown, no explanation).

Question: {query}"""

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a logistics SQL assistant. Only return raw SQL queries."},
                    {"role": "user", "content": sql_prompt}
                ]
            )

            sql_code = response.choices[0].message.content.strip()
            st.code(sql_code, language='sql')

            # Execute SQL
            result_df = pd.read_sql_query(sql_code, conn)
            st.dataframe(result_df)

        except Exception as e:
            st.error(f"Error executing SQL: {e}")

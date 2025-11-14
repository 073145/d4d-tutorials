import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
# Must be the first Streamlit command in the script
st.set_page_config(
    page_title="Municipal Spending Dashboard",
    page_icon="📊",
    layout="wide"
)




# --- Data Loading ---
@st.cache_data
def load_data():
    # Diga ao Pandas para ignorar linhas que começam com '#'
    df = pd.read_csv(
        "municipal_spending.csv", 
        comment='#'  # <--- Esta é a linha mágica
    ) 
    df['date'] = pd.to_datetime(df['date'])
    return df

# Load the data
df = load_data()

# --- Dashboard Title ---
st.title("📊 Municipal Spending Dashboard")

# --- Sidebar for Filters ---
st.sidebar.header("Filters")

# Get the list of unique municipalities
municipalities_unique = sorted(df['municipality'].unique())

# Create the selectbox in the sidebar
selected_municipality = st.sidebar.selectbox(
    "Select a Municipality:",
    municipalities_unique
)

# --- Data Filtering ---
# Filter the main dataframe based on user selection
df_filtered = df[df['municipality'] == selected_municipality]

# --- Main Layout (Charts) ---
st.header(f"Analysis for: {selected_municipality}", divider="gray")

# Create two columns for the charts
col1, col2 = st.columns(2)

# --- Chart 1: Spending Over Time (Line Chart) ---
with col1:
    st.subheader("Spending Over Time")
    fig_line = px.line(
        df_filtered,
        x="date",
        y="amount",
        color="category", # Shows different lines for Health, Education, etc.
        title=f"Spending Evolution"
    )
    # Use streamlit's theme and fit to column width
    st.plotly_chart(fig_line, use_container_width=True, theme="streamlit")

# --- Chart 2: Distribution by Category (Pie Chart) ---
with col2:
    st.subheader("Distribution by Category")
    # Group data for the pie chart
    df_grouped_category = df_filtered.groupby('category')['amount'].sum().reset_index()

    fig_pie = px.pie(
        df_grouped_category,
        names="category",
        values="amount",
        title="Percentage of Spending by Category"
    )
    st.plotly_chart(fig_pie, use_container_width=True, theme="streamlit")


# --- Show raw data (optional, with an expander) ---
with st.expander("View Filtered Raw Data"):
    st.dataframe(df_filtered)

# To run this application:
# 1. Save this file as 'app.py'
# 2. Make sure 'municipal_spending.csv' is in the same folder
# 3. Open your terminal and run: streamlit run app.py

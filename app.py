import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import date

# Set the title of the app
st.set_page_config(page_title='GenceCom', layout='wide')
st.title('E-Commerce Dashboard')

# Sidebar for navigation
st.sidebar.header('Navigation')
nav_choice = st.sidebar.radio("", ["📊 Dashboard", "⚙️ Settings", "📄 Contracts"])

# Sidebar for parameters
st.sidebar.header('Dashboard Parameters')

# Add more fake parameters
start_date = st.sidebar.date_input("Start date", date(2024, 1, 1))
end_date = st.sidebar.date_input("End date", date(2024, 12, 31))
category = st.sidebar.selectbox("Select Category", ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Toys"])
region = st.sidebar.selectbox("Select Region", ["North America", "Europe", "Asia", "South America", "Africa"])
threshold = st.sidebar.slider("Sales Threshold", 0, 10000, 5000)

# Add buttons to launch different actions
if st.sidebar.button('Generate Sales Report', key='sidebar_sales_report'):
    st.sidebar.success("Sales Report Generated Successfully!")
if st.sidebar.button('Update Inventory', key='sidebar_update_inventory'):
    st.sidebar.success("Inventory Updated Successfully!")
if st.sidebar.button('Analyze Customer Data', key='sidebar_analyze_customer_data'):
    st.sidebar.success("Customer Data Analyzed Successfully!")

# Main dashboard content
if nav_choice == "📊 Dashboard":
    st.header("")

    # Add a fake KPI section
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric(label="Total Sales", value="$1.2M", delta="15%")
    kpi2.metric(label="Total Orders", value="8.3K", delta="12%")
    kpi3.metric(label="Customer Satisfaction", value="4.5 / 5", delta="0.2")

    # Add buttons to launch algorithms on the main page
    st.subheader("")
    col1, col2, col3 = st.columns(3)
    if col1.button('Run Sales Analysis', key='main_sales_analysis'):
        st.success("Sales Analysis Completed Successfully!")
    if col2.button('Run Inventory Check', key='main_inventory_check'):
        st.success("Inventory Check Completed Successfully!")
    if col3.button('Run Customer Analysis', key='main_customer_analysis'):
        st.success("Customer Analysis Completed Successfully!")

    # Add a fake table with fewer rows
    st.header("Sales Data")
    data = {
        "Order ID": [f"ORD-{i:05d}" for i in range(1, 6)],
        "Product": ["Product A", "Product B", "Product C", "Product D", "Product E"],
        "Category": ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Toys"],
        "Order Date": pd.date_range(start='1/1/2024', periods=5),
        "Sales": np.random.randint(100, 1000, size=5)
    }
    df = pd.DataFrame(data)
    st.table(df)

    # Add a single graph showing market caps per field with different colors
    st.header("Market Caps Per Field")
    fields = ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Toys"]
    market_caps = np.random.randint(1, 100, size=len(fields)) * 1e6

    fig = px.bar(x=fields, y=market_caps, labels={'x': 'Fields', 'y': 'Market Cap ($)'},
                 title="", color=fields)
    st.plotly_chart(fig, use_container_width=True)

    # Add a section for algorithm results
    st.header("Sales Prediction")

    if st.button("Run Sales Prediction", key='main_sales_prediction'):
        st.write("Running sales prediction algorithm...")
        # Fake results
        st.success("Sales prediction completed successfully!")
        results = {
            "Month": ["January", "February", "March"],
            "Predicted Sales": [50000, 60000, 55000]
        }
        results_df = pd.DataFrame(results)
        fig2 = px.bar(results_df, x='Month', y='Predicted Sales', text='Predicted Sales', title='Sales Prediction for Next 3 Months', color='Month')
        st.plotly_chart(fig2, use_container_width=True)

    # Placeholder for images
    st.header("Images")
    st.write("Upload images to be displayed here.")

    uploaded_files = st.file_uploader("Choose an image...", accept_multiple_files=True)
    if uploaded_files:
        for uploaded_file in uploaded_files:
            st.image(uploaded_file, caption=f'Uploaded Image: {uploaded_file.name}', use_column_width=True)

    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Footer with enhanced CSS for full coverage, including sidebar
    footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        height: 50px; /* Set the height of the footer */
        background-color: grey;
        color: white;
        text-align: center;
        line-height: 50px; /* Use the same as height for vertical alignment */
        z-index: 9999; /* Ensures it stays on top */
    }

    /* Ensure the sidebar doesn't overlap the footer */
    div[data-testid="stSidebar"] {
        z-index: 1; /* Ensure sidebar is below the footer */
        bottom: 50px; /* Raise the bottom of the sidebar to make room for the footer */
    }

    /* Additional CSS to ensure content doesn't get hidden under the footer */
    div.block-container {
        padding-bottom: 60px; /* Add padding to make sure content doesn't get hidden under the footer */
    }
    </style>
    """
    st.markdown(footer, unsafe_allow_html=True)

elif nav_choice == "⚙️ Settings":
    st.header("Settings")
    st.write("Settings page content goes here.")

elif nav_choice == "📄 Contracts":
    st.header("Contracts")
    st.write("Contracts page content goes here.")

st.markdown("<div style='text-align: center; margin-top: 50px;'>© 2024 Made by Yoluko Solutions - Alexandre Kocev</div>", unsafe_allow_html=True)

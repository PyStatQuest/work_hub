import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("COVID-19 Data Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload COVID-19 CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV file
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.write(df.head())

    #Bar Chart
    st.subheader("Bar Chart - Cases by Country")
    if 'Country/Region' in df.columns:
        country_data = df['Country/Region'].value_counts().head(10)
        st.bar_chart(country_data)

    #Line Chart
    st.subheader("Line Chart - Cumulative Cases Over Time")
    if 'ObservationDate' in df.columns and 'Confirmed' in df.columns:
        df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
        time_series = df.groupby('ObservationDate')['Confirmed'].sum()
        st.line_chart(time_series)

    #Pie Chart
    st.subheader("Pie Chart - Confirmed Cases by Top 5 Countries")
    if 'Country/Region' in df.columns and 'Confirmed' in df.columns:
        pie_data = df.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False).head(5)
        st.write(pie_data)
        fig, ax = plt.subplots()
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
        ax.axis('equal')
        st.pyplot(fig)


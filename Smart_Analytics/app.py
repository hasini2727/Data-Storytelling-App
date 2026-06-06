import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Smart Analytics Tool")
st.write("Upload a CSV file and perform basic data analysis.")
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.header("Dataset Preview")
    st.dataframe(df.head())
    st.subheader("Dataset Shape")
    st.write(df.shape)
    st.header("Missing Value Analysis")
    st.dataframe(df.isnull().sum())
    st.header("Statistical Summary")
    st.dataframe(df.describe())
    st.header("Dynamic Visualizations")
    numeric_columns = df.select_dtypes(
        include=["number"]
    ).columns
    st.subheader("Scatter Plot")
    x_axis = st.selectbox(
        "Select X-axis",
        numeric_columns,
        key="scatter_x"
    )
    y_axis = st.selectbox(
        "Select Y-axis",
        numeric_columns,
        key="scatter_y"
    )
    fig1 = px.scatter(
        df,
        x=x_axis,
        y=y_axis
    )
    st.plotly_chart(fig1)
    st.subheader("Histogram")
    hist_column = st.selectbox(
        "Select Column",
        numeric_columns,
        key="hist"
    )
    fig2 = px.histogram(
        df,
        x=hist_column
    )
    st.plotly_chart(fig2)
    st.subheader("Box Plot")
    box_column = st.selectbox(
        "Select Column",
        numeric_columns,
        key="box"
    )
    fig3 = px.box(
        df,
        y=box_column
    )
    st.plotly_chart(fig3)
else:
    st.info("Please upload a CSV file to begin analysis.")
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Data Storytelling: Titanic Survival Analysis")
df = pd.read_csv("train.csv")
df = df.dropna(subset=["Age"])
st.header("Dataset Introduction")
st.dataframe(df.head())
st.write("Dataset Shape:", df.shape)
st.header("EDA")
st.write("""
Columns used:

- Survived
- Sex
- Age
- Pclass
- Fare
""")
st.header("Overall Survival Rate")
survival_counts = df["Survived"].value_counts().reset_index()
survival_counts.columns = ["Survived", "Count"]
fig1 = px.bar(
    survival_counts,
    x="Survived",
    y="Count",
    title="Overall Survival Count"
)
st.plotly_chart(fig1)
st.write("More passengers did not survive.")
st.header("Gender and Survival")
gender_survival = df.groupby("Sex")["Survived"].mean().reset_index()
fig2 = px.bar(
    gender_survival,
    x="Sex",
    y="Survived",
    title="Survival Rate by Gender"
)
st.plotly_chart(fig2)
st.write("Females survived more.")
st.header("Passenger Class")
class_survival = df.groupby("Pclass")["Survived"].mean().reset_index()
fig3 = px.bar(
    class_survival,
    x="Pclass",
    y="Survived",
    title="Survival Rate by Passenger Class"
)
st.plotly_chart(fig3)
st.write("Higher class had better survival.")
st.header("Age Distribution")
fig4 = px.histogram(
    df,
    x="Age",
    nbins=20,
    title="Age Distribution"
)
st.plotly_chart(fig4)
st.write("Most passengers were adults.")
st.header("Fare Analysis")
fig5 = px.scatter(
    df,
    x="Age",
    y="Fare",
    color="Survived",
    title="Age vs Fare"
)
st.plotly_chart(fig5)
st.write("Age and Fare")
st.header("Conclusion")
st.success("""
1. Females survived more.

2. First class survived more.

3. Gender affected survival.

4. Passenger class affected survival.
""")
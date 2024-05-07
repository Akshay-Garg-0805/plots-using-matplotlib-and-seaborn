import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.DataFrame(np.random.randn(20,3),columns=[1,2,3])

st.header("Plots using streamlit builtin commands")

# line chart
st.line_chart(df)

# area chart
st.area_chart(df)

# barchart
st.bar_chart(df)

st.header("Visulaization Using Matplotlib and Seaborn")
# reading dataset from csv using pandas
df = pd.read_csv("iris.csv")
st.dataframe(df)

st.subheader("Bar Plot using matplotlib")
fig = plt.figure(figsize=(15,8))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader("Dist plot using seaborn")
fig = plt.figure(figsize=(15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.subheader("Multiple plots")
col1, col2, col3 = st.columns(3)
with col1:
    col1.write("KDE = False")
    fig1=plt.figure()
    sns.distplot(df['sepal_length'],kde=False)
    st.pyplot(fig1)
with col2:
    col2.write("Hist=False")
    fig2=plt.figure()
    sns.distplot(df['sepal_length'],hist=False)
    st.pyplot(fig2)
with col3:
    col3.write("Full")
    fig3=plt.figure()
    sns.distplot(df['sepal_length'])
    st.pyplot(fig3)

st.subheader("Scatter plot")
fig,ax = plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader("Count plot")
fig=plt.figure(figsize=(15,8))
sns.countplot(data=df,x='species')
st.pyplot(fig)

st.subheader("Box plot")
fig = plt.figure(figsize=(15,8))
sns.boxplot(data=df,x='species',y='petal_length')
st.pyplot(fig)

st.subheader("Violin Plot")
fig=plt.figure(figsize=(15,8))
sns.violinplot(data=df,x='species',y='petal_length')
st.pyplot(fig)
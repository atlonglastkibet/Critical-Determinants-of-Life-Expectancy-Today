import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset (Ensure your CSV or DataFrame is available)
df = pd.read_csv("/home/davidkibet/Desktop/Life Expectancy ML/docs/EDA_for_data.csv")  # Replace with your actual dataset

# Sort data by year
df_sorted = df.sort_values(by="Year", ascending=True)

# Define color range limits
zmin, zmax = df_sorted['Life expectancy '].min(), df_sorted['Life expectancy '].max()

# Create an animated choropleth map
fig = px.choropleth(
    df_sorted,
    locations='Country',
    locationmode="country names",  
    color='Life expectancy ',
    animation_frame='Year',       
    color_continuous_scale="YlGnBu",
    range_color=(zmin, zmax),
    # title="Animated Choropleth Map of Life Expectancy (2000–2015)"
)

# Optimize layout
fig.update_layout(
    autosize=True,
    height=800,  # Adjust height to fit the page
    title_x=0.5,
    margin=dict(l=0, r=0, t=40, b=0)  # Reduce margins for a full-screen effect
)

# # Streamlit App UI
# st.title("Life Expectancy Analysis")
# st.write("This is an interactive visualization of life expectancy trends from 2000 to 2015.")

# Display the choropleth map
st.plotly_chart(fig, use_container_width=True)

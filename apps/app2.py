import streamlit as st
import plotly.express as px
import pandas as pd

# Set page configuration for full-screen layout
st.set_page_config(page_title="Global Life Expectancy", layout="wide")

# Custom CSS to enhance the app's appearance
st.markdown("""
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .stPlotlyChart {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and introduction
st.title("Global Life Expectancy Trends (2000-2015)")
st.markdown("*An interactive visualization exploring life expectancy across countries*")

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("/home/davidkibet/Desktop/Life Expectancy ML/docs/EDA_for_data.csv")

df = load_data()

# Prepare the data
df_sorted = df.sort_values(by="Year", ascending=True)

# Calculate color range
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
    title="Life Expectancy Evolution (2000-2015)"
)

# Optimize layout for full-screen render
fig.update_layout(
    autosize=True,
    height=700,  # Slightly reduced to ensure clean fit
    title_x=0.5,
    margin=dict(l=20, r=20, t=50, b=20),
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    )
)

# Customize color bar
fig.update_coloraxes(
    colorbar_title_text='Life Expectancy (Years)',
    colorbar_title_side='right'
)

# Display the choropleth map
st.plotly_chart(fig, use_container_width=True)

# Additional insights section
st.markdown("### Key Observations")
st.markdown("""
- The map shows global life expectancy trends from 2000 to 2015
- Color intensity represents life expectancy levels
- Use the play button to animate changes over time
""")
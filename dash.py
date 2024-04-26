import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Load the datasets for each city
Benin_city1_df = pd.read_csv("src/models/datasets/Benin/solar-measurements_benin-malanville_qc.csv", encoding='latin-1', low_memory=False)
Benin_city2_df = pd.read_csv("src/models/datasets/Benin/solar-measurements_benin-parakou_qc.csv", encoding='latin-1', low_memory=False)

Sirearra_Leone_city1_df = pd.read_csv("src/models/datasets/Sirearra-Leone/solar-measurements_sierraleone-bumbuna_qc.csv", encoding='latin-1', low_memory=False)
Sirearra_Leone_city2_df = pd.read_csv("src/models/datasets/Sirearra-Leone/solar-measurements_sierraleone-kenema_qc.csv", encoding='latin-1', low_memory=False)

Togo_city1_df = pd.read_csv("src/models/datasets/Togo/solar-measurements_togo-dapaong_qc.csv", encoding='latin-1', low_memory=False)
Togo_city2_df = pd.read_csv("src/models/datasets/Togo/solar-measurements_togo-davie_qc.csv", encoding='latin-1', low_memory=False)

# Sidebar
st.sidebar.title('MoonLight Energy Solutions')
st.sidebar.image("tests/th.jpeg", width=150, use_column_width=False)
st.sidebar.markdown("""
    <style>
        .sidebar-image img {
            border-radius: 50%;
            border: 2px solid #ccc;
            width: 150px;
            height: 150px;
            object-fit: cover;
        }
    </style>
""", unsafe_allow_html=True)

# Select country
country_list = ['Benin', 'Sierra Leone', 'Togo']
selected_country = st.sidebar.selectbox('Select a country', country_list)

# Get the corresponding datasets based on the selected country
if selected_country == 'Benin':
    city1_df = Benin_city1_df
    city2_df = Benin_city2_df
elif selected_country == 'Sierra Leone':
    city1_df = Sirearra_Leone_city1_df
    city2_df = Sirearra_Leone_city2_df
elif selected_country == 'Togo':
    city1_df = Togo_city1_df
    city2_df = Togo_city2_df

# Select plot type
plot_type_list = ['Histogram', 'Scatter Plot']
selected_plot_type = st.sidebar.selectbox('Select a plot type', plot_type_list)

# Define function to display descriptions
def display_description(plot_type, city1_df, city2_df):
    city1_df['GHI'] = pd.to_numeric(city1_df['GHI'], errors='coerce')
    city2_df['GHI'] = pd.to_numeric(city2_df['GHI'], errors='coerce')
    city1_df['Tamb'] = pd.to_numeric(city1_df['Tamb'], errors='coerce')
    city2_df['Tamb'] = pd.to_numeric(city2_df['Tamb'], errors='coerce')
    
    if plot_type == 'Histogram':
        diff1 = city1_df['GHI'].mean() - city2_df['GHI'].mean()
        diff2 = city1_df['GHI'].median() - city2_df['GHI'].median()
        return f"In this comparison:\n- City 1's mean GHI is {diff1:.2f} higher than City 2's.\n- City 1's median GHI is {diff2:.2f} higher than City 2's."
    elif plot_type == 'Scatter Plot':
        diff1 = city1_df['Tamb'].mean() - city2_df['Tamb'].mean()
        diff2 = city1_df['Tamb'].median() - city2_df['Tamb'].median()
        return f"In this comparison of data of:\n- City 1's mean Ambient Temperature is {diff1:.2f} higher than City 2's.\n- City 1's median Ambient Temperature is {diff2:.2f} higher than City 2's."

# Create two columns for sidebar and main content
sidebar, main = st.columns([1, 4])

# Sidebar
with sidebar:
    # Sidebar content
    st.sidebar.title('MoonEnergy Solar Installation')
    # Add sidebar content here

# Main content
with main:
    st.title("Solar Data Analysis")

    # Plot the selected data
    if selected_plot_type == 'Histogram':
        fig, axes = plt.subplots(1, 2, figsize=(15, 7))

        # Histograms for City 1
        axes[0].hist(city1_df['GHI'], bins=20, edgecolor='black')
        axes[0].set_xlabel('GHI')
        axes[0].set_ylabel('Frequency')
        axes[0].set_title(f'Global Horizontal Irradiance (GHI) - City 1')

        # Histograms for City 2
        axes[1].hist(city2_df['GHI'], bins=20, edgecolor='black')
        axes[1].set_xlabel('GHI')
        axes[1].set_ylabel('Frequency')
        axes[1].set_title(f'Global Horizontal Irradiance (GHI) - City 2')

        plt.tight_layout()
        st.pyplot()

        # Write the description
        st.write("**Description for Histogram:**")
        st.write(display_description(selected_plot_type, city1_df, city2_df))

    elif selected_plot_type == 'Scatter Plot':
        fig, axes = plt.subplots(1, 2, figsize=(15, 7))

        # Scatter plots for City 1
        axes[0].scatter(city1_df['GHI'], city1_df['Tamb'])
        axes[0].set_xlabel('GHI')
        axes[0].set_ylabel('Ambient Temperature (°C)')
        axes[0].set_title(f'GHI vs. Ambient Temperature - City 1')

        # Scatter plots for City 2
        axes[1].scatter(city2_df['GHI'], city2_df['Tamb'])
        axes[1].set_xlabel('GHI')
        axes[1].set_ylabel('Ambient Temperature (°C)')
        axes[1].set_title(f'GHI vs. Ambient Temperature - City 2')

        plt.tight_layout()
        st.pyplot()
        # Write the description
        st.write("**Description for Scatter Plot:**")
        st.write(display_description(selected_plot_type, city1_df, city2_df))

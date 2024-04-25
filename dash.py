import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data for each city
data_Benin_parakou = pd.read_csv("src/models/datasets/Benin/solar-measurements_benin-malanville_qc.csv", encoding='latin-1',low_memory=False)
data_Benin_malanville = pd.read_csv("src/models/datasets/Benin/solar-measurements_benin-parakou_qc.csv",encoding='latin-1',low_memory=False)
data_Sierra_Leone_bumbuna = pd.read_csv("src/models/datasets/Sirearra-Leone/solar-measurements_sierraleone-bumbuna_qc.csv", encoding='latin-1',low_memory=False)
data_Sierra_Leone_kenema = pd.read_csv("src/models/datasets/Sirearra-Leone/solar-measurements_sierraleone-kenema_qc.csv",encoding='latin-1',low_memory=False)
data_Togo_dapaong = pd.read_csv("src/models/datasets/Togo/solar-measurements_togo-dapaong_qc.csv", encoding='latin-1',low_memory=False)
data_Togo_davie = pd.read_csv("src/models/datasets/Togo/solar-measurements_togo-davie_qc.csv",encoding='latin-1',low_memory=False)

# Function to generate scatter plots
def generate_scatter_plots(data, title_suffix):
    plt.figure(figsize=(12, 8))
    # Scatter plots generation code...

# Function to generate histograms
def generate_histograms(data, title_suffix):
    plt.figure(figsize=(12, 8))
    # Histograms generation code...

# Function to display the home page
def display_home_page():
    st.title("MoonLight Energy Solutions")
    # Home page content...

# Function to display analysis for Benin cities
def display_benin_analysis():
    st.header('Analysis for Benin - Parakou')
    generate_scatter_plots(data_Benin_parakou, 'Benin - Parakou')
    generate_histograms(data_Benin_parakou, 'Benin - Parakou')
    # Add more analysis for Benin cities...

# Function to display analysis for Sierra Leone cities
def display_sierra_leone_analysis():
    st.header('Analysis for Sierra Leone - Bumbuna')
    generate_scatter_plots(data_Sierra_Leone_bumbuna, 'Sierra Leone - Bumbuna')
    generate_histograms(data_Sierra_Leone_bumbuna, 'Sierra Leone - Bumbuna')
    # Add more analysis for Sierra Leone cities...

# Function to display analysis for Togo cities
def display_togo_analysis():
    st.header('Analysis for Togo - Dapaong')
    generate_scatter_plots(data_Togo_dapaong, 'Togo - Dapaong')
    generate_histograms(data_Togo_dapaong, 'Togo - Dapaong')
    # Add more analysis for Togo cities...

# Function to display comparison between cities of the same country
def display_city_comparison():
    st.header('Compare Cities from the Same Country')
    # Comparison logic...

# Function to display conclusion and acknowledgements
def display_conclusion_and_acknowledgements():
    st.header('Conclusion')
    st.write("In conclusion, the analysis provides insights into solar radiation and temperature patterns across different cities, which are essential for solar panel installation and energy production.")

    st.write("Thank you for reading our solar panel installation analysis blog!")

# Main function to handle page navigation
def main():
    pages = {
        "Home": display_home_page,
        "Benin Analysis": display_benin_analysis,
        "Sierra Leone Analysis": display_sierra_leone_analysis,
        "Togo Analysis": display_togo_analysis,
        "Compare Cities": display_city_comparison,
        "Conclusion": display_conclusion_and_acknowledgements
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    pages[selection]()

if __name__ == "__main__":
    main()

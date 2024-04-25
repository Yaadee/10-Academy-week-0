import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load data for each city
Benin_city1_df = pd.read_csv("src/models/datasets/Benin/solar-measurements_benin-malanville_qc.csv", encoding='latin-1',low_memory=False)
Benin_city2_df = pd.read_csv("src/models/datasets/Benin/solar-measurements_benin-parakou_qc.csv",encoding='latin-1',low_memory=False)

Sirearra_Leone_city1_df = pd.read_csv("src/models/datasets/Sirearra-Leone/solar-measurements_sierraleone-bumbuna_qc.csv", encoding='latin-1',low_memory=False)
Sirearra_Leone_city2_df = pd.read_csv("src/models/datasets/Sirearra-Leone/solar-measurements_sierraleone-kenema_qc.csv",encoding='latin-1',low_memory=False)

Togo_city1_df = pd.read_csv("src/models/datasets/Togo/solar-measurements_togo-dapaong_qc.csv", encoding='latin-1',low_memory=False)
Togo_city2_df = pd.read_csv("src/models/datasets/Togo/solar-measurements_togo-davie_qc.csv",encoding='latin-1',low_memory=False)


st.set_page_config(page_title="MoonLight Energy Solutions",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )
st.title("MoonLight Energy Solutions")

@st.cache_data
def load_data(path:str):
    data = pd.read_csv("src/models/datasets/Benin/solar-measurements_benin-malanville_qc.csv",encoding='latin-1',low_memory=False)
    return data

with st.sidebar:
    upload_file = st.file_uploader("Choose a file", type=["csv", "xlsx",'pdf'])

    if upload_file is None:
        st.info("upload file through config",icon="ℹ️")
        st.stop()

df = load_data(upload_file)


Benin_city1=Benin_city1_df.describe()


col1, col2, col3 = st.columns([1,1,1])


Converted_to_numeric=Benin_city1_df.apply(pd.to_numeric, errors='coerce')

st.write(Converted_to_numeric)
st.write(Converted_to_numeric.describe())

st.subheader('Summary Statistics for Benin')
st.write(Benin_city1_df.describe())


correlation_matrix = benin_city1_df[['GHI', 'DHI', 'DNI', 'TModA', 'TModB']].corr()
st.subheader('Corrolation matrix')
st.write(correlation_matrix)


Benin_city1_df = Benin_city1_df[Benin_city1_df['Timestamp'] != 'yyyy-mm-dd hh:mm']
Benin_city1_df['Timestamp'] = pd.to_datetime(Benin_city1_df['Timestamp'])

# Title and Introduction
st.title('Solar Panel Installation Analysis')
st.write("Welcome to the solar panel installation analysis blog!")

# Visualization for Benin City
st.header('Analysis for Benin City')

Benin_city2_df = Benin_city2_df[Benin_city2_df['Timestamp'] != 'yyyy-mm-dd hh:mm']
Benin_city2_df['Timestamp'] = pd.to_datetime(Benin_city2_df['Timestamp'])

# Title and Introduction
st.title('Solar Panel Installation Analysis')
st.write("Welcome to the solar panel installation analysis blog!")

# Visualization for Benin City
st.header('Analysis for Benin City')





# Plot GHI
plt.figure(figsize=(10, 6))
plt.plot(Benin_city1_df['Timestamp'].to_numpy(), Benin_city1_df['GHI'], label='GHI', color='blue')
plt.xlabel('Timestamp')
plt.ylabel('GHI')
plt.title('Variation of GHI over Time')
plt.xticks(rotation=45)
plt.legend()
st.pyplot()

# Conclusion
st.header('Conclusion')
st.write("In conclusion, the plot above shows the variation of Global Horizontal Irradiance (GHI) over time in Benin City, which is important for understanding the solar radiation pattern.")



# Visualization: Histogram for GHI (Global Horizontal Irradiance) - City 1
plt.figure(figsize=(10, 6))
sns.histplot(Benin_city1_df['GHI'], bins=20, kde=True)
plt.title('Histogram of GHI in City 1')
plt.xlabel('GHI')
plt.ylabel('Frequency')
st.pyplot()

# Visualization for City 2
st.header('City 2 Analysis')

# Summary Statistics for City 2
st.subheader('Summary Statistics for City 2')
st.write(Benin_city2_df.describe())

# Visualization: Histogram for GHI (Global Horizontal Irradiance) - City 2
plt.figure(figsize=(10, 6))
sns.histplot(Benin_city2_df['GHI'], bins=20, kde=True)
plt.title('Histogram of GHI in City 2')
plt.xlabel('GHI')
plt.ylabel('Frequency')
st.pyplot()

# Comparison between Cities
st.header('City Comparison')

# Select cities to compare
selected_cities = st.multiselect('Select cities to compare', ['City 1', 'City 2', 'City 3'])

# Visualization: Histogram for GHI Comparison
if len(selected_cities) > 1:
    plt.figure(figsize=(10, 6))
    for city in selected_cities:
        if city == 'City 1':
            sns.histplot(city1_df['GHI'], bins=20, kde=True, label='City 1')
        elif city == 'City 2':
            sns.histplot(city2_df['GHI'], bins=20, kde=True, label='City 2')
        elif city == 'City 3':
            sns.histplot(city3_df['GHI'], bins=20, kde=True, label='City 3')
    plt.title('Histogram of GHI Comparison between Cities')
    plt.xlabel('GHI')
    plt.ylabel('Frequency')
    plt.legend()
    st.pyplot()
else:
    st.write("Select at least two cities for comparison")

# Conclusion
st.header('Conclusion')
st.write("In conclusion, each city's solar panel installation analysis reveals different levels of solar radiation, which can impact the efficiency and feasibility of solar energy projects.")

# Acknowledgements
st.write("Thank you for reading our solar panel installation analysis blog!")


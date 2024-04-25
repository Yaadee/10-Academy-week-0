import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(page_title="MoonLight Energy Solutions",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )
st.title("MoonLight Energy Solutions")

@st.cache_data
def load_data(path:str):
    data = pd.read_csv("/home/yadasa/Desktop/10-Academy-week-0/src/models/datasets/Benin/solar-measurements_benin-malanville_qc.csv")
    return data

with st.sidebar:
    upload_file = st.file_uploader("Choose a file", type=["csv", "xlsx",'pdf'])

    if upload_file is None:
        st.info("upload file through config",icon="ℹ️")
        st.stop()

df = load_data(upload_file)

col1, col2, col3 = st.columns([1,1,1])

# Adding a filter for software sales
all_months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

sales_data = df.loc[(df["Year"] == 2023) & 
            (df["Account"]=="Sales")&
            (df["business_unit"] =="Software"),
            ["Scenario"] + all_months,
            ].melt(
                id_vars="Scenario",
                var_name="month",
                value_name= "sales",
            )

with col1.expander("Sales Data"):
    st.dataframe(
        df,
        column_config={
            "Year": st.column_config.NumberColumn(format="%d")
        }
        )




info = sales_data.describe()

with col2.expander("Description"):
    st.write(info)


col3.metric(label="Total Sales", value= '${:,.2}'.format(sales_data["sales"].sum()/1000000000)+"B", delta="-3" )


#scatter plot
@st.cache_data
def scatter_plot():
    fig = px.scatter(sales_data, x="month", y="sales", color="Scenario", title="Monthly Budget vs Forecast 2023")
    st.plotly_chart(fig, use_container_width=True)

with col1:
    scatter_plot()

@st.cache_data
def line_plot():
    fig = px.line(sales_data, x="month", y="sales", color="Scenario",text= "sales", markers=True,
                  title="Monthly Budget vs Forecast 2023")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    line_plot()


# Pie chart
@st.cache_data
def pie_plot():
    fig = px.pie(df, names="Account")
    st.plotly_chart(fig, use_container_width=True)

with col3:
    pie_plot()


# Bar chart
@st.cache_data
def bar_plot():
    fig = px.bar(sales_data, x="month", y="sales", color="Scenario", title="Monthly Budget vs Forecast 2023")
    st.plotly_chart(fig, use_container_width=True)  


with col1:
    bar_plot()

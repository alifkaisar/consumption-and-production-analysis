import streamlit as st
import pandas as pd
import visualization

# read file csv
consumption_df = pd.read_csv("data/consumption/consumption_final.csv")
production_df = pd.read_csv("data/production/production_final.csv")
correlation_2021 = pd.read_csv("data/correlation/correlation_2021.csv", index_col=0)
correlation_2022 = pd.read_csv("data/correlation/correlation_2022.csv", index_col=0)

st.set_page_config(
    page_title="Consumption and Production of Fruit",
    page_icon="https://www.svgrepo.com/show/530445/data-analysis.svg",
    layout="centered",
    initial_sidebar_state="expanded")

with open("style.css") as css_file:
    st.write(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.header("Dashboard")
    select_data = st.selectbox(
        label="Select Data",
        options=["Consumption of Fruit", "Production of Fruit", "Correlation"])

    if select_data == "Consumption of Fruit":
        based_on = st.selectbox(label="Based on", options=["National", "Province"])
        year = st.radio(label="Select Year", options=[2021, 2022, 2023])

        # split data consumption by year and province
        consumption_yr = consumption_df[consumption_df.Year == year]
        mean_consumption_yr = consumption_yr[consumption_yr.columns[3::]].mean().sort_values(ascending=False)
        consumption_province = consumption_yr.groupby(by="Province", as_index=False)[consumption_yr.columns[3::]].mean()

        if based_on == "Province":
            province = st.selectbox(label="Select Province", options=consumption_province.Province)
            fruits_consumption = consumption_province[consumption_province.Province == province]
            consumption_data = fruits_consumption[fruits_consumption.columns[1::]].squeeze().sort_values(ascending=False)

    elif select_data == "Production of Fruit":
        production_yr = production_df[production_df.columns[1::]].groupby(by="Year", as_index=False).sum()
        new_production_yr = visualization.recreate_df(data_frame=production_yr,
                                                      columns_name=["Fruit", "Year", "Production (Ton)"],
                                                      unselected_columns=1)
        new_production_yr["Year"] = new_production_yr["Year"].astype(int).astype(str)
        new_production_yr.sort_values(by=["Year", "Production (Ton)"], ascending=True, ignore_index=True, inplace=True)

    else:
        year = st.radio(label="Select Year", options=[2021, 2022])
        correlation_data = correlation_2022

    st.markdown("About Me: [LinkedIn](https://www.linkedin.com/in/alifkaisar/)")
    st.markdown("Notebook: [Google Colaboratory]("
                "https://colab.research.google.com/drive/1T3OVzKDZjnlarKUFsT90mb5b3e7F1SQ7?usp=sharing)")

# main page
if select_data == "Consumption of Fruit" and based_on == "National":
    st.header(select_data.upper())
    # bar chart
    st.subheader(f"Weekly Fruit Consumption in {year}")
    bar_plot = visualization.bar_plot(x=consumption_yr.columns[3::], y=mean_consumption_yr, color="dodgerblue",
                                      ylabel="Consumption (g/capital/week)")
    container = st.container(border=True)
    container.pyplot(bar_plot)
    container.write(
        "<p class='image-caption'>"
        "Source of data: "
        "<a href='https://www.bps.go.id/id/statistics-table/2/MjEwMiMy/rata-rata-konsumsi-perkapita-seminggu-menurut"
        "-kelompok-buah-buahan-per-kabupaten-kota--satuan-komoditas-.html'>BPS, 2024""</a>"
        "</p>",
        unsafe_allow_html=True)

    # top 5 fruits
    st.subheader(f"Top 5 fruits most consumed in a week")
    top_5 = pd.DataFrame(data={
        "Fruit": mean_consumption_yr.index[:5:],
        "Consumption (g/capita/week)": mean_consumption_yr.values[:5:]})
    st.dataframe(top_5, hide_index=True, use_container_width=True, height=220)

    # avg consumption in a week
    st.subheader("Average consumption in a week of the top 5 fruits in each province")
    col1, col2 = st.columns(2)
    fruit = col1.selectbox(label="Select Fruit", options=mean_consumption_yr.index[:5:])
    consumption_province.sort_values(by=fruit, ascending=False, inplace=True)
    st.dataframe(consumption_province[["Province", fruit]], hide_index=True, use_container_width=True)

elif select_data == "Consumption of Fruit" and based_on == "Province":
    st.header(select_data.upper())
    # bar chart
    st.subheader(f"Weekly Fruit Consumption in {province} Province for the Year {year}")

    bar_plot = visualization.bar_plot(x=fruits_consumption.columns[1::], y=consumption_data, color="deepskyblue",
                                      ylabel="Consumption (g/capital/week)")
    container = st.container(border=True)
    container.pyplot(bar_plot)
    container.write(
        "<p class='image-caption'>"
        "Source of data: "
        "<a href='https://www.bps.go.id/id/statistics-table/2/MjEwMiMy/rata-rata-konsumsi-perkapita-seminggu-menurut"
        "-kelompok-buah-buahan-per-kabupaten-kota--satuan-komoditas-.html'>BPS, 2024""</a>"
        "</p>",
        unsafe_allow_html=True)

elif select_data == "Production of Fruit":
    st.header(select_data.upper())
    st.subheader("Production of Fruits in 2021 and 2022")
    barh = visualization.barh_plotly(new_production_yr, x="Production (Ton)", y="Fruit", group="Year")
    container = st.container(border=True)
    container.plotly_chart(barh, use_container_width=True)
    container.write(
        "<p class='image-caption'>"
        "Source of data: "
        "<a href='https://www.bps.go.id/id/statistics-table/2/NjIjMg==/produksi-tanaman-buah-buahan.html'>BPS, 2024</a>"
        "</p>",
        unsafe_allow_html=True)

else:
    st.header(select_data.upper())
    st.subheader(f"Correlation Between Consumption and Production of Fruit in {year}")
    if year == 2021:
        heatmap = visualization.heatmap_plotly(data_frame=correlation_2021)
    else:
        heatmap = visualization.heatmap_plotly(data_frame=correlation_2022)
    container = st.container(border=True)
    container.plotly_chart(heatmap, use_container_width=True)
    container.write(
        "<p class='image-caption'>"
        "Dark colors mean negative correlation values. The brighter the color means the correlation value is closer to 1."
        "</p>",
        unsafe_allow_html=True)

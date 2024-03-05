# Introduction

**There were two datasets:**

1. Fruit consumption (g/capita/week) ~  `consumption.csv`

    The fruit consumption data represents the average weekly per capita consumption across fruit groups for each 
    regency/city from 2021 to 2023. To make the analysis easier, the province column has been added manually so that it can be easily grouped by province.

2. Fruit production (Ton) ~ `production.csv`

   The fruit production data represents the total production of fruit groups per province in the years 2021 and 2022.
   Both data have different number of rows and columns because the fruit data obtained is different.

**The purpose of this data analysis is:**
1. Knowing fruit consumption on a national and provincial scale each year

    a. What is the most consumed fruit every week on a national scale each year?

    b. What is the most consumed fruit each week in each province each year?

2. Knowing the fruit production in each year.

    a. Which fruit has the highest production each year?

3. Knowing the correlation between fruit consumption and fruit production on a national scale in each year.

    a. Is there a positive or negative correlation between fruit consumption and fruit production?

    
**Data source:**
1. Fruit consumption - [BPS](https://www.bps.go.id/en/statistics-table/2/MjEwMiMy/rata-rata-konsumsi-perkapita-seminggu-menurut-kelompok-buah-buahan-per-kabupaten-kota--satuan-komoditas-.html)
2. Fruit production - [BPS](https://www.bps.go.id/en/statistics-table/2/NjIjMg==/produksi-tanaman-buah-buahan.html)

# Data File
There are 6 data files in this repository inside data folder. In this web app using 4 files:
1. `consumption_final.csv` for data consumption
2. `production_final.csv`for data production
3. `correlation_2021` for data correlation between consumption and production in 2021
4. `correlation_2022` for data correlation between consumption and production in 2022

For `consumption.csv` and `production.csv` using for analysis data in Google Colaboratory Notebook. 

Many files exist because the consumption and production data is the original file or the first file before analysis. 
The other files are data frames obtained from the analysis to make it easier to create web applications.

# Notebook and Web App
As mentioned earlier, the analysis data uses `consumption.csv` and `production.csv` files. See the analysis results:
- Google Colaboratory - [Here](https://colab.research.google.com/drive/1T3OVzKDZjnlarKUFsT90mb5b3e7F1SQ7?usp=sharing)

For web application using Streamlit. See web application:
- Streamlit - [Here](https://dasboardalif.streamlit.app)

# About Me
See more about me - [Here](https://alifcoding.cyclic.app/)

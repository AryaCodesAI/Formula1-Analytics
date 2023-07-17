import pandas as pd
import streamlit as st
import fastf1 as ff
import plotly.express as px

st.title("Formula One Driver's Statistics")

with st.sidebar:
    list = [2022,2021,2020,2019, 2018,2017,2016,2015,2014,2013,2012,2011,2010,2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000]
    season_year = st.selectbox('Select Season', options = list)
    GPs = ["Monaco Grand Prix", "Italian Grand Prix","Sakhir Grand Prix", "British Grand Prix", "German Grand Prix", "Belgian Grand Prix", "Spanish Grand Prix", "Australian Grand Prix", "Brazilian Grand Prix", "Hungarian Grand Prix", "Canadian Grand Prix", "French Grand Prix", "Austrian Grand Prix", "Japanese Grand Prix", "Malaysian Grand Prix", "United States Grand Prix", "Chinese Grand Prix", "Turkish Grand Prix", "Abu Dhabi Grand Prix", "Bahrain Grand Prix", "Russian Grand Prix", "Mexican Grand Prix", "Singapore Grand Prix", "European Grand Prix", "South African Grand Prix", "Argentine Grand Prix", "Indian Grand Prix", "Korean Grand Prix", "Portuguese Grand Prix", "Dutch Grand Prix", "Swedish Grand Prix", "San Marino Grand Prix", "Luxembourg Grand Prix", "Pacific Grand Prix", "Imola Grand Prix", "Indianapolis Grand Prix", "Maltese Grand Prix", "Moroccan Grand Prix", "Spanish Grand Prix (Valencia)", "South Korean Grand Prix", "Turkish Grand Prix (Istanbul Park)", "Vietnamese Grand Prix", "Saudi Arabian Grand Prix"]
    GPrix = st.selectbox("Select GP", options = GPs)
session = ff.get_session(season_year,GPrix,'Race')
session.load()
df_race = pd.DataFrame(session.results)

driver = st.multiselect("Select drivers", options=df_race.Abbreviation.unique())
selected_driver = session.laps.pick_drivers(driver)
driver_who= selected_driver['Driver']
lap_pos = selected_driver['Position'].astype(int)
lap_num = selected_driver['LapNumber'].astype(int)
df_driver = pd.DataFrame([lap_pos,lap_num,driver_who]).T
df_driver = df_driver.reset_index(drop='index')
df_driver = df_driver[['LapNumber', 'Position', 'Driver']]

fig = px.line(df_driver, x=df_driver['LapNumber'], y=df_driver['Position'],color='Driver', range_y=[1,20])
fig.update_yaxes(dtick=1)  
st.plotly_chart(fig)


fig0 = px.bar(df_race, x="Points", y="DriverId", color='Position', title='Total Points by Drivers')
st.plotly_chart(fig0)


fig1 = px.bar(df_race, x='TeamId', y='Points', color="TeamId" ,title='Total Points by Team')
st.plotly_chart(fig1)
import streamlit as st
import pandas as pd
import numpy as np

# # df=pd.DataFrame(np.random.randn(500, 2) / [50, 50]+ [37.76, -122.4],
# # columns=['lat': [],'lon':[]])
# cord={'lat': [25.408386830496415],'lon':[68.26042998027525]}
# df= pd.DataFrame(cord)
# st.map(df)

lat=[]
lon=[]
cord={}

lat=st.number_input ("Enter the value of Latitude")

lon=st.number_input("Enter the value of Longitude")
cord={}
lat.append()
lon.append()
cord["lat"]=lat
cord["lon"]=lon
df=pd.DataFrame(cord)
st.map(df)

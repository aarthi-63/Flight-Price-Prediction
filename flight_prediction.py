# -*- coding: utf-8 -*-
"""
Created on Thu May  8 12:18:01 2025

@author: AARTHI KRISHNAN
"""
import datetime
import streamlit as st
from PIL import Image
import pickle
import pandas as pd

# Deserialization process (python object from byte stream)
encoder=pickle.load(open("encode_file.pkl",'rb'))
model=pickle.load(open("model_file.pkl",'rb'))

# function that predicts the output
def predictive_system(input):
    input_df=pd.DataFrame(input)
    # encoding the categorical column
    encoded_arr=encoder.transform(input_df.iloc[:,:3])
    encoded_df=pd.DataFrame(encoded_arr)
    #final dataframe-input
    final_df=pd.concat([encoded_df,input_df.drop([0,1,2],axis=1)],axis=1)
    
    #prediction
    price=model.predict(final_df)
    return int(price)

def web_app():
    
    img=Image.open("flight.webp")
    st.image(img,width=800)
    
    st.title("Flight Price prediction")
    
    airline=st.selectbox("Airline : ",
                         ['IndiGo','Air India','Jet Airways','SpiceJet','Multiple carriers','GoAir','Vistara','Air Asia','Vistara Premium economy','Jet Airways Business','Multiple carriers Premium economy','Trujet'])
    
    source=st.selectbox("Departure : ",
                        ['Banglore','Kolkata','Delhi','Chennai','Mumbai'])
    
    destination=st.selectbox("Arrival : ",
                             ['Delhi','Banglore','Cochin','Kolkata','Hyderabad'])
    
    stop=int(st.slider("Select total Stops : ",1,5))
    
    input_date=st.date_input("Date of Journey")
    date=int(input_date.day)
    month=int(input_date.month)
    
    dept_time=st.time_input("Departure Time : ")
    departure_hour=int(dept_time.hour)
    departure_minute=int(dept_time.minute)
    
    arrival_time=st.time_input("Arrival Time : ")
    arrival_hour=int(arrival_time.hour)
    arrival_minute=int(arrival_time.minute)
    
    duration_hr=0
    duration_min=0
    start=(departure_hour*60)+departure_minute
    end=(arrival_hour*60)+arrival_minute
    if end<start:
        # adding the 24 hours (24*60)
        end=end+1440
    diff=end-start
    duration_hr=diff//60
    duration_min=diff%60
    
    
    if st.button("Predict"):
        price_value=predictive_system([[airline,source,destination,stop,date,month,departure_hour,departure_minute,arrival_hour,arrival_minute,duration_hr,duration_min]])
        st.info("Your predicted flight price is :")
        st.success(f'₹ {price_value}')
    
    
if __name__=='__main__':
    web_app()
    
                                
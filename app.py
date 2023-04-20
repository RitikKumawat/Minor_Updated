import numpy as np 
import pickle
import pandas as pd 

import streamlit as st 


pickle_in = open("model.pkl","rb")
model = pickle.load(pickle_in)

def fraud_prediction(input_data):
    input_data_as_numpy_array =  np.array(input_data)

    input_data_reshaped =  input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return "It is not a fraud transaction"
    else:
        return "It is a fraud Transaction"

def main():
#     st.title("Credit Card Fraud Detector")
    html_temp = """ 
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Credit card Fraud Detector</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    distance_from_home = st.text_input("Distance from home")
    distance_from_last_transaction = st.text_input("Distance from last transaction")
    ratio_to_median_purchase_price = st.text_input("Ratio to median purchase price")
    repeat_retailer = st.text_input("Repeat retailer")
    used_chip = st.text_input("Used chip")
    used_pin_number = st.text_input("Used pin number")
    online_order = st.text_input("Online order")

    detection = ''
    if st.button("Detect Fraud"):
        detection = fraud_prediction([distance_from_home,distance_from_last_transaction,ratio_to_median_purchase_price,repeat_retailer,used_chip,used_pin_number,online_order])
    st.success(detection)

if __name__ == "__main__":
    main()

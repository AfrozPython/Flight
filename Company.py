# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:29:34 2022

@author: Afroz
"""

import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('C:/Users/Appu/Desktop/Streamlit Test/Best Code Streamlit/Z Test Programs/1000 companies/CompanyF/pipe.pkl','rb'))
df = pickle.load(open('C:/Users/Appu/Desktop/Streamlit Test/Best Code Streamlit/Z Test Programs/1000 companies/CompanyF/df.pkl','rb'))


def Loan_prediction(input_data) :
    # changing input data into numpy array
    input_data_as_numpy_Array = np.array(input_data,dtype=object)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_Array.reshape(1, -1)
    prediction = pipe.predict(input_data_reshaped)
    return prediction

def main():
    st.title("Company Profit")
    
    try:
        
        Research = st.number_input('R&D Spend')                         
        Administration = st.number_input('Administration')                                        
        Marketing = st.number_input('Marketing')                             
        #State = st.selectbox('State',df['State'].unique())
        State = st.selectbox("State",('California', 'Florida','New York'))
        
        if (State == 'Florida'):
            Florida = 1
            NewYork= 0
            
        elif (State == 'NewYork'):
            Florida = 0
            NewYork= 1
            
        else:
            Florida = 0
            NewYork= 0
            
        
        if st.button('Predict Price'):
            
            prediction = Loan_prediction([
                Research,
                Administration,
                Marketing,
                NewYork,
                Florida
                
            ])
            
            output = round(prediction[0], 2)
            
            st.write(output)
            
            
    except Exception as e:
        st.text(e)
             
    
        
 
if __name__ == '__main__':
    main()
 
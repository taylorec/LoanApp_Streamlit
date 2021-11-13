# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 21:52:41 2021

@author: evan
"""

import streamlit as st
import joblib

st.title('Loan Application Predictor')
st.write("This app predicts whether or not the borrower will default on the loan if approved.")

loaded_logr = joblib.load('logmodle.joblib')

credit_policy = st.selectbox('Credit Policy - meets the credit underwriting', options=['No', 'Yes'])
int_rate = st.number_input('Interest Rate', min_value=0.05)
installment = st.number_input('Monthly installments', min_value=10.00)
log_annual_inc = st.number_input('The natural log of the self-reported annual income', min_value=5.00)
dti = st.number_input('Debt-to-income ratio', min_value=0.00)
fico = st.number_input('FICO', min_value=500)
daysCrLine = st.number_input('Number of days with a credit line', min_value=175)
revolBal = st.number_input('Revolving balance', min_value=0.00)
revolUtil = st.number_input('Revolving line utilization rate', min_value=0.00)
inqLast6mo = st.number_input('Number of inquiries by creditors in the last 6 months', min_value=0)
delinq2yr = st.number_input('Number of times 30+ days past due payment', min_value=0)
pub_rec = st.number_input('Number of derogatory public records', min_value=0)
Loan_Purpose = st.selectbox('Loan purpose', options=[
       'purpose_all_other', 'purpose_credit_card',
       'purpose_debt_consolidation', 'purpose_educational',
       'purpose_home_improvement', 'purpose_major_purchase',
       'purpose_small_business'])
purpose_all_other = 0
purpose_credit_card = 0
purpose_debt_consolidation = 0
purpose_educational = 0
purpose_home_improvement = 0 
purpose_major_purchase = 0
purpose_small_business = 0
if Loan_Purpose == 'purpose_all_other':
    purpose_all_other = 1
elif Loan_Purpose == 'Credit card':
    purpose_credit_card = 1 # This variable is the dropped variable from the prediction
elif Loan_Purpose == 'Debt consolidation':
    purpose_debt_consolidation = 1
elif Loan_Purpose == 'Educational':
    purpose_educational = 1
elif Loan_Purpose == 'Home improvement':
    purpose_home_improvement = 1
elif Loan_Purpose == 'Major purchase':
    purpose_major_purchase = 1
elif Loan_Purpose == 'Small business':
    purpose_small_business = 1
if credit_policy == 'No':
    credit_policy = 0
elif credit_policy == 'Yes':
    credit_policy = 1

new_prediction = loaded_logr.predict([[credit_policy, int_rate, installment, log_annual_inc, dti,
       fico, daysCrLine, revolBal, revolUtil,
       inqLast6mo, delinq2yr, pub_rec, purpose_credit_card, purpose_debt_consolidation,
       purpose_educational, purpose_home_improvement,
       purpose_major_purchase, purpose_small_business]])
if new_prediction == 0:
    prediction = 'No, this model predicts the loan to be paid in full.'
else: prediction = 'Yes, this model predicts the borroer to default'
st.write('Does the model predict this loan to default: {}'.format(prediction))


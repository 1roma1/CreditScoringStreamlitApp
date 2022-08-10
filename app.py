import requests
import streamlit as st 

st.title("Credit Scoring")
st.image("img.jpg")

with st.form(key='columns_in_form'):
    cols = st.columns(3)
    Age = cols[0].number_input('Age', min_value=0, max_value=100, step=1)
    DebtRatio = cols[1].number_input('DebtRatio', min_value=0.0, max_value=4000.0, step=0.001)
    MonthlyIncome = cols[2].number_input('Monthly Income', min_value=0, max_value=10000000, step=1)

    cols = st.columns(3)
    NumberOfOpenCreditLinesAndLoans = cols[0].number_input('Number Of Open Credit Lines And Loans', min_value=0, max_value=100, step=1)
    NumberOfTime60_89DaysPastDue = cols[1].number_input('Number Of Time 60-89 Days Past Due', min_value=0, max_value=30, step=1)
    NumberOfTime30_59DaysPastDue = cols[2].number_input('Number Of Time 30-59 Days Past Due', min_value=0, max_value=30, step=1)

    cols = st.columns(3)
    NumberOfDependents = cols[0].number_input('Number Of Dependents', min_value=0, max_value=30, step=1)
    NumberOfTimes90DaysLate = cols[1].number_input('Number Of Times 90 Days Late', min_value=0, max_value=30, step=1)
    NumberRealEstateLoansOrLines = cols[2].number_input('Number Real Estate Loans Or Lines', min_value=0, max_value=30, step=1)
    

    cols = st.columns(3)
    RevolvingUtilizationOfUnsecuredLines = cols[0].number_input('Revolving Utilization Of Unsecured Lines', min_value=0, max_value=100000, step=1)

    cols = st.columns(2)
    submitted = cols[0].form_submit_button('Get Result')
    result_text = cols[1]

    if submitted:
        data = {
            "RevolvingUtilizationOfUnsecuredLines": RevolvingUtilizationOfUnsecuredLines,
            "age": Age,
            "NumberOfTime30_59DaysPastDueNotWorse": NumberOfTime30_59DaysPastDue,
            "DebtRatio": DebtRatio, 
            "MonthlyIncome": MonthlyIncome, 
            "NumberOfOpenCreditLinesAndLoans": NumberOfOpenCreditLinesAndLoans, 
            "NumberOfTimes90DaysLate": NumberOfTimes90DaysLate, 
            "NumberRealEstateLoansOrLines": NumberRealEstateLoansOrLines, 
            "NumberOfTime60_89DaysPastDueNotWorse": NumberOfTime60_89DaysPastDue, 
            "NumberOfDependents": NumberOfDependents
        }
        resp = requests.post("http://simple-credit-scoring.herokuapp.com/predict", json=data)
        result = resp.json()['result']

        
        if result == 0:
            text = '<p style="font-family:sans-serif; color:Green; font-size: 24px;">Not default</p>'
        else:
            text = '<p style="font-family:sans-serif; color:Red; font-size: 24px;">Default</p>'
        result_text.markdown(text, unsafe_allow_html=True)

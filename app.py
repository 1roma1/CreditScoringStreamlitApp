import requests
import streamlit as st 

st.title("Credit Scoring")
st.image("img.jpg")

with st.form(key='columns_in_form'):
    cols = st.columns(3)
    age = cols[0].number_input('Age', min_value=0, max_value=100, step=1)
    education = cols[1].selectbox('Education',
                      ('ACD', 'GRD', 'PGR', 'SCH', 'UGR'))
    sex = cols[2].selectbox('Sex', (0, 1))

    cols = st.columns(3)
    car = cols[0].selectbox('Car', (0, 1))
    car_type = cols[1].selectbox('Car type', (0, 1))
    decline_app_cnt = cols[2].number_input('Decline application count', min_value=0, max_value=100, step=1)

    cols = st.columns(3)
    good_work = cols[0].selectbox('Good work', (0, 1))
    score_bki = cols[1].number_input('Score BKI', min_value=-4.0, max_value=2.0, step=0.001)
    bki_request_cnt = cols[2].number_input('BKI request count', min_value=0, max_value=100, step=1)
    

    cols = st.columns(3)
    region_rating = cols[0].number_input('Region rating', min_value=0, max_value=100, step=5)
    income = cols[1].number_input('Income', min_value=0, max_value=1000000, step=100)
    sna = cols[2].number_input('SNA', min_value=0, max_value=10, step=1)

    cols = st.columns(3)
    first_time = cols[0].selectbox('First time', (0, 1))
    foreign_passport = cols[1].selectbox('Foreign passport', (0, 1))

    cols = st.columns(2)
    submitted = cols[0].form_submit_button('Get Result')
    result_text = cols[1]

    if submitted:
        data = {
            "education": education, 
            "sex": sex, 
            "age": age, 
            "car": car, 
            "car_type": car_type, 
            "decline_app_cnt": decline_app_cnt, 
            "good_work": good_work,
            "score_bki": score_bki, 
            "bki_request_cnt": bki_request_cnt, 
            "region_rating": region_rating,
            "income": income, 
            "sna": sna, 
            "first_time": first_time, 
            "foreign_passport": foreign_passport
        }
        resp = requests.post("https://model-predict-api.onrender.com/credit_scoring/predict", json=data)
        result = resp.json()['default']

        if result == 0:
            text = '<p style="font-family:sans-serif; color:Green; font-size: 24px;">Not default</p>'
        else:
            text = '<p style="font-family:sans-serif; color:Red; font-size: 24px;">Default</p>'
        result_text.markdown(text, unsafe_allow_html=True)



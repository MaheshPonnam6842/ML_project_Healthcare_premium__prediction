import streamlit as st

from prediction_helper import predict
st.title('Healthcare premium prediction')

categorical_option ={'Gender':['Female','Male'],
'Region':['Northwest','Southeast','Southwest','Northeast'],
'Marital Status' :['Unmarried','Married'],
'BMI Category':['Underweight','Normal','Overweight','Obesity'],
'Smoking Status':['No Smoking','Regular','Occasional'],
'Employment Status':['Freelancer','Salaried','Self-Employed'],
'income_level':['<10L','> 40L','10L - 25L','25L - 40L'],
'Medical History':['No Disease','High blood pressure','Diabetes & High blood pressure','Diabetes & Heart disease','Diabetes',
'Diabetes & Thyroid','Heart disease','Thyroid','High blood pressure & Heart disease'],
'Insurance Plan':['Silver','Bronze','Gold']}


row1 =st.columns(3)
row2 =st.columns(3)
row3 =st.columns(3)
row4 =st.columns(3)


with row1[0]:
   age=st.number_input('Age',min_value=18,max_value=100,step=1)
with row1[1]:
   number_of_dependants=st.number_input('Number of Dependents',min_value=0,max_value=20,step=1)
with row1[2]:
   income_lakhs=st.number_input('Income in Lakhs',min_value=0,max_value=500,step=1)

with row2[0]:
     genetical_risk=st.number_input('Genetical Risk',min_value=0,max_value=25,step=1)
with row2[1]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_option['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('Employment Status', categorical_option['Employment Status'])

with row3[0]:
    gender = st.selectbox('Gender', categorical_option['Gender'])
with row3[1]:
    marital_status = st.selectbox('Marital Status', categorical_option['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('BMI Category', categorical_option['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('Smoking Status', categorical_option['Smoking Status'])
with row4[1]:
    region = st.selectbox('Region', categorical_option['Region'])
with row4[2]:
    medical_history = st.selectbox('Medical History', categorical_option['Medical History'])


input_dict= {'Age':age,
             'Number of Dependents':number_of_dependants,
             'Income in Lakhs':income_lakhs,
             'Genetical Risk':genetical_risk,
             'Insurance Plan':insurance_plan,
             'Employment Status':employment_status,
             'Gender':gender,
             'Marital Status':marital_status,
             'BMI Category':bmi_category,
             'Smoking Status':smoking_status,
             'Region':region,
             'Medical History':medical_history}


if st.button('predict'):
    prediction=predict(input_dict)
    st.success(f'Predicted Insurance amount{prediction}')


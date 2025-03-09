import pandas as pd
import joblib
from joblib import load

model_rest=joblib.load('Artifacts/model_rest.joblib')
model_young=joblib.load('Artifacts/model_young.joblib')
scaler_rest =joblib.load('Artifacts/scaler_rest.joblib')
scaler_young=joblib.load('Artifacts/scaler_young.joblib')


def total_risk_score(medical_history):
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0}
    diseases=medical_history.lower().split('&')
    total_risk_scores=sum(risk_scores.get(disease,0) for disease in diseases)
    return total_risk_scores


def preprocess_input(input_dict):
    expected_columns=['age', 'number_of_dependants', 'income_lakhs', 'insurance_plan',
       'genetical_risk', 'total_risk_score', 'gender_Male', 'region_Northwest',
       'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
       'bmi_category_Obesity', 'bmi_category_Overweight',
       'bmi_category_Underweight', 'smoking_status_Occasional',
       'smoking_status_Regular', 'employment_status_Salaried',
       'employment_status_Self-Employed']
    df=pd.DataFrame(0,columns=expected_columns,index=[0])
    for key,value in input_dict.items():
        if key=='Insurance Plan':
            if value=='Bronze':
                df['insurance_plan']=1
            elif value=='Silver':
                df['insurance_plan']=2
            elif value=='Gold':
                df['insurance_plan']=3
        elif key=='Gender' and value=='Male':
            df['gender_Male']=1
        elif key== 'Region':
            if value=='Northwest':
                df['region_Northwest']=1
            elif value=='Southeast':
                df['region_Southeast']=1
            elif value=='Southwest':
                df['region_Southwest']=1
        elif key=='Marital Status' and value=='Unmarried':
            df['marital_status_Unmarried']=1
        elif key=='BMI Category':
            if value=='Underweight':
                df['bmi_category_Underweight']=1
            elif value=='Obesity':
                df['bmi_category_Obesity']=1
            elif value=='Overweight':
                df['bmi_category_Obesity']=1
        elif key=='Smoking Status':
            if value=='Regular':
                df['smoking_status_Regular']=1
            elif value=='Occasional':
                df['smoking_status_Occasional']=1
        elif key=='Employment Status':
            if value=='Salaried':
                df['employment_status_Salaried']=1
            elif value=='Self-Employed':
                df['employment_status_Self-Employed']=1

        elif key=='Age':
            df['age']=value
        elif key=='Number of Dependents':
            df['number_of_dependants']=value
        elif key=='Income in Lakhs':
            df['income_lakhs']=value
        elif key=='Genetical Risk':
            df['genetical_risk']=value
    df['total_risk_score']=total_risk_score(input_dict['Medical History'])
    df=handle_scaling(input_dict['Age'],df)
    return df
def handle_scaling(age,df):
    if age<=25:
        scaler_object=scaler_young
    else:
        scaler_object=scaler_rest
    cols_to_scale=scaler_object['cols_to_scale']
    scaler=scaler_object['scaler']

    df['income_level']=None
    df[cols_to_scale]=scaler.transform(df[cols_to_scale])
    df.drop('income_level',axis=1,inplace=True)

    return df


def predict(input_dict):
    input_df=preprocess_input(input_dict)
    if input_dict['Age']<=25:
        prediction=model_young.predict(input_df)
    else:
        prediction=model_rest.predict(input_df)

    return int(prediction[0])


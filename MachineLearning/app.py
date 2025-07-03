import streamlit as st
import pickle
# Load the pre-trained model    
model = pickle.load(open('model.pkl', 'rb'))
st.title('Insurance Premium Predication App')
print('SpringBoot')

age = int(st.text_input("Enter age: "))
gender = st.text_input('Enter gender:')
gender = 0 if gender=='male' else 1
bmi = float(st.text_input("Enter bmi: "))
children = int(st.text_input("Enter number of children: "))
smoker = st.text_input('Are you a smoker? (yes/no): ')
smoker = 1 if smoker.lower() == 'yes' else 0

X_test = [[age,gender,bmi,children,smoker]]
model.predict(X_test)[0]
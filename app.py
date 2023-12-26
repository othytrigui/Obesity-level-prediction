import pickle
import numpy as np
import streamlit as st

# Load the model from disk
filename = 'final_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))
obesity_mapping = {0: 'Insufficient Weight', 1: 'Normal Weight', 2: 'Obesity Type I', 3: 'Obesity Type II', 4: 'Obesity Type III', 5: 'Overweight Level I', 6: 'Overweight Level II'}

mappings = {
    "Gender": {'Female': 0, 'Male': 1},
    "family_history_with_overweight": {'No': 0, 'Yes': 1},
    "FAVC": {'No': 0, 'Yes': 1},
    "CAEC": {'Always': 0, 'Frequently': 1, 'Sometimes': 2, 'No': 3},
    "SMOKE": {'No': 0, 'Yes': 1},
    "SCC": {'No': 0, 'Yes': 1},
    "TUE": {"Low": 0, "Medium": 1, "High": 2},
    "CALC": {'Always': 0, 'Frequently': 1, 'Sometimes': 2, 'Never': 3},
    "MTRANS": {'Automobile': 0, 'Bike': 1, 'Motorbike': 2, 'Public Transportation': 3, 'Walking': 4}
}

# Interface Streamlit
image_url = "image3.png"
st.image(image_url, caption="", use_column_width=True)

# Adjust the space between the image and the title
st.markdown("<style>div.Widget.row-widget.stRadio>div{flex-direction:column;height: 100vh;margin: 0;display: flex;align-items: center;justify-content: center;}</style>", unsafe_allow_html=True)

st.title("How healthy are you?")
long_text = """
Health is a fundamental aspect of our lives, influencing our overall well-being and 
quality of life. It encompasses physical, mental, and social dimensions, and 
maintaining good health is essential for a fulfilling and productive life. Obesity, a 
complex and multifaceted health issue, is influenced by various factors that extend 
beyond simple caloric intake and physical activity. Lifestyle choices, such as smoking
habits, meal portion sizes (CAEC), frequency of consumption of high-calorie food (FCVC), 
and family history with overweight, all play critical roles in the development of obesity.
Additionally, factors like nutritional habits (NCP), consumption of high-calorie snacks 
(FAVC), and even demographic variables such as gender contribute to the intricate web of 
influences on obesity.
"""

st.markdown(f'<div style="text-align: justify">{long_text}</div>', unsafe_allow_html=True)

with st.sidebar:
    st.title("Complete the form to determine your obesity level!")
    # Form inputs
    gender = st.radio("Gender", ["Male", "Female"], key='genre')
    age = st.number_input("Age", min_value=1, max_value=120, step=1, key='age')
    height = st.number_input("Height (in meters)", min_value=1.0, max_value=5.0, step=0.1, key='height')
    weight = st.number_input("Weight (in KG)", min_value=1, max_value=300, step=1, key='weight')
    fhwo = st.radio("Has a family member experienced or is currently experiencing overweight?", ["Yes", "No"], key='fhwo')
    favc = st.radio("Do you eat high caloric food frequently?", ["Yes", "No"], key='favc')
    fcvc = st.slider("What percentage of your meals typically include vegetables?", min_value=0, max_value=100, value=50, format="%d%%", step=1, key='fcvc')
    ncp = st.slider('How many main meals do you have daily?', 1, 4, 2, key='ncp')
    caec = st.selectbox("Do you eat any food between meals?", ('Always', 'Frequently', 'Sometimes', 'No'), key='caec')
    smoke = st.radio("Do you smoke?", ["Yes", "No"], key='smoke')
    ch2o = st.slider('How much water do you drink daily? (in liters)', 0.0, 5.0, 1.0, 0.5, '%.2f', key='ch2o')
    scc = st.radio("Do you monitor the calories you eat daily?", ["Yes", "No"], key='scc')
    faf = st.number_input("How often do you have physical activity? (in a week)", min_value=0, max_value=7, step=1, key='faf')
    tue = st.selectbox('How would you categorize your usage of technological devices such as cell phones, television, computers, and others?', ["Low", "Medium", "High"], key='tue')
    calc = st.selectbox("How often do you drink alcohol?", ('Never', 'Sometimes', 'Frequently', 'Always'), key='calc')
    mTransp = st.selectbox("Which transportation do you usually use?", ('Walking', 'Bike', 'Public Transportation', 'Automobile', 'Motorbike'), key='mTransp')
    # Add a submit button at the end of the form
    if st.button("Submit"):

        gender = mappings["Gender"][gender]
        fhwo = mappings["family_history_with_overweight"][fhwo]
        favc = mappings["FAVC"][favc]
        fcvc = 1 + 2 * (fcvc / 100.0)
        caec = mappings["CAEC"][caec]
        smoke = mappings["SMOKE"][smoke]
        scc = mappings["SCC"][scc]
        tue = mappings["TUE"][tue]
        calc = mappings["CALC"][calc]
        mTransp = mappings["MTRANS"][mTransp]

        # Create a numpy array with user inputs
        user_input = np.array([[gender, age, height, weight, fhwo, favc, fcvc, ncp, caec, smoke, ch2o, scc, faf, tue, calc, mTransp]])

        # Make prediction
        prediction = loaded_model.predict(user_input)
        
        st.subheader("Prediction result:")
        st.write(f"The predicted obesity level is: {obesity_mapping.get(prediction[0])}")









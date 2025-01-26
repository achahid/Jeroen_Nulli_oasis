import streamlit as st
import numpy as np



def calculate_probability(inputs, intercept):
    logit = intercept + sum(inputs.values())
    probability = 1 / (1 + np.exp(-logit))
    return probability


# Button to choose between "Spontaneous vaginal delivery" and "Instrumental delivery"


delivery_type = st.selectbox("Choose Delivery Type", ["Choose a model", "Spontaneous vaginal delivery", "Instrumental delivery"])

inputs = None
intercept_ = None

# Show input form only after a delivery type is selected
if delivery_type == "Choose a model":
    st.write("### Study Overview:")
    st.write("""
        This study aimed to develop and validate prediction models for Obstetric Anal Sphincter Injury (OASI) in nulliparous women. The models focus on two types of deliveries:
        1. Spontaneous vaginal delivery
        2. Instrumental delivery

        **Population:** Data from the Netherlands Perinatal Registry was used, which includes records from 2016-2020. The study focused on nulliparous women who delivered a singleton live-born infant in cephalic presentation at term, either through spontaneous or operative vaginal delivery.
        """)
    st.write("**Like:** To be added in the future.")


else:
    if delivery_type == "Spontaneous vaginal delivery":
        st.header("Enter Predictor Values for Spontaneous Vaginal Delivery")
        # Add your model coefficients here (using the example coefficients you provided)

        # Collect input values (same form for both types of delivery)
        episiotomy = st.selectbox("Mediolateral Episiotomy (Yes/No)", ["Yes", "No"])
        fetal_weight = st.selectbox("Expected Fetal Birth Weight", ["< 3000 grams", "3000-3999 grams", "≥ 4000 grams"])
        duration_stage = st.selectbox("Duration of 2nd Stage of Labour",
                                      ["< 30 minutes", "30-59 minutes", "60-119 minutes", "≥ 120 minutes"])
        fetal_presentation = st.selectbox("Fetal Presentation", ["Occipito-anterior and other", "Occipitoposterior"])
        induction = st.selectbox("Induction of Labour", ["Yes", "No"])
        epidural = st.selectbox("Epidural Analgesia", ["Yes", "No"])
        race = st.selectbox("Maternal Race/Ethnicity", ["White European", "South Asian/other Asian", "Other Non-Western"])
        maternal_age = st.slider("Maternal Age (Years)", min_value=14, max_value=50, value=29)
        gestational_age = st.selectbox("Gestational Age (Weeks)", ["37", "38", "39", "40", "41", "42"])
        fetal_sex = st.selectbox("Fetal Sex", ["Boy", "Girl"])


        # Inputs for Spontaneous Vaginal Delivery
        inputs_spontaneous = {
            "Episiotomy": -1.162 if episiotomy == "Yes" else 0,
            "FetalWeight_<3000": -0.677 if fetal_weight == "< 3000 grams" else 0,
            "FetalWeight_3000-3999": 0 if fetal_weight == "3000-3999 grams" else 0,
            "FetalWeight_≥4000": 0.730 if fetal_weight == "≥ 4000 grams" else 0,
            "Duration_30-59": 0.192 if duration_stage == "30-59 minutes" else 0,
            "Duration_60-119": 0.290 if duration_stage == "60-119 minutes" else 0,
            "Duration_≥120": 0.169 if duration_stage == "≥ 120 minutes" else 0,
            "Occipitoposterior": 0.257 if fetal_presentation == "Occipitoposterior" else 0,
            "Induction": -0.142 if induction == "Yes" else 0,
            "Epidural": -0.353 if epidural == "Yes" else 0,
            "Race_SouthAsian": 0.636 if race == "South Asian/other Asian" else 0,
            "Race_NonWestern": 0.087 if race == "Other Non-Western" else 0,
            "MaternalAge": 0.021 * maternal_age,  # multiply age by coefficient
            "GestAge_37": -0.270 if gestational_age == "37" else 0,
            "GestAge_38": -0.174 if gestational_age == "38" else 0,
            "GestAge_39": -0.035 if gestational_age == "39" else 0,
            "GestAge_40": 0 if gestational_age == "40" else 0,
            "GestAge_41": -0.006 if gestational_age == "41" else 0,
            "GestAge_42": 0.002 if gestational_age == "42" else 0,
            "FetalSex_Boy": 0.058 if fetal_sex == "Boy" else 0,
        }


        inputs = inputs_spontaneous
        intercept_ = -3.605


        # Model input form for spontaneous vaginal delivery goes here
    elif delivery_type == "Instrumental delivery":
        st.header("Enter Predictor Values for Instrumental Delivery")


        # Collect input values (same form for both types of delivery)
        episiotomy = st.selectbox("Mediolateral Episiotomy (Yes/No)", ["Yes", "No"])
        fetal_weight = st.selectbox("Expected Fetal Birth Weight", ["< 3000 grams", "3000-3999 grams", "≥ 4000 grams"])
        duration_stage = st.selectbox("Duration of 2nd Stage of Labour",
                                      ["< 30 minutes", "30-59 minutes", "60-119 minutes", "≥ 120 minutes"])
        fetal_presentation = st.selectbox("Fetal Presentation", ["Occipito-anterior and other", "Occipitoposterior"])
        epidural = st.selectbox("Epidural Analgesia", ["Yes", "No"])
        race = st.selectbox("Maternal Race/Ethnicity", ["White European", "South Asian/other Asian", "Other Non-Western"])
        gestational_age = st.selectbox("Gestational Age (Weeks)", ["37", "38", "39", "40", "41", "42"])

        # Inputs for Operative Delivery (Instrumental delivery)
        inputs_operative = {
            "Episiotomy": -1.683 if episiotomy == "Yes" else 0,
            "FetalWeight_<3000": -0.577 if fetal_weight == "< 3000 grams" else 0,
            "FetalWeight_≥4000": 0.390 if fetal_weight == "≥ 4000 grams" else 0,
            "Duration_<30": 0 if duration_stage == "< 30 minutes" else 0,
            "Duration_30-59": 0.163 if duration_stage == "30-59 minutes" else 0,
            "Duration_60-119": 0.394 if duration_stage == "60-119 minutes" else 0,
            "Duration_≥120": 0.420 if duration_stage == "≥ 120 minutes" else 0,
            "Occipitoposterior": 0.602 if fetal_presentation == "Occipitoposterior" else 0,
            "Epidural": -0.193 if epidural == "Yes" else 0,
            "Race_SouthAsian": 0.591 if race == "South Asian/other Asian" else 0,
            "Race_NonWestern": 0.064 if race == "Other Non-Western" else 0,
            "GestAge_37": -0.436 if gestational_age == "37" else 0,
            "GestAge_38": -0.0543 if gestational_age == "38" else 0,
            "GestAge_39": 0.028 if gestational_age == "39" else 0,
            "GestAge_40": 0 if gestational_age == "40" else 0,
            "GestAge_41": 0.082 if gestational_age == "41" else 0,
            "GestAge_42": 0.186 if gestational_age == "42" else 0,
        }

        inputs = inputs_operative
        intercept_ = -2.270

# Calculate and display the predicted probability
if st.button("Predict Probability"):
    if delivery_type == "Choose a model":
        st.warning("Please select a model to proceed.")
    else:
        # st.write(f"Assigned Inputs: {inputs}")
        # st.write(f"Assigned Betas: {betas}")


        probability=calculate_probability(inputs, intercept_)
        st.success(f"The predicted probability of OASI is: {probability:.4f}")

# Place Contact Information at the bottom with styling

# Spacer to push contact to bottom
# Use a container to push contact to bottom
spacer = st.container()

# Footer container
footer = st.container()
with footer:
    st.markdown("---")
    if st.button('Contact'):
        st.markdown("""
        ### Contact Information
    
        **Article Inquiries:**
        - Email: contact@example.com 
    
        **Application Support:**
        - Technical Support: ch_abdelhak@hotmail.com
 
        """)

import pickle
import streamlit as st
import numpy as np

model = pickle.load(open('finalized_model.sav', 'rb'))

st.title('HAND GRIP STRENGTH ANALYSIS')

st.write('This is a machine learning web app to predict the hand grip strength of a person')

st.write('Please enter the following details')

# in_x = [ 'Gender (M/F)', 'Age (years)', 'Medicin (n)',
#        'Smokingstatus (Yes=1, No=2, previously=3)', 'Packyears',
#        'Activitylevel work (1-4)', 'Activitylevel sparetime (1-4)', 'B1SD',
#        'B1SND', 'B1EAD', 'B1EAND', 'B2BS', 'B2BAE', 'B2SS', 'B2SEA', 'SHD',
#        'SHND', 'S1D', 'S1ND', 'RHD', 'RHND', 'RFD', 'RFND',]

Gender = st.selectbox('Gender (M/F)', ['M', 'F'])
if Gender == 'M':
    Gender = 1
else:
    Gender = 2
Age = st.number_input('Age (years)')
Medicine = st.number_input('Medicine (n)')
Somkingstatus = st.selectbox(
    'Somkingstatus (Yes=1, No=2, previously=3)', ['1', '2', '3'])
Packyears = st.number_input('Packyears')
Activitylevelwork = st.selectbox(
    'Activitylevel work (1-4)', ['1', '2', '3', '4'])
Activitylevelsparetime = st.selectbox(
    'Activitylevel sparetime (1-4)', ['1', '2', '3', '4'])
B1SD = st.number_input('B1SD')
B1SND = st.number_input('B1SND')
B1EAD = st.number_input('B1EAD')
B1EAND = st.number_input('B1EAND')
B2BS = st.number_input('B2BS')
B2BAE = st.number_input('B2BAE')
B2SS = st.number_input('B2SS')
B2SEA = st.number_input('B2SEA')
SHD = st.number_input('SHD')
SHND = st.number_input('SHND')
S1D = st.number_input('S1D')
S1ND = st.number_input('S1ND')
RHD = st.number_input('RHD')
RHND = st.number_input('RHND')
RFD = st.number_input('RFD')
RFND = st.number_input('RFND')

data = np.array([Gender, Age, Medicine, Somkingstatus, Packyears,
                Activitylevelwork, Activitylevelsparetime, B1SD, B1SND, B1EAD, B1EAND, B2BS, B2BAE, B2SS, B2SEA, SHD,
                SHND, S1D, S1ND, RHD, RHND, RFD, RFND])
data = data.reshape(1, -1)
out = model.predict(data)

# out = model.predict([1,1,84,8.0,3,18.0,1.0,14.564388275146484,36.887102127075195,29.967077255249023,151.35318756103516,17.891121864318848,16.6898832321167,132.53414154052734,144.6554718017578,701.6666666666666,780.3333333333334,1009.0,962.6666666666666])
if st.button('Predict'):
    if out == 0:
        st.write('The predicted health status is', 'Healthy')
    else:
        st.write('The predicted health status is', 'UnHealthy')
        
    
import streamlit as st

st.title('First app')
st.write('Enetr a number to claculate its square and cube')

n = st.number_input('Enter a number', value=1, step=1)
# where value is the default value: in simple words it is the value which is shown in the input box
# step is the step size: in simple words it is the value which is shown in the input box

st.write('The square of', n, 'is', n*n)
st.write('The cube of', n, 'is', n*n*n)

# To run this app: streamlit run first_app.py
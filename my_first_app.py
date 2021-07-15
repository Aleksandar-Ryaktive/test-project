import streamlit as st

st.write("""
         # My first app
         
         Hello Ryaktivers,
         
         This is my very first app deployment made in Streamlit.
         
         Here is something you can test to see how it works:
         """)

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)



st.title('Doublecheck')

st.text('Type a number in the box below')

n = st.number_input('Number', step=1)

st.write(f'{n} * {n} = {n*n}')

s = st.text_input('Type a name in the box below')



st.write(f'Cheers, {s}')
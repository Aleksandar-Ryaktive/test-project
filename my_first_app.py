import streamlit as st

st.write("""
         # My first app
         
         Hello Ryaktivers,
         
         This is my very first app deployment made in Streamlit.
         
         Here is something you can test how it works:
         """)

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)


st.write("""
         Cheers,
         Aleksandar
         """)

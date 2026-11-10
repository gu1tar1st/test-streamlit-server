# run command: streamlit run <file_name.py>

import streamlit as st
import time
from PIL import Image

st.title(
    "ML Model Deployed w/ Streamlit"
)

st.header("Header: Introduction")
st.subheader("Subheader: Part 1")

# read
st.text("Text: this is a text")
# write
user_input = st.text_input(
    "A box of input", 
    placeholder='Type something here :)', 
    max_chars=10
)
st.text(f"You have typed: {user_input}")
user_input = st.text_area(
    "A bigger input box for you",
    placeholder="Type here"
)
st.text(f"You typed: {user_input}")

# markdown
st.markdown("A __super important__ piece of text")

# button
if "clicked" not in st.session_state:
    st.session_state['clicked'] = False
if st.button("Click me"):
    st.session_state['clicked'] = not st.session_state['clicked']
if st.session_state['clicked']:
    st.text('You clicked it!')
    st.info('You clicked it!')
    st.warning('You clicked it!')
    st.error('You clicked it!')
    st.toast('You clicked it!')

# image
st.image("https://images.stockcake.com/public/c/3/6/c3642e55-45ab-4010-904a-118e86e4db97/ethereal-mountain-sunset-stockcake.jpg")

# check box
flag = st.checkbox("Select me", key=1)
st.write(flag)
flag = st.checkbox("Select me", key=2)
st.write(flag)
flag = st.checkbox("Select me", key=3)
st.write(flag)
flag = st.checkbox("Select for image", key="image")
if flag:
    st.image("https://images.stockcake.com/public/c/3/6/c3642e55-45ab-4010-904a-118e86e4db97/ethereal-mountain-sunset-stockcake.jpg", width=100)

st.color_picker("Pick a color")

# radio button
selection = st.radio(
    label='Choose your ML model (radio for a few options)',
    options=['Astra', 'Fable', 'Grok', 'Gemini']
)
if selection:
    st.write(selection)

# select box
selection = st.selectbox(
    label='Choose your ML model (selectbox for lots of options)',
    options=['Astra', 'Fable', 'Grok', 'Gemini']
)
if selection:
    st.write(selection)
# multi select
selection = st.multiselect(
    label='Choose your ML model (multiselect for lots of options & multiple selection)',
    options=['Astra', 'Fable', 'Grok', 'Gemini']
)
if selection:
    st.write(selection)

# select a (range) of number
range = st.slider(
    "Number slider",
    min_value=0,
    max_value=100,
    value=(0, 100)    
)
if range:
    st.write(range)
level = st.select_slider(
    "Difficulty",
    options=["Easy", "Medium", "Hard"]
)
if level:
    st.write(level)

# spinner for download
with st.spinner("Downloading your model.."):
    time.sleep(20)
    st.write('Model downloaded')
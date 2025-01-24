# pip install -r .\requirements.txt
# pipreqs .
# This will create requirements.txt file at the current directory.

# test

import streamlit as st
import pandas as pd
import numpy as np



x = st.slider('Select a value: ')
st.write(f'{x} + 2 = {x+2}')


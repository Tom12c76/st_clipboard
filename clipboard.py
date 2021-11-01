import pandas as pd
import streamlit as st
from datetime import datetime
import glob
from io import StringIO

todo = st.radio('what do you want to do', ['save clipboard data to csv', 'download csv files'])

if todo == 'save clipboard data to csv':
    df = st.text_area('paste your data here')
    if st.button('read text area & save csv'):
        st.success('button pressed')
        df = pd.read_csv(StringIO(df), delimiter=";")
        st.write(df)
        now = datetime.now()
        file_name = f'{now:%Y-%m-%d %H-%M-%S} clipboard data.csv'
        df.to_csv(file_name, index=False)
        st.success(f'file has been saved with {file_name} name')

if todo == 'download csv files':
    list_csv = sorted(glob.glob('*.csv'), reverse=True)
    d_filename = st.selectbox('Choose a file', options=list_csv)
    df = pd.read_csv(d_filename)
    st.write(df)
    st.download_button('download now', data=df.to_csv(index=False), file_name=d_filename, mime='text/csv')
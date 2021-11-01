import pandas as pd
import streamlit as st
from datetime import datetime
import glob

todo = st.radio('what do you want to do', ['save clipboard data to csv', 'download csv files'])

if todo == 'save clipboard data to csv':
    if st.button('read clipboard & save csv'):
        try:
            df = pd.read_clipboard()
            st.write(df)
            now = datetime.now()
            file_name = f'{now:%Y-%m-%d %H-%M-%S} clipboard data.csv'
            df.to_csv(file_name, index=False)
            st.success(f'file has been saved with {file_name} name')
        except:
            st.error('clipboard empty or error with data')

if todo == 'download csv files':
    list_csv = sorted(glob.glob('*.csv'), reverse=True)
    d_filename = st.selectbox('Choose a file', options=list_csv)
    df = pd.read_csv(d_filename)
    st.write(df)
    st.download_button('dwnload now', data=df.to_csv(index=False), file_name=d_filename, mime='text/csv')

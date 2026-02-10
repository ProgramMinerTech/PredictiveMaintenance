import streamlit as st
import pandas as pd
import numpy as np

class Welc:
    def show(self):
        st.header('WELCOME !!!')
        st.write('Welcome to my dashboard of Predictive Maintenance Project.')
        st.write('The Predictive Maintenance project focuses on applying machine' \
        ' learning techniques to predict equipment failures before they occur, enabling ' \
        'optimized maintenance and reducing unplanned downtime. This is particularly valuable'
        ' in manufacturing industries, where unexpected machine failures can lead to high ' \
        'costs and production losses.')
        st.write('The AI4I 2020 Predictive Maintenance Dataset from Kaggle is a ' \
        'synthetic yet representative dataset that contains sensor measurements, ' \
        'operational conditions, and failure labels. It includes around 10,000' \
        ' records with 14 features, such as temperature, rotational speed, torque, tool ' \
        'wear, and a binary machine failure label.')
        st.write('The main objectives of this project are:')
        st.markdown("""
        1. Explore and clean the dataset to understand variable behavior.
        2. Develop and evaluate machine learning models to anticipate equipment failures.
        3. Visualize results and key metrics to assess model performance.
        """)
        st.write('This approach not only improves operational efficiency but also ' \
        'demonstrates how artificial intelligence can be integrated into real industrial ' \
        'processes to make proactive decisions.')


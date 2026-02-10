import pandas as pd
import streamlit as st
from pathlib import Path

class VData:
    def show(self):
        st.subheader('Dataset')
        st.write('Now, I describe all features about the datasets an the content of this featrues.')
        base_dir = Path(__file__).parents[2]
        file = (base_dir / 'data' / 'raw' / 'data.csv').resolve()
        ndata = pd.read_csv(file)
        st.dataframe(ndata.head())

        st.markdown("""
            1. **UID**: Unique identifier ranging from 1 to 10000.
            2. **Product ID**: Consisting of a letter L, M, or H for low 
                    (50% of all products), medium (30%) and high (20%) as product 
                    quality variants and a variant-specific serial number.
            3. **Type**: Just the product type L, M or H from column 2.
            4. **Air Temperature [K]**: 
        """)

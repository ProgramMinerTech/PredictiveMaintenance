import streamlit as st
from sections.welcome import Welc
from sections.data import VData

class Dashboard:
    def __init__(self):
        self.menu_op = ['Welcome', 'Data', 'EDA']

    def run(self):
        st.title('Predictive Maintenance Project')
        option = st.sidebar.radio('MENU', self.menu_op)

        if option == 'Welcome':
            Welc().show()
        elif option == 'Data':
            VData().show()

if __name__ == '__main__':
    app = Dashboard()
    app.run()
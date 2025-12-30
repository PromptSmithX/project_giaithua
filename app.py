import streamlit as st
import pandas as pd
from ham_tinh import fact

def main():
    st.title("Phần mềm tính toán giai thừa")
    number = st.number_input("Nhập số: ",min_value=0, max_value=900)

    if st.button("Enter"):
        result = fact(number)
        st.write(f'Kết quả giai thừa của số {number} là {result}')
main()


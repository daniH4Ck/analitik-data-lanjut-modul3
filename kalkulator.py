import streamlit as st

def kali(x1,x2):
    return x1*x2
def bagi(x1,x2):
    return x1/x2
def tambah(x1,x2):
    return x1+x2
def kurang(x1,x2):
    return x1-x2

option = st.selectbox(
    'Pilihan',
    ('x', '/', '-','+'))
angka1 = st.number_input('Insert a number1')
angka2 = st.number_input('Insert a number2')
if option == "x":
    st.write('The number is ', kali(angka1,angka2))
elif option == "/":
    st.write('The number is ', bagi(angka1,angka2))
elif option == "-":
    st.write('The number is ', kurang(angka1,angka2))
elif option == "+":
    st.write('The number is ', tambah(angka1,angka2))
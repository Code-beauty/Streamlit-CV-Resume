import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Tayyaba's CV")

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("profile-pic.png",width=230)
with col2:
    st.title("Tayyaba Shaikh")
    st.write("Undergraduate Telecommunication Engineer ")
    st.info("I am currently enrolled in BE Telecommunication 3rd Year and seeking  skills in AI and ML")
    st.write("📫", "shaikhtayyaba28@gmail.com")

# --- QUALIFICATIONS ---
st.write('\n')
st.subheader("Qualifications")
df = pd.DataFrame({
     'Year': ['2020-Current', '2019-2020', '2017'],
     'Degree/Certification': ['BE','Intermidiates', 'Matriculation'],
     'Field ': ['Telecommunications','Computer Science', 'Computer Science'],
     'Institute Name': ['Mehran University Jamshoro','F.G Girls Inter College KHI CANTT', 'F.G Public Girls School HYD CANTT'],
     })
st.write(df)


# --- EXPERIENCE ---
st.write('\n')
st.subheader("Experience")
st.write(
    """
- ✔️ Strong hands on experience and knowledge in Python and MS.Office 
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Numpy,Pandas), C/C++, Matlab 
- 📊 Data Visulization: MS Excel, Python

"""
)

# --- Contact Details ---
st.write('\n')
st.subheader("Contact Details")
st.write(
    """
- 📞 0000-0000000
- 📧 shaikhtayyaba28@gmail.com
- 📍  Karachi, Pakistan
"""
)

# --- Certifications ---
st.write('\n')
st.subheader("Certifications")
st.write(
    """
- Introduction to Machine Learning - Simplilearn
- Graphic Designing - NFTP
- Canva Basics to Advanced Training - LWS Academy
"""
)


# --- Honor And Awards ---
st.write('\n')
st.subheader("Honor And Awards")
st.write(
    """
- PSF-STFS Scholarship (2018-2020)
- Ehsaas Scholarship of Undergraduate Program (2020-2024)
"""
)

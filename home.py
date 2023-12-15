import streamlit as st

st.header("Star")
st.title('การทดสอบเขียนเว็บด้วย Python')
st.header('Panwarit Suriwan')
st.subheader('สาขาวิชาเทคโนโลยีสารสนเทศ')
st.markdown("----")

col1, col2 = st.columns(2)

# เพิ่มข้อความหรือข้อมูลเพิ่มเติมในแต่ละคอลัมน์
with col1:
    st.image('./pic/263829-qgdtri-1.n.jpg', width=200)

with col2:
    st.image('./pic/unnamed.jpg', width=200)
html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")
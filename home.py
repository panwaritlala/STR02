import streamlit as st

st.header("Star")
st.title('การทดสอบเขียนเว็บด้วย Python')
st.header('Panwarit Suriwan')
st.subheader('สาขาวิชาเทคโนโลยีสารสนเทศ')
st.markdown("----")

col1, col2 = st.columns(2)

# เพิ่มข้อความหรือข้อมูลเพิ่มเติมในแต่ละคอลัมน์
with col1:
    st.write("Column 1 Content")
    st.image('./pic/263829-qgdtri-1.n.jpg', width=200)

with col2:
    st.write("Column 2 Content")
    st.image('./pic/unnamed.jpg', width=200)

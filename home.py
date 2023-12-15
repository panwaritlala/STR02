import streamlit as st

st.header("star")
st.title('การทดสอบเขียนเว็บด้วย Python')
st.header('panwarit suriwan')
st.subheader('สาขาวิชาเทคโนโลยีสารสนเทศ')
st.markdown("----")
col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
    st.image('./pic/263829-qgdtri-1.n.jpg')
with col2:
    st.image('./pic/unnamed.jpg')
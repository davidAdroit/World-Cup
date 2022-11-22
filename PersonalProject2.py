import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title("David's Website")
st.header("World Cup Predictions")

tab1, tab2 = st.tabs(["Opinion", "Results of Matches"])
tab1.title("Opinion that lead to predictions of games")

tab2.title("Results of Games that already happened")
with tab1:
    st.subheader("Spain v Costa Rica")
    st.info("It's evident this will be a massive wipe in Spain's favor")
    st.subheader("US v England")
    st.info("I only predict US will win because im from the US")
    st.subheader("Brazil v Serbia")
    st.info("Brazil")


#with st.container():

   #st.write("This is inside the container")
   #st.write("Prediction for : Spain v Costa Rica ")

   #st.metric(label="Spain", value="WIN", delta="90%")
st.title("Future Predictions")
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Spain vs Costa Rica")
    st.success("Spain Win")
    st.metric(label="Spain", value="WIN", delta="90%")
with col2:
    st.header("USA vs England")
    st.success("USA WIN")
    st.metric(label="USA", value="WIN", delta = "50%")
with col3:
    st.header("Brazil vs Serbia")
    st.success("Brazil Win!")
    st.metric(label="Brazil", value = "WIN", delta = "99%")

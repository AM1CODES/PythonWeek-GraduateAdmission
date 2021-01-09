import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('new_model.pkl','rb'))


def main():
  st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>Graduate Admission Predictor</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center; color: Black;'>Drop in The required Inputs and we will do  the rest.</h3>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: center; color: Black;'>Submission for The Python Week</h4>", unsafe_allow_html=True)
  st.sidebar.header("What is this Project about?")
  st.sidebar.text("It a Web app that would help the user in determining whether they will get admission in a Graduate Program or not.")
  st.sidebar.header("What tools where used to make this?")
  st.sidebar.text("The Model was made using a dataset from Kaggle along with using Kaggle notebooks to train the model. We made use of Sci-Kit learn in order to make our Linear Regression Model.")



  cgpa = st.slider("Input Your CGPA",0.0,10.0)
  gre = st.slider("Input your GRE Score",0,340)
  toefl = st.slider("Input your TOEFL Score",0,120)
  research = st.slider("Do You have Research Experience (0 = NO, 1 = YES)",0,1)
  uni_rating = st.slider("Rating of the University you wish to get in on a Scale 1-5",1,5)

  inputs = [[cgpa,gre,toefl,research,uni_rating]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(float)
    st.success('The Probability of getting admission is {}'.format(updated_res))


if __name__ =='__main__':
  main()
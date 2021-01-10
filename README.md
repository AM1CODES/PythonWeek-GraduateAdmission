<p align="center">
<img src="https://github.com/AM1CODES/PythonWeek-GraduateAdmission/blob/main/pyweek.png" alt="drawing" width="500"/>
</p>

# PythonWeek-GraduateAdmission
Students all across the world go through a phase where they have to make a decision whether they wish to study further in order to gain in-dept knowledge about the stuff in their field or whether they start working. Well that depends on an individual and what he/she wishes to do but if you are someone who wishes to pursue further studies, this project might help you out.

# What is the Project about?
It is a web-app that makes use of Machine learning inorder to determine whether a student will be able to get into a Graduate Admission based on metrics such as their GRE scores, TOEFL scores, their CGPA and other relevant stuff.

# What did we use to build it?
<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/pandas%20-%23150458.svg?&style=for-the-badge&logo=pandas&logoColor=white" />  <img src="https://img.shields.io/badge/numpy%20-%23013243.svg?&style=for-the-badge&logo=numpy&logoColor=white" /> <img src="https://img.shields.io/badge/Jupyter%20-%23F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white" /> <br>


 
The primary language for modeling and data analysis was Python. We made use of Sci-Kit learn library in order to make our model which is a linear regression model. We made use of Libraries like Matplotlib and Seaborn for visualizing our data.


# About the Data-set
I used a data set off of Kaggle. It contained data of real students and their GRE scores, TOEFL scores and other relevant data which is important during Admission in any Graduate Program.

# How was the project built?
1. I started off by getting the data from Kaggle and used the Kaggle notebooks to  create the model. After importing the data i looked at the different columns in our data. <br>
2. I then visualized the various columns of our data using various graphs in order to determine the columns that i wished to use to make our model. <br>
3. Once i had my columns, i split the data into training and testing set using the train-test split and made my Linear Regression model using the Sci-Kit learn Library. <br>
4. Once the model was ready, i put it in a pickle file. <br>
5. I then shifted to Colab Notebook where i deployed the model on web  using PyNgrok and Streamlit. The front end of the Web app was all made using Stream lit and i then used Pyngrok to host it on web. <br>
6. In the end i tested the web app with the inputs from the test set that we created and the model gave results very close to the results we had in our original data. <br>

# Image Gallery
<p align="center">
<img src="https://github.com/AM1CODES/PythonWeek-GraduateAdmission/blob/main/Screenshot%20(125).png" alt="drawing" width="800"/>
</p>
<p align="center">
<img src="https://github.com/AM1CODES/PythonWeek-GraduateAdmission/blob/main/Screenshot%20(126).png" alt="drawing" width="800"/>
</p>

# Conclusion
The model was able to make some very good predictions. The model accuracy was somewhere around 94-95% which is quite decent and even on the data which the model had never seen before, it was able to make some good predictions.

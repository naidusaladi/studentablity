import streamlit as st
import pickle 



dic1={'Gabriel Pereira':0, 'Mousinho da Silveria':1}

dic3={'Female':0, 'Male':1}
dic4={'Urban':1,'Rural':0}
dic5={'<=3':1,'>3':0}
dic6={'Living Together':1, 'Apart':0}
dic7={'None':0, 'Primary(upto 4th)':1,'High School(5th to 9th)':2,"10+2":3,'Higher Education':4}
dic8={'Teacher':0, 'Health care realated':1,'Civil Services':2,'Other':3,'At Home':4}
dic9={'School Reputation':3,'Course preference':0,'Close to Home':4,'Other':2}
dic10={'Mother':1,'Father':0,'Other':2}
dic11={'<15min':1,'15-30min':2,'30-60min':3,'>60min':4}
dic12={'<2hrs':1,'2-5hrs':2,'5-10hrs':3,'>10hrs':4}
dic13={'0':0,'1':1,'2':2,'3':3,'more':4}
dic14={'True':1,'False':0}



st.title('Analysis and Prediction of Student Performace')

School = st.selectbox(
    
    'School',
    ('Gabriel Pereira', 'Mousinho da Silveria'))

st.write('You selected:', School)



Sex = st.selectbox(
    
    'Sex',
    ('Female', 'Male'))




#-------------------------- age (15-22)-----------------------------

age=st.number_input("Age", min_value=15, max_value=22)



Address = st.selectbox(
    
    'Address',
    ('Urban', 'Rural'))



Family_Size = st.selectbox(
    
    'Family Size',
    ('<=3', '>3'))



Pstatus = st.selectbox(
    
    "Parent's Cohabitation Status",
    ('Living Together', 'Apart'))

st.write('You selected:', Pstatus)

Medu = st.selectbox(
    
    "Mother's Education",
    ('None', 'Primary(upto 4th)','Highschool(5th to 9th)','10+2','Higher Education'))



Fedu = st.selectbox(
    
    "Father's Education",
    ('None', 'Primary(upto 4th)','Highschool(5th to 9th)','10+2','Higher Education'))




Mjob = st.selectbox(
    
    'Mother Job',
    ('Teacher', 'Health care realated','Civil Services','Other','At Home'))



Fjob = st.selectbox(
    
    'Father Job',
    ('Teacher', 'Health care realated','Civil Services','At Home','Other'))



reson = st.selectbox(
    
    'Reson to Choose this School',
    ( 'School Reputation','Course preference','Close to Home','Other'))




guardian  = st.selectbox(
    
    "Student's Guardian",
    ('Mother','Father','Other'))




traveltime  = st.selectbox(
    
    "Travel time(from home to school)",
    ('<15min','15-30min','30-60min','>60min'))




studytime  = st.selectbox(
    
    "Weekly Study Time",
    ('<2hrs','2-5hrs','5-10hrs','>10hrs'))




failures  = st.selectbox(
    
    "No.of past class failures",
    ('0','1','2','3','more'))




schoolsup  = st.selectbox(
    
    "Extra Educational Support",
    ('True','False'))




famsup = st.selectbox(
    
    "Family Educational Support",
    ('True','False'))



paid  = st.selectbox(
    
    "Extra Paid Classes Within The Course Subject ",
    ('True','False'))




activities = st.selectbox(
    
    "Extra-Curricular Activities ",
    ('True','False'))




nursery = st.selectbox(
    
    "Attended Nursery School",
    ('True','False'))



higher= st.selectbox(
    
    "Wants To Take Higher Education",
    ('True','False'))



internet = st.selectbox(
    
    "Internet Access At Home ",
    ('True','False'))



romantic = st.selectbox(
    
    "With A Romantic Relationship ",
    ('True','False'))
#--------famrel-----------------

famrel=st.number_input("Quality Of Family Relationships", min_value=1, max_value=5)

#-------freetime----------------

freetime=st.number_input("Free Time After School", min_value=1, max_value=5)

#-------goout------------------

goout=st.number_input("Go Out With Friends", min_value=1, max_value=5)

#-------dalc-------------------

dalc=st.number_input("Workday Alcohol Consumption", min_value=1, max_value=5)

#-------walc-----------------

walc=st.number_input("Weekend Alcohol Consumption", min_value=1, max_value=5)

#------health----------

health=st.number_input("Current Health Status", min_value=1, max_value=5)

#------absent---------

absences=st.number_input("No.of School Absences",min_value=0, max_value=32)

Algo = st.selectbox(
    
    "Select Algorithms ",
    ('Decision Trees','Support Vector Machie','Randomforest','KNN'))

dic_algo={'Decision Trees':0,'Support Vector Machie':1,'Randomforest':2,'KNN':3}
counter=dic_algo[Algo]
dec=pickle.load(open("decisiontree.sav",'rb'))
svm=pickle.load(open("svm.sav",'rb'))
random=pickle.load(open("randomforest.sav",'rb'))
knn=pickle.load(open("knn.sav",'rb'))
if st.button('Predict'):
    values=[dic1[School],dic3[Sex],age,dic4[Address],dic5[Family_Size],dic6[Pstatus],dic7[Medu],dic7[Fedu],dic8[Mjob],dic8[Fjob],dic9[reson]
            ,dic10[guardian],dic11[traveltime],dic12[studytime],dic13[failures],dic14[schoolsup],dic14[famsup],dic14[paid],dic14[activities],
            dic14[nursery],dic14[higher],dic14[internet],dic14[romantic],famrel,freetime,goout,dalc,walc,health,absences]
    
   
    pred1=dec.predict([values])
    pred2=svm.predict([values])
    pred3=random.predict([values])

    pred5=knn.predict([values])
    if counter==0:
        st.write("Decisointree:"+str(pred1[0]))
    if counter==1:
        st.write("Support Vector Machine:"+str(pred2[0]))
    if counter==2:
        st.write("Random Forest:"+str(pred3[0]))
    if counter==3:
        st.write("KNN:"+str(pred5[0]))
    
else:
    st.write('click above for prediction')







































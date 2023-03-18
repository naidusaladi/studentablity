import streamlit as st
import pickle 



dic1={'Gabriel Pereira':0, 'Mousinho da Silveria':1}
#dic2={'Mathmatics':0, 'Portuguese Language':1}
dic3={'Female':0, 'Male':1}
dic4={'Urban':1,'Rural':0}
dic5={'<=3':1,'>3':0}
dic6={'Living Together':1, 'Apart':0}
dic7={'None':0, 'Primary(upto 4th)':1,'High School(5th to 9th)':2,"10+2":3,'Higher Education':4}
dic8={'Teacher':3, 'Health care realated':1,'Civil Services':0,'Other':2}
dic9={'Close to Home':1, 'School Reputation':4,'Course preference':2,'At_Home':0,'Other':3}
dic10={'Mother':1,'Father':0,'Other':2}
dic11={'<15min':2,'15-30min':0,'30-60min':1,'>60min':3}
dic12={'<2hrs':2,'2-5hrs':0,'5-10hrs':1,'>10hrs':3}
dic13={'0':0,'1':1,'2':2,'3':3,'more':4}
dic14={'True':1,'False':0}



st.title('Student Ability')

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
    ('Teacher', 'Health care realated','Civil Services','Other'))



Fjob = st.selectbox(
    
    'Mother Job',
    ('Teacher', 'Health care realated','Civil Services','At_Home','Other'))



reson = st.selectbox(
    
    'Reson to Choose this School',
    ('Close to Home', 'School Reputation','Course preference','At_Home','Other'))




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

absences=age=st.number_input("No.of School Absences",min_value=1, max_value=5)

dec=pickle.load(open("decision.sav",'rb'))
svm=pickle.load(open("svm.sav",'rb'))
random=pickle.load(open("random.sav",'rb'))
logistic=pickle.load(open("logisticreg.sav",'rb'))
knn=pickle.load(open("knn.sav",'rb'))
if st.button('Predict'):
    values=[dic1[School],dic3[Sex],age,dic4[Address],dic5[Family_Size],dic6[Pstatus],dic7[Medu],dic7[Fedu],dic8[Mjob],dic8[Fjob],dic9[reson]
            ,dic10[guardian],dic11[traveltime],dic12[studytime],dic13[failures],dic14[schoolsup],dic14[famsup],dic14[paid],dic14[activities],
            dic14[nursery],dic14[higher],dic14[internet],dic14[romantic],famrel,freetime,goout,dalc,walc,health,absences]
    st.write(len(values))
   
    pred1=dec.predict([values])
    pred2=svm.predict([values])
    pred3=random.predict([values])
    pred4=logistic.predict([values])
    pred5=knn.predict([values])
    if(st.success):st.write(pred1[0],pred2[0],pred3[0],pred4[0],pred5[0])
    
else:
    st.write('click above for prediction')







































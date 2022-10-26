import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.linear_model import LinearRegression



''' # House Prediction Application
## This application predicts the price of houses in locations in the United Kingdom(UK)'''

#sidebar user input features
st.sidebar.header('## User input features')

def user_features():
    area =('Aberdeenshire', 'Adur', 'Allerdale', 'Amber Valley', 'Angus',
       'Argyll and Bute', 'Arun', 'Ashfield', 'Ashford', 'Babergh',
       'Barking and Dagenham', 'Barnet', 'Barnsley', 'Barrow-in-Furness',
       'Basildon', 'Basingstoke and Deane', 'Bassetlaw',
       'Bath and North East Somerset', 'Bedford', 'Bexley', 'Birmingham',
       'Blaby', 'Blackburn with Darwen', 'Blackpool', 'Blaenau Gwent',
       'Bolsover', 'Bolton', 'Boston',
       'Bournemouth Christchurch and Poole', 'Bracknell Forest',
       'Bradford', 'Braintree', 'Breckland', 'Brent', 'Brentwood',
       'Bridgend', 'Brighton and Hove', 'Broadland', 'Bromley',
       'Bromsgrove', 'Broxbourne', 'Broxtowe', 'Buckinghamshire',
       'Burnley', 'Bury', 'Caerphilly', 'Calderdale', 'Cambridge',
       'Cambridgeshire', 'Camden', 'Cannock Chase', 'Canterbury',
       'Cardiff', 'Carlisle', 'Carmarthenshire', 'Castle Point',
       'Central Bedfordshire', 'Ceredigion', 'Charnwood', 'Chelmsford',
       'Cheltenham', 'Cherwell', 'Cheshire East',
       'Cheshire West and Chester', 'Chesterfield', 'Chichester',
       'Chorley', 'City of Aberdeen', 'City of Bristol', 'City of Derby',
       'City of Dundee', 'City of Edinburgh', 'City of Glasgow',
       'City of Kingston upon Hull', 'City of Nottingham',
       'City of Peterborough', 'City of Plymouth', 'City of Westminster',
       'Clackmannanshire', 'Colchester', 'Conwy', 'Copeland', 'Cornwall',
       'Cotswold', 'County Durham', 'Coventry', 'Craven', 'Crawley',
       'Croydon', 'Cumbria', 'Dacorum', 'Darlington', 'Dartford',
       'Denbighshire', 'Derbyshire', 'Derbyshire Dales', 'Devon',
       'Doncaster', 'Dorset', 'Dover', 'Dudley', 'Dumfries and Galloway',
       'Ealing', 'East Ayrshire', 'East Cambridgeshire', 'East Devon',
       'East Dunbartonshire', 'East Hampshire', 'East Hertfordshire',
       'East Lindsey', 'East Lothian', 'East Midlands',
       'East Renfrewshire', 'East Riding of Yorkshire',
       'East Staffordshire', 'East Suffolk', 'East Sussex',
       'East of England', 'Eastbourne', 'Eastleigh', 'Eden', 'Elmbridge',
       'Enfield', 'England', 'England and Wales', 'Epping Forest',
       'Epsom and Ewell', 'Erewash', 'Essex', 'Exeter', 'Falkirk',
       'Fareham', 'Fenland', 'Fife', 'Flintshire', 'Folkestone and Hythe',
       'Forest of Dean', 'Fylde', 'Gateshead', 'Gedling', 'Gloucester',
       'Gloucestershire', 'Gosport', 'Gravesham', 'Great Britain',
       'Great Yarmouth', 'Greater Manchester', 'Greenwich', 'Guildford',
       'Gwynedd', 'Hackney', 'Halton', 'Hambleton',
       'Hammersmith and Fulham', 'Hampshire', 'Harborough', 'Haringey',
       'Harlow', 'Harrogate', 'Harrow', 'Hart', 'Hartlepool', 'Hastings',
       'Havant', 'Havering', 'Herefordshire', 'Hertfordshire',
       'Hertsmere', 'High Peak', 'Highland', 'Hillingdon',
       'Hinckley and Bosworth', 'Horsham', 'Hounslow' )
    options= list(range(len(area)))
    RegionName = st.sidebar.selectbox('Select the Region', options, format_func=lambda x: area[x])
    
    year=st.sidebar.slider('Select year of prediction?', 2021, 2040, 2030)
    month=st.sidebar.slider('Select month of prediction?', 1, 12, 6)
    data ={'RegionName':RegionName,'year':year,'month':month}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_features()

st.write(df)
#read in saved classification model
model= pickle.load(open('baggingreg.pkl','rb'))
model.fit(df)

#apply model
prediction =model.predict(df)
col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button('Calculate the Average Price')
if center_button:

    import time

    #my_bar = st.progress(0)

    with st.spinner('Calculating....'):
        time.sleep(2)

    lower_number = "{:,.2f}".format(float(prediction))
    st.subheader('GBP ' +str(lower_number))



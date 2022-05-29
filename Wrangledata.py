# packages

import  requests
import numpy as np
import pandas as pd
from datetime import datetime

 # define cleaning function 

 # define cleaning function 

def wrangle(file):
    
    # Load data
    dataset_name = file
    df = pd.read_csv(dataset_name, sep=";")
    
    # delete columns with more than 50% missing value
    df.drop(columns = ["assoc_actor_1","assoc_actor_2","admin3"], inplace =True)

    # delete columns with no useful information 
    df.drop(columns = ["event_id_cnty","region","iso3","country"], inplace=True)

    # convert event_date to datetime dtype
    dateFormatter = "%d %B %Y"
    df['event_date']=pd.to_datetime(df["event_date"], format=dateFormatter)

    # drop numeric features with no useful information 
    df.drop(columns = ["data_id", "iso", "event_id_no_cnty","time_precision","timestamp","geo_precision"] , inplace=True)
    
    # create new feature interact
    key = [10,11,12,13,14,15,16,17,18,20,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,44,45,46,47,48,50,55,56,57,58,60,66,67,68,78,80]

    value = ["SOLE MILITARY ACTION","MILITARY VERSUS MILITARY","MILITARY VERSUS REBELS","MILITARY VERSUS POLITICAL MILITIA",
      "MILITARY VERSUS COMMUNAL MILITIA","MILITARY VERSUS RIOTERS","MILITARY VERSUS PROTESTERS","MILITARY VERSUS CIVILIANS",
      "MILITARY VERSUS OTHER","SOLE REBEL ACTION","REBELS VERSUS REBELS","REBELS VERSUS POLITICAL MILIITA","REBELS VERSUS COMMUNAL MILITIA",
      "REBELS VERSUS RIOTERS","REBELS VERSUS PROTESTERS","REBELS VERSUS CIVILIANS","REBELS VERSUS OTHERS","SOLE POLITICAL MILITIA ACTION",
      "POLITICAL MILITIA VERSUS POLITICAL MILITIA","POLITICAL MILITIA VERSUS COMMUNAL MILITIA","POLITICAL MILITIA VERSUS RIOTERS",
      "POLITICAL MILITIA VERSUS PROTESTERS","POLITICAL MILITIA VERSUS CIVILIANS","POLITICAL MILITIA VERSUS OTHERS","SOLE COMMUNAL MILITIA ACTION",
      "COMMUNAL MILITIA VERSUS COMMUNAL MILITIA","COMMUNAL MILITIA VERSUS RIOTERS","COMMUNAL MILITIA VERSUS PROTESTERS","COMMUNAL MILITIA VERSUS CIVILIANS",
      "COMMUNAL MILITIA VERSUS OTHER","SOLE RIOTER ACTION","RIOTERS VERSUS RIOTERS","RIOTERS VERSUS PROTESTERS","RIOTERS VERSUS CIVILIANS",
      "RIOTERS VERSUS OTHERS","SOLE PROTESTER ACTION","PROTESTERS VERSUS PROTESTERS","PROTESTERS VERSUS CIVILIANS","PROTESTERS VERSUS OTHER",
      "OTHER ACTOR VERSUS CIVILIANS","SOLE OTHER ACTION"]

    actor_type= ["No victime","State Forces","Rebel Groups","Political Militias","Communal Militias",
                 "Rioters","Protesters","Civilians","Other Forces"]
    actor_key=range(0,9)

    # inter1
    df["inter_1"]=df["inter1"]
    for i in range(len(actor_key)):
        df.inter_1[df["inter1"]==int(actor_key[i])]=str(actor_type[i].lower())
    # inter2
    df["inter_2"]=df["inter2"]
    for i in range(len(actor_key)):
        df.inter_2[df["inter2"]==int(actor_key[i])]=str(actor_type[i].lower())

    # interaction    
    df["interact"]=df["interaction"]

    for i in range(len(key)):
        df.interact[df["interact"]==int(key[i])]=str(value[i].lower())
        
    df.drop(columns=["interaction",'inter1','inter2'], inplace=True)
    

    return df

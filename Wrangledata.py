# packages

import  requests
import numpy as np
import pandas as pd
from datetime import datetime

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
    df.drop(columns = ["data_id", "iso", "event_id_no_cnty",
                       "time_precision","timestamp","geo_precision"] , inplace=True)
    
       # Transform variable

    key = [10,11,12,13,14,15,16,17,18,20,22,23,24,25,26,27,28,30,33,34,35,
           36,37,38,40,44,45,46,47,48,50,55,56,57,58,60,66,67,68,78,80,88]

    value = ['sole military action', 'military versus military', 'military versus rebels', 'military versus political militia',
         'military versus communal militia', 'military versus rioters', 'military versus protesters', 'military versus civilians',
         'military versus other', 'sole rebel action', 'rebels versus rebels', 'rebels versus political miliita',
         'rebels versus communal militia', 'rebels versus rioters', 'rebels versus protesters', 'rebels versus civilians',
         'rebels versus others', 'sole political militia action', 'political militia versus political militia',
         'political militia versus communal militia', 'political militia versus rioters', 'political militia versus protesters',
         'political militia versus civilians', 'political militia versus others', 'sole communal militia action',
         'communal militia versus communal militia', 'communal militia versus rioters', 'communal militia versus protesters',
         'communal militia versus civilians', 'communal militia versus other', 'sole rioter action', 'rioters versus rioters',
         'rioters versus protesters', 'rioters versus civilians', 'rioters versus others', 'sole protester action', 'protesters versus protesters',
         'protesters versus civilians', 'protesters versus other', 'other actor versus civilians',
             'sole other action','other force versus  other force']

    actor_type= ['no victicme', 'state forces', 'rebel groups', 'political militias', 'communal militias',
             'rioters', 'protesters', 'civilians', 'other forces']
    actor_key=range(0,9)

    # inter1
    df["inter1"]=df["inter1"].replace(actor_key,actor_type)

    # inter2
    df["inter2"]=df["inter2"].replace(actor_key,actor_type)

    # interaction    
    df["interaction"]=df["interaction"].replace(key,value)

    
    return df

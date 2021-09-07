import pandas as pd
import numpy as np


def get_connection(db_name):
    '''
    Function to connect to the data base
    
    '''
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'



def wrangle_zillow():
    '''
    Creating a pandas database from the telco data
   
    '''
    sql_query = '''
    SELECT 
    bedroomcnt, 
    bathroomcnt, 
    calculatedfinishedsquarefeet, 
    taxvaluedollarcnt, 
    yearbuilt, 
    taxamount, 
    fips
    FROM properties_2017
    where propertylandusetypeid = 261
    ;
    '''
    return pd.read_sql(sql_query, get_connection('zillow'))
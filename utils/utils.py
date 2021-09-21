import pandas as pd
import time
import logging
from functools import wraps
import streamlit as st


# define the logging
logger = logging.getLogger(__name__)

# Misc logger setup so a debug log statement gets printed on stdout.
logger.setLevel("INFO")
handler = logging.FileHandler('exec_time_logs.txt', mode='a', delay=False, errors=None)
log_format = "%(asctime)s %(levelname)s -- %(message)s"
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
logger.addHandler(handler)

def timed(func):
    """This decorator prints the execution time for the decorated function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info("{} ran in {}s".format(func.__name__, round(end - start, 2)))
        return result

    return wrapper

# preprocess dataset for analysis
@timed
@st.cache(persist=True)
def preprocess_data():
    df = pd.read_csv('../ny-trips-data.csv')  
    lowercase = lambda x: str(x).lower()
    df.rename(lowercase, axis="columns", inplace=True)
    
    # convert to datetime
    df['tpep_pickup_datetime'] =  pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] =  pd.to_datetime(df['tpep_dropoff_datetime'])    
    
    # derive features based on datetime column
    df['hour_pickup']=df['tpep_pickup_datetime'].dt.hour
    df['hour_dropoff']=df['tpep_dropoff_datetime'].dt.hour
    df['min_pickup']=df['tpep_pickup_datetime'].dt.minute
    df['min_dropoff']=df['tpep_dropoff_datetime'].dt.minute
    
    # create a trip duration feature
    df['trip_duration'] = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']
    df['trip_duration'] = df['trip_duration'].apply(lambda x: x.seconds)

    return df

df = preprocess_data()

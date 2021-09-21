import streamlit as st
import time
from utils.utils import df
import streamlit.components.v1 as components

# setting up a progress bar
bar = st.progress(0)
for i in range(100):
    bar.progress(i + 1)
    time.sleep(0.025)
bar.empty() 

def app():

    # LAYING OUT THE TOP SECTION OF THE APP
    
    components.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        
        <div class="alert alert-success" >
        Congratulations! Analysis has been performed successfully.
        </div> <br>
        <br>
        <div class="card mx-auto" style="width: 40rem;">
        <img class="card-img-top" src="https://nypost.com/wp-content/uploads/sites/2/2020/05/sized-yellow-taxi.jpg?quality=90&strip=all" alt="Card image cap">
        <div class="card-body">
            <h5 class="card-title">Analysis of NYC trips</h5>
            <p class="card-text">Examining NYC trips using different vizualisation techniques. By sliding the slider on the left you can view different slices of time and explore different transportation trends.</p>
            <a href="https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page" class="btn btn-primary">Source dataset can be found here.</a>
        </div>
        </div>
        """,
        height=800
    )

    st.video("https://www.youtube.com/watch?v=8wbRUl7I2A8&ab_channel=AssociatedPress")


    

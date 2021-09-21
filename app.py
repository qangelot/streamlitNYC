from apps import app1, app2, home
import streamlit as st
from multiapp import MultiApp


# add all apps
app = MultiApp()

app.add_app("Home", home.app)
app.add_app("Exploratory analysis", app1.app)
app.add_app("Geospatial analysis", app2.app)

# The main app
app.run()
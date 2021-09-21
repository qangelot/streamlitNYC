import pydeck as pdk
from utils.utils import timed, df, st
import numpy as np


# CREATING FUNCTION FOR MAPS
@timed
def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 50,
        },
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position=["pickup_longitude", "pickup_latitude"],
                radius=100,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ]
    ))
    

def app():

    st.header("**Filtered by hour**")

    hours_selected = st.slider("Select hours of pickup", 0, 23, (12, 14))

    # FILTERING DATA BY HOUR SELECTED
    data = df[df['hour_pickup'].between(hours_selected[0],hours_selected[1])]

    st.write("")

    st.header("**Geospatial analysis**")
    
    st.write("")

    # LAYING OUT THE MIDDLE SECTION OF THE APP WITH THE MAPS
    # SETTING THE ZOOM LOCATIONS FOR THE AIRPORTS
    la_guardia= [40.7900, -73.8700]
    jfk = [40.6650, -73.7821]
    zoom_level = 12
    midpoint = (np.average(data["pickup_latitude"]), np.average(data["pickup_longitude"]))  

    st.write("**All New York City from %i:00 and %i:00**" % (hours_selected[0], (hours_selected[1]) % 24))
    map(data, midpoint[0], midpoint[1], 11)

    st.write("")

    row2_3, row2_4 = st.columns((1,1))

    with row2_3:
        st.write("**La Guardia Airport**")
        map(data, la_guardia[0],la_guardia[1], zoom_level)

    with row2_4:
        st.write("**JFK Airport**")
        map(data, jfk[0],jfk[1], zoom_level)
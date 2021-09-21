import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import altair as alt
import pydeck as pdk
import numpy as np
import matplotlib.patches as mpatches
import plotly.express as px
import plotly.graph_objects as go
from utils.utils import timed, df, st
 

def app(): 
    st.header("**Global analysis**")
    st.write("")

    ##################################univariate################################

    @timed
    def plot_dist(df, col1, col2):
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=df[col1], 
            name=str(col1)))
        fig.add_trace(go.Histogram(x=df[col2], 
            name=str(col2)))
        # Overlay both histograms
        fig.update_layout(barmode='overlay', margin=dict(
                l=0, r=0, b=0, t=0,
            ), legend=dict(yanchor="top",
                y=0.99, xanchor="left", x=0.01))
        # Reduce opacity to see both histograms
        fig.update_traces(opacity=0.5)
        st.plotly_chart(fig)


    st.write("**Pickup distribution by hour**")
    plot_dist(df, 'hour_pickup', 'hour_dropoff')

    st.write("**Pickup distribution by minute**")
    plot_dist(df, 'min_pickup', 'min_dropoff')

    ##################################filtered by hour################################

    st.write("")

    st.header("**Filtered by hour**")

    hours_selected = st.slider("Select hours of pickup", 0, 23, (12, 14))

    # FILTERING DATA BY HOUR SELECTED
    data = df[df['hour_pickup'].between(hours_selected[0],hours_selected[1])]

    my_expander = st.expander(label="Show the distribution of rides per minute between %i:00 and %i:00" % (hours_selected[0], (hours_selected[1]) % 24))

    hist = np.histogram(data['min_pickup'], bins=60, range=(0, 60))[0]
    chart_data = pd.DataFrame({"minute": range(60), "pickups": hist})

    # LAYING OUT THE HISTOGRAM SECTION
    with my_expander:

        st.altair_chart(alt.Chart(chart_data)
            .mark_area(
                interpolate='step-after',
            ).encode(
                x=alt.X("minute:Q", scale=alt.Scale(nice=False)),
                y=alt.Y("pickups:Q"),
                tooltip=['minute', 'pickups']
            ).configure_mark(
                opacity=0.5,
                color='red'
            ), use_container_width=True)


    @timed
    def trip_distance_distri(df):
        data = go.Histogram(x=df.trip_distance)
        # Reduce opacity to see both histograms
        layout = go.Layout(
        margin=go.layout.Margin(
                l=0, r=0, b=0, t=0,
            )
        )
        fig = dict(data=data, layout=layout)
        st.plotly_chart(fig)


    @timed
    def fare_n_tips_distri(df):
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=df.fare_amount, 
            name='fare_amount'))
        fig.add_trace(go.Histogram(x=df.tip_amount, 
            name='tip_amount'))
        fig.update_xaxes(range=(0, 100))
        fig.update_yaxes(range=(0, 2500))

        # Overlay both histograms
        fig.update_layout(barmode='overlay', margin=dict(
                l=0, r=0, b=0, t=0,
            ), legend=dict(yanchor="top",
                y=0.99, xanchor="left", x=0.01))
        # Reduce opacity to see both histograms
        fig.update_traces(opacity=0.75)
        st.plotly_chart(fig)


    st.write("**Fares and tips distribution**")
    fare_n_tips_distri(data)

    st.write("**Trip distances distribution**")
    trip_distance_distri(data)

    st.write("")

    st.header("**Multivariate analysis**")


    @timed
    def scatter(df, col, range=None):
        fig = px.scatter(df, x=col, y='total_amount', color="passenger_count")
        fig.update_xaxes(range=range)
        fig.update_layout(barmode='overlay', margin=dict(
                l=0, r=0, b=0, t=0,
            ), legend=dict(yanchor="top",
                y=0.99, xanchor="left", x=0.01))
        fig.update_traces(opacity=0.5)
        fig.update_yaxes(range=(0, 250))

        st.plotly_chart(fig)


    st.write("**Fares et tips distribution**")
    scatter(data, 'trip_duration', range=(0, 15000))

    st.write("**Trip distance distribution**")
    scatter(data, 'trip_distance')


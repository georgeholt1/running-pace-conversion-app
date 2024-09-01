import streamlit as st

# Constants
# ----------------------------------------------------------------------

MILES_PER_KM = 1.60934


# Functions
# ----------------------------------------------------------------------


def calculate_total_secs(hrs, mins, secs):
    return hrs * 60 * 60 + mins * 60 + secs


def convert_from_km_pace(km_pace):
    """Convert from pace in seconds per kilometer to pace in seconds per
    mile, speed in miles per hour and speed in kilometers per hour"""
    mile_pace = km_pace * MILES_PER_KM
    kph = 60 * 60 / km_pace
    mph = 60 * 60 / mile_pace
    return mile_pace, mph, kph


def convert_from_mile_pace(mile_pace):
    """Convert from pace in seconds per mile to pace in seconds per
    kilometer, speed in miles per hour and speed in kilometers per hour"""
    km_pace = mile_pace / MILES_PER_KM
    kph = 60 * 60 / km_pace
    mph = 60 * 60 / mile_pace
    return km_pace, kph, mph


def convert_from_kph(kph):
    """Convert from speed in kilometers per hour to speed in miles per
    hour, pace in seconds per mile and pace in seconds per kilometer"""
    mph = kph / MILES_PER_KM
    mile_pace = 60 * 60 / mph
    km_pace = 60 * 60 / kph
    return mile_pace, km_pace, mph


def convert_from_mph(mph):
    """Convert from speed in miles per hour to speed in kilometers per
    hour, pace in seconds per mile and pace in seconds per kilometer"""
    kph = mph * MILES_PER_KM
    km_pace = 60 * 60 / kph
    mile_pace = 60 * 60 / mph
    return km_pace, kph, mile_pace


def calculate_mph(miles, secs):
    """Calculate speed in miles per hour"""
    return miles / secs * 60 * 60


def calculate_kph(km, secs):
    """Calculate speed in kilometers per hour"""
    return km / secs * 60 * 60


# App
# ----------------------------------------------------------------------

st.title("Running pace converter")

st.markdown(
    """This app converts between running pace and speed units.

To get started, select the tab for the known units and enter the values."""
)

pace_tab, distance_and_time_tab = st.tabs(["Pace", "Distance and time"])

# Tab to convert from pace
with pace_tab:

    # Inputs
    with st.container(border=True):
        st.markdown("Inputs")

        # Units selection
        pace_unit = st.radio("Pace unit", ["Kilometers", "Miles"])

        # Pace input
        col_mins, col_secs = st.columns(2)

        with col_mins:
            mins = st.number_input("Minutes", 0, 59, 5, key="pace_mins")
        with col_secs:
            secs = st.number_input("Seconds", 0, 59, 0, key="pace_secs")

    # Calculations
    total_secs = calculate_total_secs(0, mins, secs)
    if total_secs == 0:
        div_by_zero = True
    else:
        div_by_zero = False

    if not div_by_zero:
        if pace_unit == "Kilometers":
            mile_pace, mph, kph = convert_from_km_pace(total_secs)
        else:
            km_pace, kph, mph = convert_from_mile_pace(total_secs)

    # Results
    with st.container(border=True):
        st.markdown("Results")

        if div_by_zero:
            st.markdown("Please enter a pace greater than zero")
        else:
            col_pace_result, col_mph_result, col_kph_result = st.columns(3)

            # Pace results
            with col_pace_result:
                if pace_unit == "Kilometers":
                    st.markdown(
                        f"Mile pace:  \n{int(mile_pace // 60)}:{int(mile_pace % 60):02d}"
                    )
                else:
                    st.markdown(
                        f"Kilometer pace:  \n{int(km_pace // 60)}:{int(km_pace % 60):02d}"
                    )

            # Speed results
            with col_mph_result:
                st.markdown(f"Speed (km/h):  \n{kph:.2f}")
            with col_kph_result:
                st.markdown(f"Speed (miles/h):  \n{mph:.2f}")

# Tab to convert from distance and time
with distance_and_time_tab:

    # Inputs
    with st.container(border=True):
        st.markdown("Inputs")

        # Distance input
        with st.container(border=True):
            distance_unit = st.radio("Distance unit", ["Kilometers", "Miles"])
            distance = st.number_input(
                "Distance", 0.0, 10000000.0, 10.0, key="distance"
            )

        # Time input
        with st.container(border=True):
            col_dist_hours, col_dist_mins, col_dist_secs = st.columns(3)
            with col_dist_hours:
                dist_hours = st.number_input(
                    "Hours", 0, 1000, 0, key="dist_hours"
                )
            with col_dist_mins:
                dist_mins = st.number_input(
                    "Minutes", 0, 59, 50, key="dist_mins"
                )
            with col_dist_secs:
                dist_secs = st.number_input(
                    "Seconds", 0, 59, 0, key="dist_secs"
                )

    # Calculations
    total_secs = calculate_total_secs(dist_hours, dist_mins, dist_secs)
    if total_secs == 0:
        div_by_zero = True
    else:
        div_by_zero = False

    if not div_by_zero:
        if distance_unit == "Kilometers":
            kph = calculate_kph(distance, total_secs)
            mile_pace, km_pace, mph = convert_from_kph(kph)
        else:
            mph = calculate_mph(distance, total_secs)
            km_pace, kph, mile_pace = convert_from_mph(mph)

    # Results
    with st.container(border=True):
        st.markdown("Results")

        if div_by_zero:
            st.markdown("Please enter a time greater than zero")
        else:
            (
                col_pace_mile_result,
                col_pace_km_result,
                col_mph_result,
                col_kph_result,
            ) = st.columns(4)

            # Pace results
            with col_pace_mile_result:
                st.markdown(
                    f"Mile pace:  \n{int(mile_pace // 60)}:{int(mile_pace % 60):02d}"
                )
            with col_pace_km_result:
                st.markdown(
                    f"Kilometer pace:  \n{int(km_pace // 60)}:{int(km_pace % 60):02d}"
                )

            # Speed results
            with col_mph_result:
                st.markdown(f"Speed (km/h):  \n{kph:.2f}")
            with col_kph_result:
                st.markdown(f"Speed (miles/h):  \n{mph:.2f}")


# Footer
# ----------------------------------------------------------------------

from htbuilder import HtmlElement, a, div, hr, img, p, styles
from htbuilder.units import percent, px


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="white",
        text_align="center",
        height="auto",
        opacity=1,
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2),
    )

    body = p()
    foot = div(style=style_div)(hr(style=style_hr), body)

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Made in Streamlit ",
        " with ❤️ by ",
        link("https://github.com/georgeholt1", "@georgeholt1"),
    ]
    layout(*myargs)


footer()

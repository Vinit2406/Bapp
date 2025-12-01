import streamlit as st
import pandas as pd

# ---------------------------------------
# HARD-CODED DATA (From your Excel file)
# ---------------------------------------
years   = [2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
budget  = [179,188,200,215,230,245,260,275,290,310,325,340]
revenue = [155,162,175,190,205,220,210,225,240,260,280,295]

# Create DataFrame for easier chart handling
df = pd.DataFrame({
    "Year": years,
    "Budget": budget,
    "Revenue": revenue
})

data = {
    "Year": years,
    "Budget": budget,
    "Revenue": revenue
}

# ---------------------------------------
# THEME (Light / Dark Toggle)
# ---------------------------------------
st.sidebar.title("⚙️ Settings")

theme = st.sidebar.radio("Theme", ["Light", "Dark"])

if theme == "Dark":
    st.markdown("""
        <style>
            .stApp {
                background-color: #0d0f15;
                color: white;
            }
            .stMarkdown, .stMetric, .stDataFrame, .stTable {
                color: white !important;
            }
        </style>
    """, unsafe_allow_html=True)

# ---------------------------------------
# TITLE
# ---------------------------------------
st.title("📊 Budget Dashboard (2014–2025)")
st.write("Clean, minimal dashboard using only Streamlit — no external modules required.")

# ---------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------
page = st.sidebar.selectbox("Navigate", ["Overview", "Charts", "Comparison", "Data"])

# ---------------------------------------
# PAGE: OVERVIEW
# ---------------------------------------
if page == "Overview":
    st.header("📌 Summary Highlights")

    total_budget = sum(budget)
    total_revenue = sum(revenue)
    growth = round(((budget[-1] - budget[0]) / budget[0]) * 100, 2)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Budget", total_budget)
    col2.metric("Total Revenue", total_revenue)
    col3.metric("Budget Growth", f"{growth}%")

    st.subheader("📈 Budget Trend")
    st.line_chart(df, x="Year", y="Budget")

# ---------------------------------------
# PAGE: CHARTS
# ---------------------------------------
elif page == "Charts":
    st.header("📉 Trends Over Time")

    variable = st.selectbox("Select Metric", ["Budget", "Revenue"])

    if variable == "Budget":
        st.area_chart(df, x="Year", y="Budget")
    else:
        st.area_chart(df, x="Year", y="Revenue")

# ---------------------------------------
# PAGE: COMPARISON
# ---------------------------------------
elif page == "Comparison":
    st.header("📊 Budget vs Revenue")

    st.bar_chart(df, x="Year", y=["Budget", "Revenue"])

# ---------------------------------------
# PAGE: RAW DATA
# ---------------------------------------
elif page == "Data":
    st.header("📄 Full Dataset")
    st.table(data)

    # Generate CSV manually
    csv = "Year,Budget,Revenue\n"
    for y, b, r in zip(years, budget, revenue):
        csv += f"{y},{b},{r}\n"

    st.download_button(
        "⬇️ Download CSV",
        csv,
        "budget_data.csv",
        "text/csv"
    )

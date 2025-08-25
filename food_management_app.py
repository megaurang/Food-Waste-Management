import streamlit as st
import pandas as pd

st.title("🍽️ Food Donation Insights Dashboard")

# Load DataFrames
dfs = {}
for i in range(1, 16):
    dfs[f"df{i}"] = pd.read_csv(f"df{i}.csv")

# ----------------- Major Tabs -----------------
tabs = st.tabs([
    "Providers & Receivers",
    "Food Listings",
    "Claims & Distribution",
    "Analysis & Insights"
])

# ----------------- Tab 1: Providers & Receivers -----------------
with tabs[0]:
    st.subheader("Providers & Receivers Insights")

    # Dropdown to select which data to see
    choice = st.selectbox("Select view:", [
        "Providers & Receivers per City",
        "Provider Types Contribution",
        "Provider Contact Information"
    ])

    if choice == "Providers & Receivers per City":
        st.dataframe(dfs["df1"])
        st.bar_chart(dfs["df1"].set_index("City"))
    elif choice == "Provider Types Contribution":
        st.dataframe(dfs["df2"])
        st.bar_chart(dfs["df2"].set_index("Provider_Type"))
    elif choice == "Provider Contact Information":
        selected_city = st.selectbox("Select City", dfs["df3"]["City"].unique())
        st.dataframe(dfs["df3"][dfs["df3"]["City"] == selected_city])

# ----------------- Tab 2: Food Listings -----------------
with tabs[1]:
    st.subheader("Food Listings Insights")
    section = st.radio("Select Section:", [
        "Top Receivers", 
        "Total Food Available", 
        "Number of Food Listings per City/Location",
        "Most Common Food Types"
    ])
    if section == "Top Receivers":
        st.dataframe(dfs["df4"])
        st.bar_chart(dfs["df4"].set_index("Receiver_Name"))
    elif section == "Total Food Available":
        st.dataframe(dfs["df5"])
        st.bar_chart(dfs["df5"].set_index("Food_Name"))
    elif section == "Number of Food Listings per City/Location":
        st.dataframe(dfs["df6"])
        st.bar_chart(dfs["df6"].set_index("Location"))
    elif section == "Most Common Food Types":
        st.dataframe(dfs["df7"])
        st.bar_chart(dfs["df7"].set_index("Food_Type"))

# ----------------- Tab 3: Claims & Distribution -----------------
with tabs[2]:
    st.subheader("Claims & Distribution")
    section = st.selectbox("Select Claim Section:", [
        "Completed Claims per Food Item",
        "Provider with Most Successful Claims",
        "Claims Status Distribution"
    ])
    if section == "Completed Claims per Food Item":
        st.dataframe(dfs["df8"])
        st.bar_chart(dfs["df8"].set_index("Food_Name"))
    elif section == "Provider with Most Successful Claims":
        st.dataframe(dfs["df9"])
    elif section == "Claims Status Distribution":
        st.dataframe(dfs["df10"])
        st.bar_chart(dfs["df10"].set_index("Status"))

# ----------------- Tab 4: Analysis & Insights -----------------
with tabs[3]:
    st.subheader("Analysis & Insights")
    section = st.selectbox("Select Analysis Section:", [
        "Average Quantity per Receiver",
        "Most Claimed Meal Types",
        "Total Donations by Provider",
        "Cancelled Claims by City",
        "Cancelled Claims by Food Type"
    ])
    if section == "Average Quantity per Receiver":
        st.dataframe(dfs["df11"])
    elif section == "Most Claimed Meal Types":
        st.dataframe(dfs["df12"])
        st.bar_chart(dfs["df12"].set_index("Meal_Type"))
    elif section == "Total Donations by Provider":
        st.dataframe(dfs["df13"])
        st.bar_chart(dfs["df13"].set_index("Provider_Name"))
    elif section == "Cancelled Claims by City":
        st.dataframe(dfs["df14"])
        st.bar_chart(dfs["df14"].set_index("City"))
    elif section == "Cancelled Claims by Food Type":
        st.dataframe(dfs["df15"])
        st.bar_chart(dfs["df15"].set_index("Food_Type"))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit_shadcn_ui as ui


st.set_page_config(page_title="AutoNote")

html = """
<style>
.gradient-text {
    background-image: linear-gradient(to right top, #051937, #004d7a, #008793, #00bf72, #a8eb12);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 3em;
    font-weight: bold;
}
</style>
<div class="gradient-text">AutoNote App - View Code</div>
"""
st.markdown(html, unsafe_allow_html=True)

conn = st.connection("CloudSQL", type="sql", autocommit=True)
groups = conn.query("select * from code_groups3", ttl=3600)
# st.dataframe(groups)

conn = st.connection("CloudSQL", type="sql", autocommit=True)
code = conn.query("select * from code_blocks3", ttl=3600)
# st.dataframe(code)

st.sidebar.container(height=5, border=0)

page = st.sidebar.radio(
    "Choose a Page",
    [
        "View Code",
        "Enter New Code",
        "Edit Group Names",
        "Delete Code",
        "About",
    ],
)
st.sidebar.container(height=200, border=0)


st.sidebar.write("")

centered_html = """
    <style>
    .centered {
        text-align: center;
    }
    </style>
    <div class='centered'>
    <img alt="Static Badge" src="https://img.shields.io/badge/github-janduplessis883-%2338808e?style=social">

    </div>
"""


# Using the markdown function with HTML to center the text
st.sidebar.markdown(centered_html, unsafe_allow_html=True)

# ======== View Code ===============================================================
if page == "View Code":
    options = groups["group_name"].to_list()
    options.sort()
    name_to_id = pd.Series(groups.id.values, index=groups.group_name).to_dict()
    selected_group_name = st.selectbox("Choose an option:", options)

    selected_id = name_to_id[selected_group_name]

    # Display the selected information
    st.markdown(f"You selected {selected_group_name} with ID `{selected_id}`")

    selected_code = code[code["group_id"] == selected_id]

    # st.write(selected_code)

    for _, row in selected_code.iterrows():
        code = row["code"]
        markdown = row["markdown"]

        print("Markdown:", markdown)  # Debugging line to check values

        if markdown == 0:
            st.code(code)
        else:
            st.markdown(code)


if page == "Enter New Code":
    st.header("Enter New Code")


if page == "Edit Group Names":
    st.header("Edit Group Names")


if page == "Delete Code":
    st.header("Delete Code")


if page == "About":
    st.header("About")

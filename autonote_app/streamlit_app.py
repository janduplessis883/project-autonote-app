import streamlit as st
import os
import streamlit.components.v1 as components
from pydataset import data
import random

# Assuming streamlit_shadcn_ui exists and has been installed
import streamlit_shadcn_ui as ui

random_number = random.randint(1, 4)


# Function to check the password
def check_password(entered_password):
    """Returns `True` if the user had the right password."""
    return entered_password == "jan883"


# Main app
def main():
    """Main function running Streamlit app."""
    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        ui.badges(
            badge_list=[("Welcome, Jan", "default"), ("You are logged in!", "outline")],
            class_name="flex gap-2",
            key="badges2",
        )
        tab = ui.tabs(
            options=["Home", "AutoNote", "ML", "URLs", "Pydataset"],
            default_value="Home",
            key="kanaries",
        )

        if tab == "Home":
            st.title("Home")
            st.image(f"images/random{random_number}.png")

        elif tab == "AutoNote":
            st.title("AutoNote")
            pass

        elif tab == "ML":
            st.title("Machine Learning")
            pass

        elif tab == "URLs":
            st.title("URLs")
            ui.link_button(
                text="Github Jan Repo",
                url="https://github.com/janduplessis883?tab=repositories",
                key="link_btn1",
            )
            ui.link_button(
                text="Streamlit My Apps",
                url="https://share.streamlit.io",
                key="link_btn2",
            )
            ui.link_button(
                text="AI MedReview",
                url="https://ai-medreview.streamlit.app",
                key="link_btn3",
            )
            ui.link_button(
                text="DeepLearningAI",
                url="https://www.deeplearning.ai/short-courses/",
                key="link_btn4",
            )

        elif tab == "Pydataset":
            st.title("Pydataset")
            my_dataset = data()
            st.write(my_dataset)

            dataset_id_list = my_dataset["dataset_id"].to_list()
            select_dataset = st.selectbox(label="View Dataset", options=dataset_id_list)
            st.markdown(f"Dataset size = **{data(select_dataset).shape}**")
            st.write(data(select_dataset))

    else:
        login_form()


def login_form():
    """Login form for password entry styled with custom CSS."""
    with st.container(height=150, border=0):
        pass
    ui.avatar(
        src="https://github.com/janduplessis883/project-autonote-app/blob/master/images/janavi2.png?raw=true"
    )
    password = ui.input(
        default_value="", type="password", placeholder="Enter password!", key="input1"
    )
    submitted = ui.button("Login", key="clk_btn")
    if submitted:
        if check_password(password):
            st.session_state["logged_in"] = True
            st.experimental_rerun()
        else:
            st.write("")  # Clear any previous messages
            ui.badges(
                badge_list=[("Incorrect Password! Please try again.", "destructive")],
                class_name="flex gap-2",
                key="password_badge",
            )


if __name__ == "__main__":
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    main()

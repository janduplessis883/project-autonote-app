import streamlit as st
import os
import streamlit.components.v1 as components
from pydataset import data
import random
from datetime import datetime
import requests

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
            options=["Home", "AutoNote", "ML", "URLs", "Pydataset", "Reg Authority"],
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

        elif tab == "Reg Authority":
            st.title("Registration Authority")
            # Create a form
            # Create a form
            with st.form(key="staffmember_form"):
                # Input fields
                name = st.text_input(label="", placeholder="Full Name")
                smart_card = st.text_input(label="", placeholder="Smart Card No.")
                pos1 = st.text_input(label="", placeholder="Position Name")
                reason = st.text_input(
                    label="", placeholder="Reason for position assignment."
                )
                eps = st.toggle(
                    label="Electronic Prescribing"
                )  # Changed toggle to checkbox

                col1, col2 = st.columns(2)
                start_date = col1.date_input(label="Start Date", value=datetime.today())
                end_date = col2.date_input(label="End Date", value=datetime.today())

                submit_button = st.form_submit_button(label="Submit")

                # Handling form submission
                if submit_button:
                    form_data = {
                        "name": name,
                        "smart_card": smart_card,
                        "position": pos1,
                        "reason": reason,
                        "electronic_prescribing": eps,
                        "start_date": start_date.strftime("%Y-%m-%d"),
                        "end_date": end_date.strftime("%Y-%m-%d"),
                    }

                    # Send the form data via a webhook
                    webhook_url = (
                        "https://hook.eu1.make.com/dpo7fghnlv7elbgoqnaj6gpk0gg4mn44"
                    )
                    response = requests.post(webhook_url, json=form_data)

                    if response.status_code == 200:
                        st.success(
                            f"Form submitted successfully! Name: {name}, Smart card: {smart_card}"
                        )
                    else:
                        st.error(
                            f"Failed to submit form. Status code: {response.status_code}"
                        )

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

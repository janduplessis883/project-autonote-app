import streamlit as st
import os

# Assuming streamlit_shadcn_ui exists and has been installed
import streamlit_shadcn_ui as ui


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
        st.image("images/new.png")
        # You can add your main app logic here
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

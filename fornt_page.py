import streamlit as st
from datetime import datetime

def display_front_page():
    st.markdown(
        """
        <style>
        .front-page {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 30vh; /* Reduced height to make room for text overlay */
            background-color: #001f3f; /* Dark blue background */
            color: white;
            padding: 20px;
            border-radius: 10px;
        }
        .start-demo {
            margin-top: 20px;
            font-size: 1.5em; /* Larger font size for headings */
        }
        .email-input {
            width: 300px;
            margin-top: 20px;
            padding: 10px;
            border-radius: 5px;
            border: none;
            font-size: 1em;
        }
        .submit-button {
            margin-top: 10px;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: #FF851B; /* Orange button */
            color: white;
            font-size: 1em;
            cursor: pointer;
        }
        .submit-button:hover {
            background-color: #FF6347; /* Lighter orange on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<div class="front-page">'
                "<h1>AI-Assisted Case Classification</h1>",
                  unsafe_allow_html=True)
    # st.markdown("<h1>AI-Assisted Case Classification</h1>", unsafe_allow_html=True)
    st.markdown('<h2 class="start-demo">Start Demo</h2>', unsafe_allow_html=True)

    email = st.text_input("Enter your Email Id:", key="email", help="We will not share your email with anyone.")
    if st.button("Submit", key="submit_button"):
        if email:
            log_email(email)
            st.session_state.email_logged = True
        else:
            st.warning("Please enter your email address to proceed.")

    st.markdown('<p>Illustrative Version Only</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def log_email(email):
    with open('email_log.txt', 'a') as log_file:
        log_file.write(f"{email} logged in at {datetime.now()}\n")

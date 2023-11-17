import streamlit as st

st.header(":envelope: Email me!")

email = st.secrets["EMAIL"]

contact_form = f"""
    <form action="https://formsubmit.co/{email}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

st.markdown(contact_form, unsafe_allow_html=True)


# css function
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

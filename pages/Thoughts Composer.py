import streamlit as st

st.title(" Thought Composer")

st.markdown("Describe your intention or thought below. The system will interpret it into pseudo-code.")

user_thought = st.text_area("Your Thought", placeholder="e.g., I want to comfort someone who feels lost tomorrow.")

if st.button("Compose Logic"):
    if user_thought:
        st.subheader(" Interpreted Logic")
        st.code(f"# Intent: {user_thought}\nif future.user_emotion == 'lost':\n    send_message('You are not alone.')", language="python")
    else:
        st.warning("Please enter a thought to compose logic.")

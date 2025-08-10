import streamlit as st
import uuid
import importlib.util
import os

utils_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils.py'))
spec = importlib.util.spec_from_file_location("utils", utils_path)
utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(utils)

save_data = utils.save_data

st.title("Thought Composer")

st.markdown("Describe your intention or thought below. The system will interpret it into pseudo-code.")

user_thought = st.text_area("Your Thought", placeholder="e.g., I want to comfort someone who feels lost tomorrow.")

if st.button("Compose Logic"):
    if user_thought:
        logic = f"# Intent: {user_thought}\nif future.user_emotion == 'lost':\n    send_message('You are not alone.')"
        st.subheader("Interpreted Logic")
        st.code(logic, language="python")
        save_data("data/thoughts.json", str(uuid.uuid4()), {"thought": user_thought, "logic": logic})
    else:
        st.warning("Please enter a thought to compose logic.")

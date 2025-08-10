import streamlit as st
import uuid
import datetime
import importlib.util
import os

utils_path = os.path.abspath(os.path.join(os.path.dirname( *file*), '..', 'utils.py'))
spec = importlib.util.spec_from_file_location("utils", utils_path)
utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(utils)

save_data = utils.save_data

st.title("Temporal Logic")

st.markdown("Define logic that reacts to time-based conditions or future events.")

event = st.text_input("Event Description", placeholder="e.g., User feels anxious on Sunday")
trigger_date = st.date_input("Trigger Date", value=datetime.date.today())
response = st.text_area("Response Action", placeholder="e.g., Send calming message")

if st.button("Generate Temporal Logic"):
    if event and response:
        logic = {
            "event": event,
            "trigger_date": str(trigger_date),
            "response": response
}
        st.subheader("Generated Logic")
        st.json(logic)
        save_data("data/logic.json", str(uuid.uuid4()), logic)
    else:
        st.warning("Please fill in all fields to generate logic.")

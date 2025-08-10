import streamlit as st
import uuid
import importlib.util
import os

utils_path = os.path.abspath(os.path.join(os.path.dirname( *file*), '..', 'utils.py'))
spec = importlib.util.spec_from_file_location("utils", utils_path)
utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(utils)

save_data = utils.save_data

st.title("Dream Debugger")

st.markdown("Visualize your logic as a narrative journey. Enter your logic steps below.")

steps = st.text_area("Logic Steps (one per line)", placeholder="e.g.\nCheck emotion\nTrigger response\nLog interaction")

if st.button("Visualize Journey"):
    if steps:
        st.subheader("Narrative Flow")
        journey = []
        for i, step in enumerate(steps.splitlines(), start=1):
            if step.strip():
                st.markdown(f"Step {i}: {step.strip()}")
                journey.append(f"Step {i}: {step.strip()}")
        save_data("data/logic.json", str(uuid.uuid4()), {"journey": journey})
    else:
        st.warning("Please enter logic steps to visualize.")

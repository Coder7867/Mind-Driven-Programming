import streamlit as st

st.title("Dream Debugger")

st.markdown("Visualize your logic as a narrative journey. Enter your logic steps below.")

steps = st.text_area("Logic Steps (one per line)", placeholder="e.g.\nCheck emotion\nTrigger response\nLog interaction")

if st.button("Visualize Journey"):
    if steps:
        st.subheader("Narrative Flow")
        for i, step in enumerate(steps.splitlines(), start=1):
            if step.strip():
                st.markdown(f" *Step {i}:* {step.strip()}")
    else:
        st.warning("Please enter logic steps to visualize.")

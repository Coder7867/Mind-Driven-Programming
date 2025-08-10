import streamlit as st
import importlib.util
import os
import uuid

utils_path = os.path.abspath(os.path.join(os.path.dirname( *file*), '..', 'utils.py'))
spec = importlib.util.spec_from_file_location("utils", utils_path)
utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(utils)

save_data = utils.save_data

st.title("Manifesto")

st.markdown("""
Mind-Driven Programming is built on the belief that code should reflect human intention, emotion, and time-awareness.

This system explores a future where:
- Logic is shaped by thought, not syntax
- Emotional tone influences behavior
- Time is a first-class citizen in programming
- Debugging becomes a journey, not just a fix

We envision tools that feel intuitive, empathetic, and alive—where programming becomes a natural extension of human cognition.

This is not just a framework. It’s a philosophy.
""")

save_data("data/messages.json", str(uuid.uuid4()), {"manifesto": "Mind-Driven Programming philosophy saved."})

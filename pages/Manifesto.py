import streamlit as st
from utils import save_data
import uuid

st.title("Manifesto")

st.markdown("""
Mind-Driven Programming is built on the belief that code should reflect human intention, emotion, and time-awareness.

This system explores a future where:
- Logic is shaped by thought, not syntax
- Emotional tone influences behavior
- Time is a first-class citizen in programming
- Debugging becomes a journey, not just a fix

We envision tools that feel intuitive, empathetic, and alive.

""")

save_data("data/messages.json", str(uuid.uuid4()), {"manifesto": "Mind-Driven Programming philosophy saved."})

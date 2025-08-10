import streamlit as st
import importlib.util
import os

utils_path = os.path.abspath(os.path.join(os.path.dirname( __file__), '..', 'utils.py'))
spec = importlib.util.spec_from_file_location("utils", utils_path)
utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(utils)

load_data = utils.load_data

st.title("Data Viewer")

st.markdown("Browse all saved thoughts, logic, and messages.")

def show_entries(title, file_path):
    st.subheader(title)
    data = load_data(file_path)
    if data:
        for key, entry in data.items():
            with st.expander(f"Entry {key}"):
                st.json(entry)
    else:
        st.info("No entries found.")

show_entries("Thoughts", "data/thoughts.json")
show_entries("Logic", "data/logic.json")
show_entries("Messages", "data/messages.json")

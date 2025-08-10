import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

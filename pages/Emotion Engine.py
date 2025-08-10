import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import save_data, load_data
import uuid

st.title("Emotion Engine")

st.markdown("Select an emotional tone to modify the behavior or message of your logic.")

message = st.text_area("Base Message", placeholder="e.g., You are not alone.")
tone = st.selectbox("Emotional Tone", ["Gentle", "Urgent", "Warm", "Reflective", "Neutral"])

def apply_tone(msg, tone):
    modifiers = {
        "Gentle": "Softly say: ",
        "Urgent": "Immediately alert: ",
        "Warm": "With care, express: ",
        "Reflective": "Thoughtfully share: ",
        "Neutral": ""
}
    return modifiers.get(tone, "") + msg

if st.button("Apply Tone"):
    if message:
        modified = apply_tone(message, tone)
        st.subheader("Modified Message")
        st.write(modified)
        save_data("data/messages.json", str(uuid.uuid4()), {"message": message, "tone": tone, "modified": modified})
    else:
        st.warning("Please enter a message to apply tone.")

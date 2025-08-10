import streamlit as st

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
    else:
        st.warning("Please enter a message to apply tone.")

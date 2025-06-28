import streamlit as st
import json

# Load your knowledge base
with open("aircraft_info.json", "r") as f:
    aircraft_db = json.load(f)

# Simple summarizer function
def summarize_aircraft(model_query):
    found = None
    for entry in aircraft_db:
        if model_query.lower() in entry["model"].lower():
            found = entry
            break
    if not found:
        return f"❌ Sorry, no data found for '{model_query}'."
    
    summary = (
        f"✈️ **Model:** {found['model']}\n\n"
        f"🛠️ **Manufacturer:** {found['manufacturer']}\n\n"
        f"📅 **Year Introduced:** {found['year_introduced']}\n\n"
        f"🔧 **Engines:** {found['engines']}\n\n"
        f"🧩 **Known Issues:** {found['known_issues']}\n\n"
        f"📝 **Incident Notes:** {found['incident_notes']}\n\n"
        f"🔄 **Maintenance Interval:** {found['maintenance_interval']}\n\n"
        f"👥 **Passenger Capacity:** {found['passenger_capacity']}"
    )
    return summary

# Streamlit UI
st.set_page_config(page_title="Flight Safety Summarizer", page_icon="✈️")
st.title("🛫 Flight Safety Summarizer AI")
st.markdown(
    """
    *Get a quick, human-friendly summary about the aircraft you are flying.*  
    Enter a model like **Boeing 777** or **A320neo** below:
    """
)

query = st.text_input("Enter aircraft model:")

if query:
    with st.spinner("Retrieving information..."):
        result = summarize_aircraft(query)
        st.markdown(result)

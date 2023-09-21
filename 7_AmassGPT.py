import streamlit as st
import subprocess

# Streamlit app title and description
st.title("OWASP Amass GUI")
st.write("Use this app to run OWASP Amass with various switches.")

# Input field for specifying the target domain
domain = st.text_input("Enter the target domain:")

# Text area for specifying additional Amass switches
amass_options = st.text_area("Amass Additional Options", " -active -v")

if st.button("Preview syntax"):
    amass_preview = f"amass intel -org {domain} {amass_options}"
    st.write(amass_preview)

# Button to run Amass
if st.button("Run Amass"):
    # Build the Amass command
    amass_command = f"amass intel -org {domain} {amass_options}"

    # Run Amass using subprocess
    try:
        result = subprocess.run(
            amass_command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        # Display the Amass output
        st.subheader("Amass Output:")
        st.code(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(f"Error running Amass: {e.stderr}")

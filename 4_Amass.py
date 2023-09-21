from pyarrow import NULL
import streamlit as st
import subprocess

# Streamlit app title and description
st.title(" :eyes: AMASS GUI :eyes: ")
st.write("Use this app to run Amass.")

amass_out = ""
# Input field for specifying the target host or IP address
host = st.text_input("Enter the target compant, host,  or IP address:")

# Dropdown to select scan type
scan_type = st.selectbox("Select the scan type:", ["intel", "enum", "viz", "track", "db"])

# Text area for custom scan options
custom_options = st.text_area("Custom Scan Options (if applicable)", "--org")

# Button to run the scan
if st.button("Run Scan"):
    # Build the Nmap command based on the selected scan type
    if scan_type == "intel":
        amass_command = f"amass intel {custom_options} {host}"
    elif scan_type == "enum":
        amass_command = f"amass enum {host}"
    else:
        amass_command = f"amass {custom_options} {host}"

    # Run the Nmap scan using subprocess
    try:
        result = subprocess.run(
            amass_command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        # Display the Nmap scan results
        st.subheader("AMASS Scan Results:")
        amass_out = st.code(result.stdout)
                                                 
    except subprocess.CalledProcessError as e:
        st.error(f"Error running AMASS: {e.stderr}")

with st.sidebar:
    st.write('See Examples')
    try:
        if scan_type == 'intel':
            st.write('See Amass INTEL examples')
        if scan_type == 'enum':
            st.write('See Amass ENUM examples')
        if scan_type == NULL:
            st.write('Standard Amass Syntax.')
        else:
            pass
    except:
        st.write("ERROR")
        
def sidb():
    with st.sidebar:
        st.write('hello')

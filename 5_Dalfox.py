
import streamlit as st
import subprocess

# Streamlit app title and description
st.title(" :fox_face: Dalfox GUI :fox_face: ")
st.write("Use this app to run Dalfox.")

with st.expander("See Help Section......"):
    st.write("HELLO HELLO")

nmap_out = ""
# Input field for specifying the target host or IP address
host = st.text_input("Enter the target host or IP address:")

# Dropdown to select scan type
scan_type = st.selectbox("Select the scan type:", ["URL (single)", "URL File", "THIRD OPTION IS????"])

# Text area for custom scan options
custom_options = st.text_area("Custom Scan Options (if applicable)", "--verbose")

# Button to run the scan
if st.button("Run Scan"):
    # Build the Nmap command based on the selected scan type
    if scan_type == "URL (single)":
        nmap_command = f"dalfox url {host}"
    elif scan_type == "Full Scan":
        nmap_command = f"dalfox file -v {host}"
    else:
        nmap_command = f"dalfox {custom_options} {host}"

    # Run the Nmap scan using subprocess
    try:
        result = subprocess.run(
            nmap_command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        # Display the Nmap scan results
        st.subheader("Dalfox Scan Results:")
        nmap_out = st.code(result.stdout)
                                                 
    except subprocess.CalledProcessError as e:
        st.error(f"Error running Nmap: {e.stderr}")

with st.sidebar:
    
    st.write('SIDEBAR TEXT')
    try:
        if nmap_out != NULL: 
            st.write('WE Have RESULTS.')
        if nmap_out == NULL:
            st.write('No Results Available.')
        else:
            pass
    except:
        st.write("ERROR")
        
def sidb():
    with st.sidebar:
        st.write('hello')

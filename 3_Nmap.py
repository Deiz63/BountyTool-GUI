import streamlit as st
import subprocess
from pyarrow import NULL
# Streamlit app title and description
st.title("Nmap GUI")
st.write("Use this app to run Nmap scans.")


# Input field for specifying the target host or IP address
host = st.text_input("Enter the target host or IP address:")

# Dropdown to select scan type
scan_type = st.selectbox("Select the scan type:", ["Quick Scan", "Full Scan", "Custom Scan"])

# Text area for custom scan options
custom_options = st.text_area("Custom Scan Options (if applicable)", "--verbose --top-ports 1000 -oA ST-nmap")
nmap_out = ""
# Button to run the scan
if st.button("Run Scan"):
    # Build the Nmap command based on the selected scan type
    if scan_type == "Quick Scan":
        nmap_command = f"nmap -T4 -F {host}"
    elif scan_type == "Full Scan":
        nmap_command = f"nmap -T4 -A -v {host}"
    else:
        nmap_command = f"nmap {custom_options} {host}"

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
        st.subheader("Nmap Scan Results:")
        nmap_out = st.code(result.stdout)
        
                                             
    except subprocess.CalledProcessError as e:
        st.error(f"Error running Nmap: {e.stderr}")
      
with st.sidebar:
    
    st.write('SIDEBAR TEXT')
    try:
        if nmap_out != NULL: 
            st.write('WE Have RESULTS.')
            if st.button('I am here to show results!'):
                st.sidebar.subheader(nmap_out)
                print(result)
        if nmap_out == NULL:
            st.write('No Results Available.')
        else:
            pass
    except:
        st.write("ERROR")
        
def sidb():
    with st.sidebar:
        st.write('hello')

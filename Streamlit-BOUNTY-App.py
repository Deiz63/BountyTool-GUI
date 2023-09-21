import streamlit as st
import subprocess
from streamlitsupport import *



def run_program():
    ff_flag_base = ('ffuf -u ')
    try:
        result = subprocess.run(
            ff_flag_base.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        # Display the Nmap scan results
        st.subheader("Nmap Scan Results:")
        nmap_out = st.code(result.stdout)
        print(nmap_out)
                                                
    except subprocess.CalledProcessError as e:
        st.error(f"Error running Nmap: {e.stderr}")


def main():
    ff_flag_base = ('ffuf -u ')
    with st.expander('Click Here to Read Instructions'):
        help_section() 
        
    # MAIN FUNCTION
    option = st.selectbox(
    'Choose the tool to use?',
    ('FFUF', 'Nikto', 'Dalfox'))
    
    
# MAIN : FFUF Section
    if option == 'FFUF':
        st.subheader(" :rabbit:    FFUF for Fuzzing.....   :rabbit:")
        ffuf_options = st.selectbox('Choose options', ("SubDomain", 'SubDirectory', 'Parameter'))
        wordlist = ""
        
# FFUF : SubDomain section        
        if ffuf_options == 'SubDomain':
            st.text('dirb_small.txt')
            
            # TOGGLE DEFAULT WORDLIST    
            if st.toggle(':house:  ADD Default SubDomain WORDLIST  :house:'):
                # WITH DEFAULT WORDLIST / TOGGLE ON
                st.text('SubDomain Default Wordlist Added')
                st.divider()
                wordlist += ('dirb_small.txt')
                url_input = st.text_input("Enter URL : 👇<  http://FUZZ.********.com  >   👇 :  Include FUZZ keyword" )
                st.divider()
                
                ff_flag1 = ('ffuf -u https://FUZZ.example.com -w ' + wordlist)
                ff_flag2 = ('ffuf -u https://FUZZ.example.com <OTHER> -w ' + wordlist)
                if url_input:
                    # WHEN URL IS ENTERED
                    st.text('URL = ' + url_input)
                    ffuf_command1 = (ff_flag_base + url_input + ' -w ' + wordlist)
                    if st.button(ffuf_command1):
                        # Syntax Button 1 Pressed
                        st.text('Command Ran =  : ' + ffuf_command1)
                        #subprocess.run(['cd Tools'])
                        #subprocess.run(['C:\Tools\ffuf -h'])
                        # Run the Nmap scan using subprocess
                        run_program()
                                            
                       
                                 
                    if st.button(ffuf_command1 + ' -recursion'):
                        # Syntax Button 2 Pressed
                        st.text('Command Ran = : ' + ffuf_command1 + ' -recursion') 
                        run_program()
            else:
                # WITHOUT DEFAULT WORDLIST / TOGGLE OFF           
                st.text('Default wordlist NOT chosen')
                st.divider()   
                wordlist_input = st.text_input('Please Enter Wordlist Location. ')  
                if wordlist_input:               
                    # CUSTOM WORDLIST ENTERED
                    wordlist += wordlist_input
                    st.text('Chosen WORDLIST = ' + wordlist)
                    st.divider()
                    ff_flag_base = ('C:\/Tools\/ffuf\/ffuf.exe -u ')
                    ff_flag1 = ('ffuf -u https://FUZZ.example.com -w ' + wordlist)
                    ff_flag2 = ('ffuf -u https://FUZZ.example.com <OTHER> -w ' + wordlist)
                    
                    url_input = st.text_input("Enter URL : 👇<  https://FUZZ.********.com  >   👇 :  Include FUZZ keyword")
                    if url_input:
                        # URL ENTERED
                        st.text('URL = ' + url_input)
                        ffuf_command1 = (ff_flag_base + url_input + ' -w ' + wordlist)
                        if st.button(ffuf_command1):
                            # First Button Pressed
                            st.text('RAN COMMAND : ' + ffuf_command1 + 'completeme')
                        if st.button(ffuf_command1 + ' -recursion'):
                            # Second Button Pressed
                            st.text('RAN COMMAND : ' + ffuf_command1 + '<OTHER>' + 'completeme') 
                    else:
                        st.button('I will disappear')            
                
# SubDomain - ALWAYS RAN/ACTIVE WHEN SUBDOMAIN CHOSEN ???                 
                                                                                        
                
            
# FFUF : SuDirectory Section            
        if ffuf_options == 'SubDirectory':
            st.text('/usr/share/seclists/subdirectories.txt')
            if st.toggle(':door:  ADD Default SubDirectory WORDLIST  :door:'):
                st.divider()
                st.text('SubDirectory Default Wordlist Added')
                wordlist += ('/usr/share/seclists/subdirectory.txt')
            else:
                st.text('no wordlist chosen')   
                wordlist_input = st.text_input('Please Enter Wordlist Location. ')  
                return wordlist_input
                
            st.divider()
            ff_flag_base = ('ffuf -u ')
            ff_flag1 = ('ffuf -u ' + 'https://example.com/FUZZ' + ' -w ' + wordlist)
            ff_flag2 = ('ffuf -u https://example.com/FUZZ' + '<OTHER>' + ' -w ' + wordlist)
                       
            if st.button(ff_flag1):
                print('Button Pressed')
                os.system(ff_flag1)
            if st.button(ff_flag2):
                print('Button Pressed')
                os.system(ff_flag2)
                
            text_input = st.text_input("Enter URL 👇")
                
# FUFF : Parameter Section              
        if ffuf_options == 'Parameter':
            st.text('/usr/share/seclists/parameters.txt')
            if st.toggle(':thermometer:  ADD Default Parameter WORDLIST  :thermometer:'):
                st.divider()
                st.text('Default Parameter Wordlist Added')
                wordlist += ('/usr/share/seclists//parameters.txt')
            else:
                st.text('no wordlist chosen')   
                wordlist_input = st.text_input('Please Enter Wordlist Location. ')
                return wordlist_input 
            st.divider()
            ff_flag_base = ('ffuf -u ')
            ff_flag1 = ('ffuf -u http://example.com?FUZZ -w ' + wordlist)
            ff_flag2 = ('ffuf -u http://example.com?FUZZ <OTHER> -w' + wordlist)
            
            st.button(ff_flag1)
            st.button(ff_flag2)
            
        if ffuf_options ==None:
            pass   
         
    
# SIDEBAR FILE UTILITY
def Sidebar_Util():
    with st.sidebar:
        # Page title
        st.title("Text File Uploader and Viewer")
        # Upload file
        uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

        # Display file contents
        if uploaded_file is not None:
            st.subheader("File Contents:")
            file_contents = uploaded_file.read()
            st.text(file_contents)
            st.divider()
            # You can perform further analysis or processing here if needed.
            # For example, you can count words, characters, or perform text analysis.

            # Example: Counting words and characters
            word_count = len(file_contents.split())
            char_count = len(file_contents)

            st.write(f"Word Count: {word_count}")
            st.write(f"Character Count: {char_count}")
            
        
        if st.button("VIEW FILE"):
            # Get PDF files
            with st.spinner("Processing files......."):
                st.divider()
                st.subheader(file_contents)
    return uploaded_file                   
#ADD TOOLS to web-app
#Add any other options to app 
#Create Functions to Run tool against chosen wordlist 
#Create Functions to View other Details / Files / Etc.                             

start = main()
side = Sidebar_Util()

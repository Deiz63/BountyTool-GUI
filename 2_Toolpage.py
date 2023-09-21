import streamlit as st
import os
 
    
def main():
    st.set_page_config(page_title="2_Toolpage")
    st.divider()
    st.write('CLI Helper GUI')
    st.checkbox(" :moon: PLEASE CHECK ME !!! :stars: ")
    if st. button("Click me for Sidebar."):
        st.sidebar.button("I am a new button")
        with st.sidebar:
            st.write("What options / utilities shoudl we put here?")
            sys_comnd = os.listdir('/') 
            with st.expander('Show Results'):
                st.write(sys_comnd)
    
    
    
    
    with st.expander('Click Here to Read Instructions'):
        st.write(' :bow_and_arrow: Choose Your Tool from the Drop Down Menu. Then Follow Tool Logic and press Button to run') 
    # MAIN FUNCTION
    
    
# MAIN : FFUF Section
    
    st.subheader(" :alien:    OWASP Amass : Recon Tool   :cat:")
    ffuf_options = st.selectbox('Choose options', ('intel', 'enum', 'viz', 'track', 'db'))
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
            text_input = st.text_input("Enter URL : 👇<  http://FUZZ.********.com  >   👇 :  Include FUZZ keyword" )
            st.divider()
            ff_flag_base = ('ffuf -u ')
            ff_flag1 = ('ffuf -u https://FUZZ.example.com -w ' + wordlist)
            ff_flag2 = ('ffuf -u https://FUZZ.example.com <OTHER> -w ' + wordlist)
            if text_input:
                # AFTER URL IS ENTERED
                st.text('URL = ' + text_input)
                ffuf_command1 = (ff_flag_base + text_input + ' -w ' + wordlist)
                if st.button(ffuf_command1):
                    # Syntax Button 1 Pressed
                    st.text('RAN COMMAND : ' + ffuf_command1)
                    os.system(ffuf_command1)
                if st.button(ffuf_command1 + ' -recursion'):
                    # Syntax Button 2 Pressed
                    st.text('RAN COMMAND : ' + ffuf_command1 + ' -recursion') 
            
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
                ff_flag_base = ('ffuf -u ')
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
                    if st.button(ffuf_command1 + ' <OTHER>'):
                        # Second Button Pressed
                        st.text('RAN COMMAND : ' + ffuf_command1 + '<OTHER>' + 'completeme') 
                            
main()

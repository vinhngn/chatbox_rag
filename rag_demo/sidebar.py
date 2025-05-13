from constants import SCHEMA_IMG_PATH, LANGCHAIN_IMG_PATH
import streamlit as st
import streamlit.components.v1 as components

def ChangeButtonColour(wgt_txt, wch_hex_colour = '12px'):
    htmlstr = """<script>var elements = window.parent.document.querySelectorAll('*'), i;
                for (i = 0; i < elements.length; ++i) 
                    { if (elements[i].innerText == |wgt_txt|) 
                        { elements[i].style.color ='""" + wch_hex_colour + """'; } }</script>  """

    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
    components.html(f"{htmlstr}", height=0, width=0)

def sidebar():
    with st.sidebar:

        with st.expander("OpenAI Key"):
            new_oak = st.text_input("Your OpenAI API Key")
            # if "USER_OPENAI_KEY" not in st.session_state:
            #     st.session_state["USER_OPENAI_KEY"] = new_oak
            # else:
            st.session_state["USER_OPENAI_KEY"] = new_oak

        st.markdown(f"""This the schema in which the EDGAR filings are stored in Neo4j: \n <img style="width: 70%; height: auto;" src="{SCHEMA_IMG_PATH}"/>""", unsafe_allow_html=True)

        st.markdown(f"""This is how the Chatbot flow goes: \n <img style="width: 70%; height: auto;" src="{LANGCHAIN_IMG_PATH}"/>""", unsafe_allow_html=True)

        st.markdown("""Questions you can ask of the dataset:""", unsafe_allow_html=True)

        # To style buttons closer together
        st.markdown("""
                    <style>
                        div[data-testid="column"] {
                            width: fit-content !important;
                            flex: unset;
                        }
                        div[data-testid="column"] * {
                            width: fit-content !important;
                        }
                    </style>
                    """, unsafe_allow_html=True)
        
        sample_questions = [
    """Which papers mention anomalous temperature regimes such as cold air outbreaks (CAOs) or
    warm waves (WWs) in relation to North America, specifically in the sentences where these
    terms appear?""",
    """Which papers discuss ocean circulation processes—such as thermohaline circulation—in oceanic
    regions that include either “North” or “South” in their names?""",
    """Which papers mention CMIP5 models and the North Atlantic Oscillation (NAO) in the context of the Southeast United States?""",
    """Which papers mention the Pacific-North American (PNA) pattern in connection with locations in the United States?""",
    """What ocean circulation processes are associated with the Southern Ocean and mentioned in
connection with upwelling?"""
        ]

        for text, col in zip(sample_questions, st.columns(len(sample_questions))):
            if col.button(text, key=text):
                st.session_state["sample"] = text

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Configure page and theme
st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🎓",
    layout="wide",
)

# Custom CSS for dark theme
st.markdown("""
    <style>
        .stApp {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        .stButton>button {
            background-color: #262730;
            color: #FAFAFA;
            border: 1px solid #4F4F4F;
        }
        .stButton>button:hover {
            background-color: #363940;
            color: #FFFFFF;
        }
        .css-1d391kg {
            background-color: #1E1E1E;
        }
        .stTextInput>div>div>input {
            background-color: #262730;
            color: #FAFAFA;
        }
        .stSelectbox>div>div {
            background-color: #262730;
            color: #FAFAFA;
        }
        div[data-baseweb="select"] {
            background-color: #262730;
        }
        div[class^='stMarkdown'] {
            color: #FAFAFA;
        }
        .info-box {
            background-color: #1E1E1E;
            padding: 1rem;
            border-radius: 10px;
            border: 1px solid #333333;
        }
    </style>
""", unsafe_allow_html=True)

LEARNING_PATHS = {
    "Spreadsheet Skills (LibreOffice)": {
        "Topics": ["Basic Operations", "Data Entry & Formatting", "Formulas & Functions", "Data Analysis"],
        "Prompts": {
            "Basic Operations": [
                "Show me how to create and save a new spreadsheet in LibreOffice Calc",
                "Guide me through the basic interface and tools in LibreOffice Calc",
                "Demonstrate how to manage multiple sheets in a workbook"
            ],
            "Data Entry & Formatting": [
                "Show me how to format cells for different data types (text, numbers, dates)",
                "Demonstrate efficient ways to copy, paste, and move data",
                "Guide me through creating professional-looking tables"
            ],
            "Formulas & Functions": [
                "Show me how to create basic arithmetic formulas",
                "Demonstrate using SUM, AVERAGE, MIN, and MAX functions",
                "Guide me through using relative vs absolute cell references"
            ],
            "Data Analysis": [
                "Show me how to sort and filter data",
                "Guide me through creating basic charts and graphs",
                "Demonstrate how to use pivot tables for data analysis"
            ]
        }
    },
    "Web Browser Skills": {
        "Topics": ["Navigation", "Bookmarks", "Advanced Features", "Web Research"],
        "Prompts": {
            "Navigation": [
                "Show me how to efficiently navigate between multiple tabs in Firefox",
                "Demonstrate using keyboard shortcuts for browser navigation",
                "Guide me through the Firefox address bar features"
            ],
            "Bookmarks": [
                "Show me how to organize bookmarks in Firefox",
                "Guide me through creating and managing bookmark folders",
                "Demonstrate how to import/export bookmarks"
            ],
            "Advanced Features": [
                "Show me how to use Firefox's privacy features",
                "Guide me through customizing Firefox settings",
                "Demonstrate how to use Firefox's developer tools"
            ],
            "Web Research": [
                "Show me efficient web search techniques",
                "Guide me through evaluating online sources",
                "Demonstrate advanced search operators in Firefox"
            ]
        }
    },
    "Terminal Mastery": {
        "Topics": ["Basic Commands", "File Management", "System Navigation", "Advanced Usage"],
        "Prompts": {
            "Basic Commands": [
                "Show me essential terminal commands for beginners",
                "Guide me through using ls, cd, and pwd commands",
                "Demonstrate how to get help for terminal commands"
            ],
            "File Management": [
                "Show me how to create, move, and delete files in terminal",
                "Guide me through file permissions and chmod",
                "Demonstrate using grep and find commands"
            ],
            "System Navigation": [
                "Show me how to navigate between directories efficiently",
                "Guide me through using path shortcuts and environment variables",
                "Demonstrate how to find and change directory locations"
            ],
            "Advanced Usage": [
                "Show me how to use pipe commands and redirections",
                "Guide me through creating and running shell scripts",
                "Demonstrate advanced text processing with sed and awk"
            ]
        }
    },
    "Image Editing": {
        "Topics": ["Basic Editing", "File Management", "Drawing Tools", "Effects"],
        "Prompts": {
            "Basic Editing": [
                "Show me how to resize and crop images",
                "Guide me through basic color adjustments",
                "Demonstrate how to save in different file formats"
            ],
            "File Management": [
                "Show me how to organize and manage image files",
                "Guide me through bulk image operations",
                "Demonstrate image format conversion techniques"
            ],
            "Drawing Tools": [
                "Show me how to use basic drawing tools",
                "Guide me through creating simple shapes and lines",
                "Demonstrate text addition and formatting in images"
            ],
            "Effects": [
                "Show me how to apply basic image effects",
                "Guide me through using filters and adjustments",
                "Demonstrate how to enhance image quality"
            ]
        }
    },
    "PDF Skills": {
        "Topics": ["Navigation", "Annotations", "Form Filling", "Organization"],
        "Prompts": {
            "Navigation": [
                "Show me how to efficiently navigate PDFs",
                "Guide me through using the PDF viewer's search features",
                "Demonstrate how to use PDF bookmarks and thumbnails"
            ],
            "Annotations": [
                "Show me how to add comments and highlights to PDFs",
                "Guide me through using different annotation tools",
                "Demonstrate how to manage and review annotations"
            ],
            "Form Filling": [
                "Show me how to fill out PDF forms",
                "Guide me through saving and printing filled forms",
                "Demonstrate how to add digital signatures"
            ],
            "Organization": [
                "Show me how to organize PDF pages",
                "Guide me through merging and splitting PDFs",
                "Demonstrate how to manage PDF portfolios"
            ]
        }
    },
    "Text Editor": {
        "Topics": ["Basic Editing", "File Operations", "Advanced Features"],
        "Prompts": {
            "Basic Editing": [
                "Show me how to create and edit text files",
                "Guide me through copy, cut, and paste operations",
                "Demonstrate text formatting features"
            ],
            "File Operations": [
                "Show me how to save and manage text files",
                "Guide me through file encoding options",
                "Demonstrate how to work with multiple documents"
            ],
            "Advanced Features": [
                "Show me how to use find and replace",
                "Guide me through using regular expressions",
                "Demonstrate advanced text manipulation techniques"
            ]
        }
    },
    "Calculator Usage": {
        "Topics": ["Basic Operations", "Scientific Functions", "Memory Features"],
        "Prompts": {
            "Basic Operations": [
                "Show me how to perform basic calculations",
                "Guide me through using calculator memory functions",
                "Demonstrate scientific calculation features"
            ],
            "Scientific Functions": [
                "Show me how to use trigonometric functions",
                "Guide me through logarithmic calculations",
                "Demonstrate statistical operations"
            ],
            "Memory Features": [
                "Show me how to store and recall numbers",
                "Guide me through using multiple memory slots",
                "Demonstrate chained calculations with memory"
            ]
        }
    }
}

def main():
    # Header with dark theme styling
    st.title("🎓 Interactive Computer Skills Learning Assistant")
    
    st.markdown("""
        <div class="info-box">
            <h3 style='color: #FAFAFA;'>Welcome to Your Personal Learning Journey!</h3>
            <p style='color: #FAFAFA;'>Select a skill path, choose a topic, and get personalized guidance from Claude.</p>
            <p style='color: #FAFAFA;'>Claude will demonstrate each step in a live environment, helping you learn by doing.</p>
        </div>
    """, unsafe_allow_html=True)

    # Main content in columns
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("🎯 Choose Your Learning Path")
        
        path = st.selectbox(
            "Select Skill Area",
            list(LEARNING_PATHS.keys()),
            key="path_select"
        )
        
        topic = st.selectbox(
            "Choose Specific Topic",
            LEARNING_PATHS[path]["Topics"],
            key="topic_select"
        )
        
        st.subheader("📝 Suggested Learning Prompts")
        
        for prompt in LEARNING_PATHS[path]["Prompts"].get(topic, []):
            if st.button(
                f"▶️ {prompt}",
                key=prompt,
                help="Click to use this prompt"
            ):
                st.session_state.current_prompt = prompt

    with col2:
        st.subheader("✨ Customize Your Learning Experience")
        
        if 'current_prompt' not in st.session_state:
            st.session_state.current_prompt = ""
        
        st.markdown("""
            <div class="info-box">
                <h4 style='color: #FAFAFA;'>🌟 Tips for Effective Learning:</h4>
                <ul style='color: #FAFAFA;'>
                    <li>Be specific about what you want to learn</li>
                    <li>Mention your experience level</li>
                    <li>Ask for step-by-step guidance</li>
                    <li>Request demonstrations of specific features</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        custom_prompt = st.text_area(
            "Your Learning Request",
            value=st.session_state.current_prompt,
            height=150,
            help="Modify the suggested prompt or write your own"
        )

        if custom_prompt:
            st.markdown("""<div class="info-box">""", unsafe_allow_html=True)
            st.markdown("### 📋 Your Learning Prompt")
            st.code(custom_prompt, language="text")
            st.markdown("</div>", unsafe_allow_html=True)

        with st.expander("🔍 Quick Reference Guide"):
            st.markdown("""
                <div class="info-box">
                    <h3 style='color: #FAFAFA;'>Making the Most of Your Learning Session</h3>
                    <ol style='color: #FAFAFA;'>
                        <li><strong>Be Interactive</strong>
                            <ul>
                                <li>Ask follow-up questions</li>
                                <li>Request clarification when needed</li>
                                <li>Try things out as you learn</li>
                            </ul>
                        </li>
                        <li><strong>Track Your Progress</strong>
                            <ul>
                                <li>Take notes of key points</li>
                                <li>Practice each new skill</li>
                                <li>Review and reinforce learning</li>
                            </ul>
                        </li>
                    </ol>
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
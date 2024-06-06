import streamlit as st
import requests
from PIL import Image
import os

im = Image.open("Garden Guru Favicon round.png")
st.set_page_config(
    page_title="Garden Guru",
    page_icon=im,
)



# Using CSS to change background color
st.markdown(
    """
    <style>
    
    
        .stApp {
            background-color: #f6f4e8ff
        }
                /* Targeting Streamlit's input elements */
        .input {
            background-color: #4a5742;
            color: white;  /* Change text color for better visibility */
        }
      .st-bc {
         color: #3e4c35ff;
            background-color: #f1e9e0ff;
        }
    .st-emotion-cache-1gulkj5 {
         display: flex;
        -webkit-box-align: center;
         align-items: center;
          padding: 1rem;
          background-color: #f1e9e0ff;
          border-radius: 0.5rem;
          color: #3e4c35ff;
}
        .textarea {
            background-color: #4a5742;
            color: white;  /* Change text color for better visibility */
        }
        .stTextInput > div > input {
            background-color: #4a5742 !important;
            color: white !important;  /* Change text color for better visibility */
        }
        .stTextArea > div > textarea {
            background-color: #4a5742 !important;
            color: white !important;  /* Change text color for better visibility */
        }
        h1 {
            color: #4a5742;
        }
        
        h2 {
            color: #c37967;
        }
     
        p {
            color: #161616;
        }
        
        button {
            color: #4a5742;
        }
        
    .st-emotion-cache-7ym5gk:hover {
    border-color: #4a5742;
    color: #161616;
    background-color: #4a5742;
}

    .st-emotion-cache-7ym5gk:focus {
    border-color: #4a5742;
    background-color: #4a5742;
}


        
    </style>
    """,
    unsafe_allow_html=True
)
API_HOST=os.environ['API_HOST']

# Defining FastAPI Endpoints
prediction_url = f"{API_HOST}/prediction"
chat_url = f"{API_HOST}/chat"

# Home endpoint response
st.header("Welcome to")

# Setting up the Streamlit Application Title
st.title("Garden Guru 🪴")

# Home endpoint response
st.header("Let me guide you on your green journey ✨")
home_response = requests.get(f"{API_HOST}/")
st.write(home_response.json().get("message", "No welcome message available."))

# Image upload section
st.header("Show me your plant:") # Adds a header for the image upload section
uploaded_file = st.file_uploader("Choose an image...", type="jpg") # Provides a file uploader widget that accepts JPG images

plant_class = 'houseplant'
# Handling the Uploaded Image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Meditating on how to take care of your green protegé...")

    # Save the uploaded file to a temporary location
    # with open(f"raw_data/{uploaded_file.namefile}", "wb") as f:
    #     f.write(uploaded_file.getbuffer())
    
    # Send image to FastAPI for prediction
    # with open(f"raw_data/{uploaded_file.namefile}","rb") as f:
    files = {"file": uploaded_file.getbuffer()}
    response = requests.post(prediction_url, files=files).json()
    care_tips = response.get("text", "No care tips available, follow your heart. 💚")
    plant_class = response.get("plant")

    st.write(f"{care_tips}")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chatbot section
st.header("Need more answers? I am here to help. 😊")
user_prompt = st.text_input("What would you like to find out?")

# Handling the User's Question
if st.button("Ask"):
    if plant_class and user_prompt:
        params = {"plant_class": plant_class, "user_prompt": user_prompt}
        response = requests.get(chat_url, params=params)
        chat_response = response.json().get("response", "No response available.")

        # Append user prompt and response to chat history
        st.session_state.chat_history.append({"user": user_prompt, "bot": chat_response})

        # Display the chat history
        for chat in st.session_state.chat_history:
            st.write(f"You: {chat['user']}")
            st.write(f"Garden Guru: {chat['bot']}")
    else:
        st.write("Please enter your question.")

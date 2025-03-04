import streamlit as st
import speech_recognition as sr
import webbrowser


st.title("🤖 WebWhisper 🔊🌐")
st.markdown("*Speak any website name with a command like Chatgpt or Instgram...*")




def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... ")
        try:
            audio = recognizer.listen(source, timeout=20)
            text = recognizer.recognize_google(audio).lower()
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand."
        except sr.RequestError:
            return "Could not request results, please check your internet."
        except sr.WaitTimeoutError:  
            return "⏳ You did not speak!"


if st.button("🎙 Speak Now"):
    command = recognize_speech()
    st.write(f"\n \t Voice : **{command}**")

    words = command.split() 
    site_name = None

    for word in words:
        if word in ["open", "launch", "start", "go", "visit"]:
            continue 
        else:
            site_name = word  
            break

    if site_name:
        url = f"https://www.{site_name}.com"
        webbrowser.open(url)
        st.success(f"Opening {site_name}...")
    else:
        st.error("Couldn't detect a website name!")

st.write()




with st.expander("ℹ️ How It Works?"):
    st.write("""
    - **Click the "🎙 Speak Now" button**  
    - **App converts your speech to text** 📝  
    - **Automatically generates a URL and opens the website!** 🌍  

    ### 💡 **No Need to Manually Add Websites!**  
    This app dynamically converts your voice input into a URL – just **say any website name** and it will open instantly!  
    """)

    

with st.sidebar:
    st.write("""
    ## 🤖 **What is a Logic-Based Mini App?**  
    - A **mini app** is a lightweight application designed for **a specific task**.  
    - A **logic-based app** means that it follows **predefined rules** or **conditions** to perform actions.  
    - This app works on an **IF-ELSE logic**, where it detects your voice input and **matches it with predefined website names** to open the right page.
    """)

    st.markdown(" **<center> **Built by Sabahat Shakeel 💖**</center>**", unsafe_allow_html=True)

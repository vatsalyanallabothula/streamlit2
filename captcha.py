import streamlit as st
import random

st.title("CAPTCHA — Human vs Bot Security Check")
st.header("What is CAPTCHA?")
st.write("""
**CAPTCHA** stands for **Completely Automated Public Turing test to tell Computers and Humans Apart**.  
It is a security mechanism used on websites to check whether the user is a **real human** or a **bot**.
""")

st.header("Why is CAPTCHA Used?")
st.write("""
CAPTCHA helps protect websites from harmful automated actions like:
- Creating fake accounts
- Submitting spam comments/forms
- Brute force login attacks
- Auto-buying tickets/products before humans
""")

st.header("How does CAPTCHA Work?")
st.write("""
It gives a **small test** that:
- Humans can easily solve  
- Bots find difficult or impossible  

Examples of such tests:
- Identify images with traffic lights or buses
- Type distorted text shown in image
- Solve a basic math question
- Click “I am not a robot” checkbox
""")

st.header("Types of CAPTCHA")
st.write("""
1) **Text-based CAPTCHA** – Type the shown letters/numbers  
2) **Image CAPTCHA** – Select specific images (e.g., traffic lights)  
3) **Math CAPTCHA** – Simple addition/subtraction  
4) **Audio CAPTCHA** – For visually impaired users  
5) **reCAPTCHA (Google)** – Behaviour-based AI check  
""")

st.divider()
st.subheader("Try a Simple Math CAPTCHA")
if "a" not in st.session_state:
    st.session_state.a = random.randint(1,10)
    st.session_state.b = random.randint(1,10)

st.write("Solve:", st.session_state.a, "+", st.session_state.b, "= ?")

ans = st.text_input("Your answer")

if ans:
    if ans.isdigit() and int(ans) == st.session_state.a + st.session_state.b:
        st.success("Correct ✅")
    else:
        st.error("Wrong ❌")


import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Function to calculate BMI
def calculate_bmi(weight: float, height_m: float) -> float:
    return weight / (height_m ** 2)

# Function to determine BMI category
def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# UI Enhancements
st.image("https://cdn-icons-png.flaticon.com/512/2434/2434887.png", width=100)
st.title("💪 BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) quickly and easily!")

# Input columns for weight and height
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)

with col2:
    height_feet = st.number_input("Enter your height (feet):", min_value=0, step=1)
    height_inches = st.number_input("Additional height (inches):", min_value=0, max_value=11, step=1)

# Convert height to meters
height_m = ((height_feet * 12) + height_inches) * 0.0254

# Calculate and display BMI
if st.button("Calculate BMI"):
    if height_m > 0:
        bmi = calculate_bmi(weight, height_m)
        category = bmi_category(bmi)
        
        with st.spinner('Calculating...'):
            st.metric(label="Your BMI", value=f"{bmi:.2f}", delta=f"Category: {category}")
            st.success(f"Result: {category}")
        
        # Progress bar animation
        progress = st.progress(0)
        for i in range(100):
            progress.progress(i + 1)
    else:
        st.error("Height must be greater than 0.")

# 🎨 Sidebar Enhancements
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4359/4359879.png", width=100)
st.sidebar.header("ℹ️ About BMI")
st.sidebar.info("""
Body Mass Index (BMI) is a measurement of a person's weight relative to their height. 
It is often used as an indicator of healthy body weight.
""")

# Add navigation links and health tips
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Useful Links")
st.sidebar.write("[What is BMI?](https://www.cdc.gov/healthyweight/assessing/bmi/index.html)")
st.sidebar.write("[Healthy BMI Range](https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight)")

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Health Tips")
st.sidebar.success("Maintain a balanced diet 🍎")
st.sidebar.info("Stay active 🚴")
st.sidebar.warning("Consult your doctor for personalized advice 👨‍⚕️")

# Add a 'Contact Us' section
st.sidebar.markdown("---")
st.sidebar.markdown("### 📬 Contact")

# Email Link
st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")

# LinkedIn Link
st.sidebar.write("🔗 [Connect on LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")

# WhatsApp Link
st.sidebar.write("💬 [Chat on WhatsApp](https://wa.me/923322241405)")


# Optional user input from sidebar
st.sidebar.markdown("---")
user_goal = st.sidebar.selectbox("What's your fitness goal?", 
                                 ["Lose Weight", "Maintain Weight", "Gain Muscle", "Improve Health"])
st.sidebar.write(f"🎯 Your goal: {user_goal}")

# Footer
st.markdown("<p style='text-align: center; color: grey;'>Developed with ❤️ By Ismail Ahmed Shah</p>", unsafe_allow_html=True)


from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure the Google Generative AI client using Streamlit secrets
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to interact with Gemini Pro Vision
def get_gemini_response(image, user_prompt):
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(
        [user_prompt, image[0]]
    )
    return response.text

# Function to handle image input
def input_image(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise ValueError("No image uploaded")

# Streamlit page configuration
st.set_page_config(
    page_title="Nutritionist Generative AI Doctor",
    page_icon=":hospital:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# UI Setup
st.header("🥗 Gemini Health App – AI-Powered Nutritionist")
input = st.text_input("🔍 Enter any specific prompt or question you have (optional):", key="input")

uploaded_file = st.file_uploader("📸 Upload a food image (jpg, jpeg, png):", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    resized_image = image.resize((300, int(300 * image.height / image.width)))
    st.image(resized_image, caption="🖼️ Uploaded Image", )

submit = st.button("🍽️ Analyze Meal")

# Nutritionist Prompt
input_prompt = """
You are a certified nutritionist analyzing the food items shown in the image.

Your task:
1. Identify each food item visible in the image.
2. Estimate the calorie count for each item.
3. Break down each item into:
   - Macronutrients (carbohydrates, proteins, fats)
   - Micronutrients (vitamins, minerals if possible)
4. Provide a total estimated calorie count for the full meal.
5. Mention whether this meal is likely a Breakfast, Lunch, Dinner, or Snack.
6. Give a health rating from 1 to 10 and explain your reasoning.
7. Suggest one or two healthier alternatives or modifications (e.g., less sugar, more fiber).
8. Highlight any allergens or dangerous ingredients (e.g., excess sodium, sugar).
9. Suggest how much walking, jogging, or cycling is needed to burn this meal.
10. Provide advice like a real-world nutritionist: is this suitable for weight loss, weight gain, or maintenance?
11. Optionally, add cultural information if you recognize the dish.

Format your response in a warm and client-friendly tone.
"""

# Generate response
if submit:
    try:
        image_data = input_image(uploaded_file)
        final_prompt = input_prompt + f"\nUser note: {input}" if input else input_prompt
        response = get_gemini_response(image_data, final_prompt)
        st.subheader("🧠 Nutritionist AI Response")
        st.write(response)
    except Exception as e:
        st.error(f"❌ Error: {e}")

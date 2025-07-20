# 🥗 Nutritionist Generative AI Doctor

This is a Streamlit-based AI web application that uses Google's Gemini Pro Vision (`gemini-2.5-pro`) model to analyze food images and provide detailed nutritional insights in a friendly, professional tone—just like a real nutritionist.

---

## 📌 Features

- 📸 Upload a food image (JPG, JPEG, PNG)
- 🧠 AI identifies visible food items
- 🔬 Provides:
  - Calorie breakdown (per item & total)
  - Macronutrient & micronutrient estimates
  - Health rating (1–10) with explanation
  - Suggested meal category (breakfast/lunch/dinner/snack)
  - Diet suitability (weight loss, gain, maintenance)
  - Allergen/high-risk ingredient alerts
  - Physical activity needed to burn calories
  - Cultural insights if dish is recognized
- 📝 Optional custom prompt input for additional queries

---

## 🧠 Powered By

- [Google Generative AI](https://makersuite.google.com/app) – Gemini 2.5 Pro Vision
- [Streamlit](https://streamlit.io) – frontend UI framework
- Python, dotenv, Pillow

---

## 🚀 Quickstart

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/nutritionist-ai-doctor.git
cd nutritionist-ai-doctor
```

### 2️⃣ Create a Conda Environment

```bash
conda create -n nutritionist-ai python=3.10 -y
conda activate nutritionist-ai
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your API Key

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_google_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🖼️ How It Works

1. Upload a clear food image.
2. Optionally type your specific dietary question.
3. Click the **🍽️ Analyze Meal** button.
4. View detailed nutrition insights, calorie breakdowns, health tips, and recommendations.

---

## 🗂️ Project Structure

```
nutritionist-ai-doctor/
│
├── app.py                # Main Streamlit app
├── .env                  # Contains your API key (ignored by Git)
├── requirements.txt      # All dependencies
└── README.md             # You're reading this!
```

---

## 📦 Dependencies

```
streamlit
python-dotenv
google-generativeai
Pillow
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 💡 Example Prompts

- "Is this meal healthy for someone on a low-carb diet?"
- "Suggest a healthier alternative to this food."
- "How much should I walk to burn this meal?"
- "Is this meal suitable for weight gain?"

---

## 🛡️ FAQ

**Q: Can it handle multiple food items?**  
Yes. Gemini will list each visible item and analyze them separately.

**Q: Is the analysis accurate?**  
Estimates are based on visual cues and may not replace professional lab-grade measurement.

**Q: Do I need a Google API Key?**  
Yes. You must get your own API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

**Q: Can I deploy this on Replit or Streamlit Cloud?**  
Yes! This is lightweight and deployable on both platforms.

---



## 👨‍⚕️ Built With ❤️ by an Hemanth tempalli

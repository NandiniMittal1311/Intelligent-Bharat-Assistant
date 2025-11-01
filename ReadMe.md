Bharat Agriculture Intelligence Assistant
🧠 Overview

The Bharat Agriculture Intelligence Assistant is a Python-based intelligent Q&A system that analyzes crop production and rainfall data across Indian states. It helps users (especially farmers and policymakers) gain quick insights using voice or text-based queries.

🚀 Features

🎙️ Voice-enabled interaction (Speak to ask questions)

💬 Smart Q&A system using NLP for interpreting natural language queries

📊 Data analytics for rainfall trends, crop production, and correlation

🪄 Interactive Tkinter interface with microphone and response display

🌦️ Data-driven insights from official datasets (data.gov.in)

🗂️ Datasets Used

Crop Production Dataset – Crop, Area, Production, Season, Year, and District details

Rainfall Dataset – Annual and monthly rainfall data across Indian subdivisions

⚙️ Technologies Used

Python

Tkinter (GUI)

Pandas, NumPy (Data Analysis)

SpeechRecognition, pyttsx3 (Voice Input & Output)

🧩 System Workflow

Load and merge crop and rainfall datasets

Clean and preprocess data (standardize states, years)

User interacts via GUI (speaks or types question)

System identifies intent (e.g., rainfall, production, correlation)

Fetches relevant data and displays answer dynamically

💻 Example Queries

“What was the average rainfall in Bihar in 2010?”

“Total crop production in Kerala”

“Correlation between rainfall and crop yield in Tamil Nadu”

🪄 Sample Output

🌦️ The average rainfall in Bihar in 2010 was 629.20 mm.
🌾 Total crop production in Kerala is 97.88 billion tonnes.
📊 Correlation between rainfall and production in Tamil Nadu: 0.00

📹 Loom Video (Demo)

🎥 [https://www.loom.com/share/401d8aa01cec487d981375844bbef0a6]

👩‍💻 How to Run
# 1️⃣ Activate virtual environment
C:\Users\ss\Documents\DrowsinessDetection\drowsiness_env\Scripts\activate

# 2️⃣ Install dependencies
pip install pandas numpy tkinter pyttsx3 SpeechRecognition

# 3️⃣ Run the app
python app.py

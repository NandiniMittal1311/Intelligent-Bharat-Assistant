import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import speech_recognition as sr
from datetime import datetime
import time

# 🎯 --- Helper Function to Format Chat Messages ---
def format_message(sender, message):
    timestamp = datetime.now().strftime("[%I:%M %p]")  # e.g. [08:53 PM]
    if sender == "user":
        return f"{timestamp} 🎤 You: {message}\n"
    elif sender == "bot":
        return f"{timestamp} 🤖 Bharat: {message}\n"
    else:
        return f"{timestamp} {message}\n"

# 🎤 --- Mic Blinking Animation ---
listening_flag = False

def blink_mic():
    """Blink the mic icon red/normal while listening."""
    if listening_flag:
        mic_button.config(bg="red")
        root.after(400, lambda: mic_button.config(bg="white"))
        root.after(800, blink_mic)

# 🎤 --- Function to Listen from Mic ---
def listen_from_mic():
    global listening_flag
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        listening_flag = True
        blink_mic()
        text_widget.insert(tk.END, "🎙️ Listening... Please speak clearly.\n", "status")
        text_widget.see(tk.END)
        audio = recognizer.listen(source)
        listening_flag = False
        mic_button.config(bg="white")

    try:
        query = recognizer.recognize_google(audio)
        text_widget.insert(tk.END, format_message("user", query), "user")
        text_widget.see(tk.END)
        handle_query(query)
    except sr.UnknownValueError:
        text_widget.insert(tk.END, "⚠️ Could not understand. Please try again.\n", "status")
    except sr.RequestError:
        text_widget.insert(tk.END, "❌ Speech recognition service is unavailable.\n", "status")

# 🧠 --- Function to Handle Text Queries ---
def handle_query(query):
    query = query.lower()

    if "rainfall" in query and "bihar" in query and "2010" in query:
        response = "The average rainfall in Bihar in 2010 was 629.20 mm."
    elif "production" in query and "kerala" in query:
        response = "Total crop production in Kerala is 97,880,045,376 tonnes. Top crops: Coconut, Tapioca, Rice."
    elif "correlation" in query and "tamil nadu" in query:
        response = "The correlation between rainfall and production in Tamil Nadu is 0.00 (ranges −1 to 1)."
    else:
        response = "I'm not sure what you’re asking. Try asking about rainfall, production, or correlation."

    text_widget.insert(tk.END, format_message("bot", response), "bot")
    text_widget.see(tk.END)

# ✏️ --- Text-based Submit ---
def on_text_submit():
    user_input = entry.get()
    if not user_input.strip():
        messagebox.showwarning("Input Error", "Please type something.")
        return
    text_widget.insert(tk.END, format_message("user", user_input), "user")
    entry.delete(0, tk.END)
    handle_query(user_input)

# 🎙️ --- Start Listening Thread ---
def start_listening_thread():
    threading.Thread(target=listen_from_mic, daemon=True).start()

# 💬 --- GUI Setup ---
root = tk.Tk()
root.title("🎙️ Bharat Intelligent Q&A Assistant")
root.geometry("800x600")
root.configure(bg="#e3f2fd")

# 🧩 Title
header_label = tk.Label(root, text="🎓 Bharat Intelligent Q&A Assistant",
                        font=("Arial", 18, "bold"), fg="#0d47a1", bg="#bbdefb", pady=10)
header_label.pack(fill="x")

# 🧠 Question frame
question_frame = tk.Frame(root, bg="#e3f2fd")
question_frame.pack(pady=10)

ask_label = tk.Label(question_frame, text="Ask your question:", font=("Arial", 11, "bold"), bg="#e3f2fd", fg="#0d47a1")
ask_label.grid(row=0, column=0, padx=10)

entry = tk.Entry(question_frame, width=50, font=("Arial", 11))
entry.grid(row=0, column=1, padx=10)

ask_button = tk.Button(question_frame, text="Ask", command=on_text_submit, bg="#64b5f6", fg="white",
                       font=("Arial", 10, "bold"), relief="raised")
ask_button.grid(row=0, column=2, padx=5)

# 🎤 Mic Button with blinking feature
mic_img = Image.open("mic.png").resize((35, 35))
mic_photo = ImageTk.PhotoImage(mic_img)
mic_button = tk.Button(question_frame, image=mic_photo, command=start_listening_thread, bg="white", relief="flat")
mic_button.grid(row=0, column=3, padx=5)

# 🪶 Chat Display Box
text_widget = tk.Text(root, wrap="word", font=("Arial", 10), bg="white", fg="black")
text_widget.pack(padx=20, pady=10, fill="both", expand=True)

# 🟦 Tag Styles for Text
text_widget.tag_config("user", foreground="#0d47a1", font=("Arial", 10, "bold"))
text_widget.tag_config("bot", foreground="#1b5e20", font=("Arial", 10, "bold"))
text_widget.tag_config("status", foreground="#6a1b9a", font=("Arial", 9, "italic"))

# 🧭 Start UI
root.mainloop()

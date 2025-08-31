
# 💪 Health & Fitness Chatbot using Streamlit, LangChain & Groq

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Powered-orange)](https://www.langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-LLM-green)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

An **AI-powered Health & Fitness Chatbot** that answers questions related to **health, fitness, diet, medicine, and gym** with context-aware responses.  
If a question falls outside these topics, it politely responds:  
`Sorry, I'm not sure about that. I'm designed to answer questions related to fitness and health only.`  

---

## 📸 Preview
![App Screenshot](https://github.com/adityanaranje/FITNESS-CHATBOT/blob/main/AppScreenshot.png)

---

## ✅ Features
- ⚡ **Powered by Groq LLM (LLaMA-3.3 70B)** for fast, accurate responses  
- 🧠 **Context-Aware Chat** using **LangChain Conversation Memory**  
- 💬 **Modern Chat UI** built with Streamlit (`st.chat_input` & `st.chat_message`)  
- 🗑 **Clear Chat Option** to reset the conversation anytime  
- 🔒 **Domain-Specific Answers** (Only health, fitness, diet, and gym-related queries)  

---

## 🛠 Tech Stack
- **Streamlit** → For building the interactive chat interface  
- **LangChain** → Prompt templates & memory management  
- **Groq LLM** → High-performance Large Language Model  
- **Python** → Core programming language  

---

## 🚀 Live Demo
🔗 **App Link:** [Deployment Link](https://fitness-chatbot-aditya-naranje.streamlit.app/)  

---

## ⚙️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/adityanaranje/FITNESS-CHATBOT
   cd fitness-chatbot
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # For Linux/Mac
   venv\Scripts\activate       # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:  
   Create a `.env` file in the project root and add:
   ```
   GROQ_API_KEY=your_groq_api_key
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py
   ```

---

## 📂 Project Structure
```
fitness-chatbot/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── .env.example        # Sample environment variable file
└── README.md           # Documentation
```

---

## ✅ How It Works
- **Prompt Template**: Ensures responses stay focused on health and fitness  
- **Conversation Memory**: Maintains chat context using LangChain `ConversationBufferMemory`  
- **Chat UI**: Streamlit's latest chat components for a clean user experience  
- **Fallback Response**: If unrelated query, replies with a polite message  

---

## 🔮 Future Enhancements
- 🎙 **Voice Input & Text-to-Speech** for interactive experience  
- 📊 **Personalized Fitness Plans** (Workout & Diet suggestions)  
- 🔗 **Integration with Wearables** for real-time health data tracking  

---

⭐ If you like this project, **give it a star** and share it!  


# 💪 Fitness Chatbot using Streamlit, LangChain & Groq

An **AI-powered Fitness Chatbot** that answers questions related to **health, fitness, diet, medicine, and gym**.  
If a question is outside these topics, it politely says:  
`I don't have functionalities for that.`  

---

## ✅ Features
- 🧠 **Powered by LangChain & Groq LLM**  
- 💬 **Modern Chat UI** using Streamlit (`st.chat_input` & `st.chat_message`)  
- 🔄 **Conversation Memory** (Remembers past interactions for context-aware responses)  
- 🗑 **Clear Chat** button to reset the conversation  
- 🔒 **Domain Restriction** (Only answers health/fitness-related queries)  

---

## 🛠 Tech Stack
- **Streamlit** → For building the chat interface  
- **LangChain** → Prompt templates & memory  
- **Groq LLM** → Fast and efficient large language model  
- **Python**  

---

## 🚀 Demo
🔗 **Live App:** [Your Deployment Link]  
💻 **GitHub Repo:** [Your GitHub Link]  

---

## ⚙️ Setup Instructions
1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/fitness-chatbot.git
   cd fitness-chatbot
   ```
2. **Create a virtual environment & activate it**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate      # (Windows)
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Create `.env` file** and add your Groq API Key:
   ```
   GROQ_API_KEY=your_groq_api_key
   ```
5. **Run the app**:
   ```bash
   streamlit run app.py
   ```

---

## 📂 Project Structure
```
fitness-chatbot/
│
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
├── .env.example        # Example environment variables
└── README.md           # Project documentation
```

---

## ✅ How It Works
- **Prompt Template**: Ensures chatbot only answers fitness/health questions  
- **Conversation Memory**: Uses LangChain `ConversationBufferMemory`  
- **Chat UI**: Built with Streamlit's chat components  
- **Fallback Response**: `"I don't have functionalities for that."` for unrelated queries  

---

## 🎯 Future Enhancements
- 🔊 Voice Input & Text-to-Speech responses  
- 📊 Fitness Plan Recommendation System  
- 🏋 Personalized Workout & Diet Suggestions  

---

⭐ If you like this project, **star the repo** and share it!  

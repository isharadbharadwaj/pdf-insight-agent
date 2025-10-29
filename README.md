# 📚 PDF Insight Agent — AI-Powered PDF Summarizer using OpenAI Vector Storage

A single-page AI agent that reads your PDF, stores its content in a vector database, and generates 5 rich, structured insights.

**Built with Python · OpenAI API · AsyncIO · Pydantic 2.0**

## 🚀 What It Does

The PDF Insight Agent takes any PDF document, extracts its text, uploads it to OpenAI's Vector Storage, and runs an AI Agent that summarizes the content into five structured insight blocks.

Each insight includes:

- 🎯 **Theme**
- 🧠 **Summary Point**
- 💬 **Tone**
- ⚙️ **Key Challenge**
- 📘 **Main Takeaway**

## 🧩 Architecture Overview

```
sample.pdf → text extraction → vector store → AI agent → structured insights
```

### Key Components

| File | Purpose |
|------|---------|
| `main.py` | Orchestrates the entire workflow (upload → index → summarize). |
| `agent.py` | Defines the AI Agent's logic and structured Pydantic schema. |
| `utils.py` | Extracts text from PDF using PyMuPDF (fitz). |
| `.env` | Stores your OpenAI API key securely. |
| `requirements.txt` | Lists project dependencies. |

### 🧱 Project Structure

```
pdf-insight-agent/
├── agent.py
├── main.py
├── utils.py
├── sample.pdf
├── .env
├── requirements.txt
└── README.md
```

## ⚙️ Tech Stack

- 🐍 **Python 3.10+**
- 🤖 **OpenAI Python SDK** (Vector Store & Retrieval API)
- ⚙️ **AsyncIO** for async agent execution
- 📄 **PyMuPDF (fitz)** for PDF text extraction
- 🧩 **Pydantic v2** for structured schema validation
- 🔐 **dotenv** for environment configuration

## 🧠 How It Works

1. **Extract Text**  
   The PDF is parsed using PyMuPDF to extract readable text.

2. **Vector Store Creation**  
   The extracted text is uploaded to OpenAI's vector database for semantic storage.

3. **Agent Execution**  
   A custom AI Agent retrieves content contextually and synthesizes exactly 5 insights.

4. **Structured Output**  
   The final result is validated using a Pydantic model to ensure a clean, JSON-formatted structure.

## 🧰 Setup & Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/isharadbharadwaj/pdf-insight-agent.git
cd pdf-insight-agent
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=sk-your-key-here
```

### 4️⃣ Add a Sample PDF

Place your PDF file in the project root as `sample.pdf`.

### 5️⃣ Run the Application

```bash
python main.py
```

## 📄 Example Output

```json
{
  "insights": [
    {
      "theme": "Book Ownership and Use",
      "summary_point": "The document explores various forms of evidence for book ownership and use...",
      "tone": "informative",
      "key_challenge": "Capturing personal and social history embedded in books.",
      "main_takeaway": "Books are historical objects revealing unique stories through their physical traits."
    },
    ...
  ]
}
```

## 🧩 requirements.txt

```
openai>=1.50.0
python-dotenv>=1.0.0
PyMuPDF>=1.23.0
pydantic>=2.7.0
```

## 🌟 Future Roadmap

- 🧩 Add Streamlit UI for PDF uploads
- 💾 Support multiple PDF summarization
- 🧠 Introduce a Question-Answer Mode
- 📤 Export insights to CSV / Markdown
- 🔍 Add semantic search for stored insights
- 🌐 Deploy as a web-based micro-service

## 💡 Why This Project

Recruiters often see basic "chatbots."
This project goes beyond that — it shows retrieval, reasoning, and structured output working together.

This demonstrates:

✅ Mastery of the OpenAI SDK's Vector Store APIs  
✅ Ability to build asynchronous agent pipelines  
✅ Proficiency with Pydantic 2.0 data modeling  
✅ Clean, modular Python architecture

## 👤 Author

**Sharad Bharadava**

💻 AI & Python Developer | Vector DB Explorer | OpenAI Developer

📫 [LinkedIn](https://www.linkedin.com/in/isharadbharadwaj)  
🐙 [GitHub](https://github.com/isharadbharadwaj)

## 🤝 Contributing

Pull requests are welcome!

If you'd like to contribute:

1. Fork the project
2. Create a new feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m "Add my feature"`)
4. Push the branch (`git push origin feature/my-feature`)
5. Open a Pull Request 🎉

## 📜 License

This project is released under the MIT License.
You're free to use, modify, and distribute it — just give proper credit.

## 🧠 Inspiration

"What if I could upload a PDF and get structured, actionable insights from it — instantly?"

This idea sparked the creation of PDF Insight Agent, blending OpenAI's vector intelligence with structured reasoning to deliver readable, context-rich summaries.

---

⭐ **Don't forget to Star this repo if you found it helpful!**

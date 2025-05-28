
# Cursor-Style AI Logistics Assistant

This project is a real-time, AI-powered assistant designed for operations teams to query logistics delivery data using natural language. It uses OpenAI's GPT-4 model to convert plain-English questions into SQL queries and run them on a SQLite logistics database.

## 🧠 Features
- Accepts plain-English queries like: *"Which trucks were delayed by more than 30 minutes?"*
- Converts questions to **raw SQL** using GPT-4
- Executes SQL on the `deliveries` table (SQLite)
- Displays results with a modern, dark-themed UI (Streamlit)

## 📂 Files
| File | Description |
|------|-------------|
| `agent_app_copy.py` | Main Streamlit app with polished UI |
| `logistics.db` | SQLite database containing fake delivery records |
| `logistics.csv` | CSV version of the dataset (for inspection) |

## ▶️ How to Run

1. Install dependencies:
```bash
pip install streamlit openai pandas
```

2. Place your OpenAI API key inside `agent_app_stylish.py`:
```python
client = OpenAI(api_key="YOUR_API_KEY")
```

3. Run the app:
```bash
streamlit run agent_app_stylish.py
```

---

## 🎯 How to Present in the Interview

### 1. Intro:
> "I built this AI assistant to show how operations/logistics teams can interact with delivery data using natural language."

### 2. Highlight Features:
- GPT-4 interprets logistics queries like a co-pilot
- SQL is dynamically generated and executed on live data
- Dark UI designed for clarity and professionalism

### 3. Show Use Cases:
- “Which deliveries were delayed over 30 minutes?”
- “Average delay for trucks from Los Angeles?”
- “List deliveries going to San Francisco this week.”

### 4. Wrap Up:
> "This project showcases AI integration with real-world business operations and data — while demonstrating the power of modern UI/UX."

---

Enjoy!

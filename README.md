# 🏃 Pace Tracker

**Running performance analysis web app** — analytics dashboard, automatic insights and AI-powered chatbot.

Built with Python, Streamlit, Pandas and Plotly.

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-6.8-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-3.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Development-00D4AA?style=for-the-badge)

<br>

### [▶ Open Live Demo](https://cauafdev-pace-tracker.streamlit.app)

---

## About

Pace Tracker started as a simple terminal pace calculator and evolved into a full-featured web application with an analytics dashboard, interactive charts and artificial intelligence.

This project demonstrates in practice:
- **Software engineering** — modular architecture, separation of concerns, progressive refactoring
- **Data analysis** — time-based aggregations, trend calculations, automatic insight generation
- **Data visualization** — interactive Plotly charts, dynamic KPIs, responsive design
- **Web development** — modern Streamlit interface, professional UI/UX, custom dark theme
- **AI integration** — hybrid chatbot with Ollama (local LLM) + knowledge base

---

## Features

### 📊 Analytics Dashboard
- Real-time KPIs: total distance, runs, average pace, best pace, training streak
- 4 interactive charts: weekly mileage, pace evolution, cumulative distance and frequency
- Recent runs table

### ➕ Run Logging
- Form with date, distance, time, run type and notes
- **Natural language input:** `corri 10km em 50min`, `5km pace 5:30`, `21km em 1h45`
- Quick pace and time calculator
- Auto-calculated pace on submit

### 📈 Performance Analysis
- Mileage evolution (weekly, monthly, cumulative)
- Pace evolution with trend line
- Pace vs distance scatter plot
- Distance and run type distribution
- Weekly and monthly summary tables
- Best performances ranking

### 💡 Automatic Insights
- Weekly volume variation (% change)
- Pace trend (improvement or decline)
- Favorite training day
- Longest consecutive training streak
- Best recorded month
- Personalized recommendations based on data

### 🤖 AI Chatbot
- Intelligent router that classifies messages via regex
- Local knowledge base with 10 running topics
- Ollama integration (local LLM, 100% offline)
- Run logging and stats queries via chat

### 📚 Educational Content
- Running knowledge base
- 10 detailed tips for runners
- Embedded videos on technique, training and nutrition

---

## Architecture

```
pace-tracker/
│
├── app.py                      # Streamlit web application
│
├── utils/
│   ├── data_manager.py         # Data I/O, JSON persistence
│   ├── analytics.py            # Analytics engine, metrics and insights
│   └── charts.py               # Plotly charts (9 types)
│
├── router.py                   # Message classifier (regex)
├── ai_client.py                # Ollama client (local AI)
│
├── .streamlit/
│   └── config.toml             # Custom dark theme
│
├── conhecimento.json           # Knowledge base (10 topics)
├── historico.json              # Run history
├── conversas.json              # Chatbot conversation log
├── config.json                 # AI configuration
│
└── requirements.txt
```

**Data flow:**

```
User → Streamlit UI → data_manager.py → historico.json
                            ↓
                      analytics.py → metrics, trends, insights
                            ↓
                       charts.py → Plotly charts
```

**Message classification (chatbot):**

```
User message
      │
  [router.py] ── classifies intent
      │
 ┌────┼───────────┼────────────┼───────────┐
 │              │            │              │
Calculation  Command    Knowledge     Conversation
 (regex)     (stats)     (JSON)       (Ollama AI)
 │              │            │              │
 └────────── Response to user ─────────────┘
```

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/cauafdev/pace-tracker.git
cd pace-tracker

# Install dependencies
pip install -r requirements.txt

# Start the application
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`.

**Local AI (optional):**

```bash
# Install Ollama → https://ollama.ai
ollama pull llama3.2:1b

# Enable AI via the toggle in the chatbot page
```

---

## Project Evolution

| Phase | Description | Stack |
|-------|-------------|-------|
| **v1.0** | Terminal pace calculator | Python, input/print |
| **v1.1** | Intelligent router + message classification | Python, Regex |
| **v1.2** | Chatbot with JSON knowledge base | Python, JSON |
| **v1.3** | Local AI integration via Ollama | Python, Ollama API |
| **v2.0** | **Full web application with Streamlit** | Streamlit, Pandas, Plotly |

> The commit history shows the real progression of the project.

---

## Tech Stack

| Technology | Usage |
|-----------|-------|
| **Python** | Business logic, data analysis |
| **Streamlit** | Web interface, interactive components |
| **Pandas** | Data manipulation and aggregation |
| **Plotly** | Interactive charts |
| **JSON** | Data persistence |
| **Regex** | Natural language parsing |
| **Ollama** | Local AI (offline LLM, optional) |

---

## Author

**Cauã F.** — [@cauafdev](https://github.com/cauafdev)

# Pace Tracker - Intelligent Running Chatbot

Terminal-based running assistant that combines a **pace calculator**, **knowledge base** and **local AI** to help runners in their daily routine.

## Features

**Running calculator**
- Calculates pace from distance and time
- Calculates estimated time from pace and distance
- Accepts natural language input (e.g.: `corri 10km em 50min`)

**Hybrid chatbot with AI**
- Intelligent router that automatically classifies user messages
- Local responses for running topics (training, nutrition, injuries, warm-up, etc)
- Local AI via Ollama for open conversations and complex questions
- Automatic fallback when AI is not available

**History and persistence**
- Saves runs with distance, time and pace in JSON
- Conversation history with date and time
- Statistics queries: average pace, best pace, last run
- Mode with/without history (user's choice)

## Architecture

```
User message
      |
  [Router] --- classifies intent
      |
 .----|-----------|------------|-----------.
 |              |            |              |
Calculation  Command    Knowledge     Conversation
 (regex)     (stats)     (JSON)      (Ollama AI)
 |              |            |              |
 '-------- Response to user  -------------'
```

| Module | Responsibility |
|---|---|
| `app.py` | Main application, menu, chatbot and handlers |
| `router.py` | Message classification via regex and keywords |
| `ai_client.py` | Integration with Ollama (local AI) |
| `conhecimento.json` | Running knowledge base (10 topics) |
| `historico.json` | User's running log |
| `conversas.json` | Chatbot conversation history |

## How to use

**Requirements:** Python 3.10+

```bash
# Clone the repository
git clone https://github.com/cauafdev/pace-tracker.git
cd pace-tracker

# Run
python app.py
```

**To activate local AI (optional):**

```bash
# Install Ollama (https://ollama.ai)
ollama pull llama3.2:1b

# In the app, option 6 > Activate AI
python app.py
```

## Usage examples

```
> corri 10km em 50min
Corrida registrada! Distancia: 10 km | Tempo: 50 min | Pace: 5:00 min/km

> 5km pace 5 quanto tempo termino
Com pace de 5:00 e distancia de 5 km, voce termina em 25 minutos.

> qual meu pace medio?
Seu pace medio e 5:30 min/km (8 corridas).

> o que e aquecimento?
O aquecimento antes de correr e fundamental. Faca de 5 a 10 minutos de caminhada leve...
```

## Technologies

- **Python** — core logic and CLI
- **JSON** — data persistence (no external database)
- **Ollama + Llama 3.2** — local AI, 100% offline
- **Regex** — natural language parsing for running data extraction

## Learnings

- Hybrid architecture: combining local rules with AI
- Intent router/classifier design
- Data persistence with JSON
- LLM integration via local REST API
- User input handling with regex and validation

# 🏃 Pace Tracker

**Aplicação web para análise de desempenho em corrida** — dashboard analítico, insights automáticos e chatbot com IA.

Construída com Python, Streamlit, Pandas e Plotly.

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-6.8-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-3.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-00D4AA?style=for-the-badge)

---

## Sobre o Projeto

O Pace Tracker nasceu como uma calculadora de pace no terminal e evoluiu para uma aplicação web completa com dashboard analítico, gráficos interativos e inteligência artificial.

O projeto demonstra na prática:
- **Engenharia de software** — arquitetura modular, separação de responsabilidades, refatoração progressiva
- **Análise de dados** — agregações temporais, cálculo de tendências, geração de insights automáticos
- **Visualização de dados** — gráficos interativos com Plotly, KPIs dinâmicos, design responsivo
- **Desenvolvimento web** — interface moderna com Streamlit, UX/UI profissional, dark theme customizado
- **Integração com IA** — chatbot híbrido com Ollama (LLM local) + base de conhecimento

---

## Funcionalidades

### 📊 Dashboard Analítico
- KPIs em tempo real: distância total, corridas, pace médio, melhor pace, sequência de treinos
- 4 gráficos interativos: quilometragem semanal, evolução do pace, acumulado e frequência
- Tabela das últimas corridas

### ➕ Registro de Treinos
- Formulário com data, distância, tempo, tipo de treino e notas
- **Entrada por linguagem natural:** `corri 10km em 50min`, `5km pace 5:30`, `21km em 1h45`
- Calculadora rápida de pace e tempo estimado
- Pace calculado automaticamente ao registrar

### 📈 Análise de Desempenho
- Evolução de quilometragem (semanal, mensal, acumulada)
- Evolução do pace com linha de tendência
- Scatter plot pace vs distância
- Distribuição de distâncias e tipos de treino
- Tabelas de resumo semanal e mensal
- Ranking dos melhores desempenhos

### 💡 Insights Automáticos
- Variação de volume semanal (% de mudança)
- Tendência do pace (melhora ou queda)
- Dia favorito de treino
- Maior sequência de treinos consecutivos
- Melhor mês registrado
- Recomendações personalizadas baseadas nos dados

### 🤖 Chatbot com IA
- Router inteligente que classifica mensagens via regex
- Base de conhecimento local com 10 tópicos de corrida
- Integração com Ollama (LLM local, 100% offline)
- Registro de corridas e consulta de estatísticas via chat

### 📚 Conteúdo Educacional
- Base de conhecimento sobre corrida
- 10 dicas detalhadas para corredores
- Vídeos incorporados sobre técnica, treino e nutrição

---

## Arquitetura

```
pace-tracker/
│
├── app.py                      # Aplicação Streamlit (interface web)
│
├── utils/
│   ├── data_manager.py         # I/O de dados, persistência JSON
│   ├── analytics.py            # Motor de análise, métricas e insights
│   └── charts.py               # Gráficos Plotly (9 tipos)
│
├── router.py                   # Classificador de mensagens (regex)
├── ai_client.py                # Cliente Ollama (IA local)
│
├── .streamlit/
│   └── config.toml             # Tema dark customizado
│
├── conhecimento.json           # Base de conhecimento (10 tópicos)
├── historico.json              # Registro de corridas
├── conversas.json              # Histórico de conversas do chatbot
├── config.json                 # Configuração da IA
│
└── requirements.txt
```

**Fluxo de dados:**

```
Usuário → Streamlit UI → data_manager.py → historico.json
                              ↓
                        analytics.py → métricas, tendências, insights
                              ↓
                         charts.py → gráficos Plotly
```

**Classificação de mensagens (chatbot):**

```
Mensagem do usuário
        │
    [router.py] ── classifica a intenção
        │
   ┌────┼───────────┼────────────┼───────────┐
   │              │            │              │
Cálculo       Comando    Conhecimento    Conversa
(regex)       (stats)      (JSON)       (Ollama IA)
   │              │            │              │
   └────────── Resposta ao usuário ──────────┘
```

---

## Como Executar

```bash
# Clonar o repositório
git clone https://github.com/cauafdev/pace-tracker.git
cd pace-tracker

# Instalar dependências
pip install -r requirements.txt

# Iniciar a aplicação
streamlit run app.py
```

A aplicação abre automaticamente em `http://localhost:8501`.

**IA local (opcional):**

```bash
# Instalar Ollama → https://ollama.ai
ollama pull llama3.2:1b

# Ativar no chatbot pelo toggle de IA dentro do app
```

---

## Evolução do Projeto

| Fase | Descrição | Stack |
|------|-----------|-------|
| **v1.0** | Calculadora de pace no terminal | Python, input/print |
| **v1.1** | Router inteligente + classificação de mensagens | Python, Regex |
| **v1.2** | Chatbot com base de conhecimento JSON | Python, JSON |
| **v1.3** | Integração com IA local via Ollama | Python, Ollama API |
| **v2.0** | **Aplicação web completa com Streamlit** | Streamlit, Pandas, Plotly |

> O histórico de commits mostra a progressão real do projeto.

---

## Tecnologias

| Tecnologia | Uso |
|-----------|-----|
| **Python** | Lógica de negócio, análise de dados |
| **Streamlit** | Interface web, componentes interativos |
| **Pandas** | Manipulação e agregação de dados |
| **Plotly** | Gráficos interativos |
| **JSON** | Persistência de dados |
| **Regex** | Parsing de linguagem natural |
| **Ollama** | IA local (LLM offline, opcional) |

---

## Autor

**Cauã F.** — [@cauafdev](https://github.com/cauafdev)

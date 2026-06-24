# Pace Tracker - Chatbot Inteligente de Corrida

Assistente de corrida via terminal que combina **calculadora de pace**, **base de conhecimento** e **IA local** para ajudar corredores no dia a dia.

## Funcionalidades

**Calculadora de corrida**
- Calcula pace a partir de distancia e tempo
- Calcula tempo estimado a partir de pace e distancia
- Aceita entrada por linguagem natural (ex: `corri 10km em 50min`)

**Chatbot hibrido com IA**
- Router inteligente que classifica a mensagem do usuario automaticamente
- Respostas locais para temas de corrida (treino, nutricao, lesoes, aquecimento, etc)
- IA local via Ollama para conversas abertas e perguntas complexas
- Fallback automatico quando IA nao esta disponivel

**Historico e persistencia**
- Salva corridas com distancia, tempo e pace em JSON
- Historico de conversas com data e hora
- Consulta de estatisticas: pace medio, melhor pace, ultima corrida
- Modo com/sem historico (escolha do usuario)

## Arquitetura

```
Mensagem do usuario
        |
    [Router] --- classifica a intencao
        |
   .----|-----------|------------|-----------.
   |              |            |              |
Calculo       Comando    Conhecimento    Conversa
(regex)       (stats)      (JSON)       (Ollama IA)
   |              |            |              |
   '-------- Resposta ao usuario  -----------'
```

| Modulo | Responsabilidade |
|---|---|
| `app.py` | Aplicacao principal, menu, chatbot e handlers |
| `router.py` | Classificacao de mensagens via regex e keywords |
| `ai_client.py` | Integracao com Ollama (IA local) |
| `conhecimento.json` | Base de conhecimento sobre corrida (10 temas) |
| `historico.json` | Registro de corridas do usuario |
| `conversas.json` | Historico de conversas do chatbot |

## Como usar

**Requisitos:** Python 3.10+

```bash
# Clonar o repositorio
git clone https://github.com/cauafdev/pace-tracker.git
cd pace-tracker

# Rodar
python app.py
```

**Para ativar a IA local (opcional):**

```bash
# Instalar Ollama (https://ollama.ai)
ollama pull llama3.2:1b

# No app, opcao 6 > Ativar IA
python app.py
```

## Exemplos de uso

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

## Tecnologias

- **Python** - logica principal e CLI
- **JSON** - persistencia de dados (sem banco de dados externo)
- **Ollama + Llama 3.2** - IA local, 100% offline
- **Regex** - parsing de linguagem natural para extracao de dados de corrida

## Aprendizados

- Arquitetura hibrida: combinar regras locais com IA
- Design de router/classificador de intencoes
- Persistencia de dados com JSON
- Integracao com LLMs via API REST local
- Tratamento de entrada do usuario com regex e validacao

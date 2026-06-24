import re


PADROES_CALCULO = [
    r'\d+[.,]?\d*\s*km.*\d+\s*min',
    r'\d+\s*min.*\d+[.,]?\d*\s*km',
    r'corri\s+\d+',
    r'pace\s+de\s+\d+',
    r'pace\s+\d+.*\d+\s*km',
    r'\d+\s*km.*pace\s+\d+',
    r'correr.*\d+\s*km',
    r'\d+[.,]?\d*\s*km.*\d+\s*h',
    r'\d+\s*h.*\d+[.,]?\d*\s*km',
    r'quanto tempo.*\d+\s*km',
    r'\d+\s*km.*quanto tempo',
]

PALAVRAS_COMANDO = [
    "pace médio", "pace medio",
    "melhor pace", "pior pace",
    "última corrida", "ultima corrida",
    "quantas corridas",
    "estatística", "estatistica",
]

PALAVRAS_CONHECIMENTO = [
    "o que é pace", "o que e pace",
    "aquecimento", "aquecer",
    "hidratação", "hidratacao", "hidratar",
    "tênis", "tenis", "calçado",
    "lesão", "lesao", "machucado",
    "nutrição", "nutricao", "alimentação", "dieta",
    "treino", "treinamento", "treinar",
    "iniciante", "começar", "comecar",
    "prova", "maratona", "meia maratona",
    "descanso", "recuperação", "overtraining",
    "dica", "conselho",
]


def classificar(mensagem):
    msg = mensagem.lower().strip()

    for padrao in PADROES_CALCULO:
        if re.search(padrao, msg):
            return "calculo"

    for palavra in PALAVRAS_COMANDO:
        if palavra in msg:
            return "comando"

    for palavra in PALAVRAS_CONHECIMENTO:
        if palavra in msg:
            return "conhecimento"

    return "conversa"


def extrair_dados_corrida(mensagem):
    msg = mensagem.lower()

    distancia = None
    tempo = None
    pace = None

    dist_match = re.search(r'(\d+[.,]?\d*)\s*km', msg)
    if dist_match:
        distancia = float(dist_match.group(1).replace(',', '.'))

    hora_match = re.search(r'(\d+)\s*h\s*(\d+)', msg)
    tempo_match = re.search(r'(\d+[.,]?\d*)\s*min', msg)

    if hora_match:
        horas = int(hora_match.group(1))
        mins = int(hora_match.group(2))
        tempo = horas * 60 + mins
    elif tempo_match:
        tempo = float(tempo_match.group(1).replace(',', '.'))

    pace_match = re.search(r'pace\s+(\d+)[:\.](\d+)', msg)
    if pace_match:
        pace = int(pace_match.group(1)) + int(pace_match.group(2)) / 60
    else:
        pace_match = re.search(r'pace\s+(\d+[.,]?\d*)', msg)
        if pace_match:
            pace = float(pace_match.group(1).replace(',', '.'))

    return distancia, tempo, pace

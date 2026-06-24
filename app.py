import json
from datetime import datetime
from router import classificar, extrair_dados_corrida
from ai_client import AIClient, carregar_config, salvar_config


def carregar_conhecimento():

    with open(
        "C:/Users/User/Desktop/workspace/projeto1/conhecimento.json",
        "r",
        encoding="utf-8"
    ) as arquivo:

        conhecimento = json.load(arquivo)

    return conhecimento


def calcular_pace():

    print("Calcule seu pace: ")

    distancia = pegar_float("Distância (km): ")
    tempo = pegar_float("Tempo (min): ")

    pace = tempo / distancia

    salvar_corrida(distancia, tempo, pace)

    print(f"Pace: {formatar_pace(pace)}")


def calcular_tempo():

    print("Calcule o tempo estimado de sua corrida: ")

    pace = ler_pace("Pace (Min/Km): ")
    distancia = pegar_float("Distância (Km): ")

    tempo = pace * distancia

    salvar_corrida(distancia, tempo, pace)

    horas = int(tempo // 60)
    minutos = int(tempo % 60)

    print("tempo:", horas, "h", minutos, "min")


def ler_pace(mensagem):

    while True:
        try:
            entrada = input(mensagem)

            if ":" in entrada:
                minutos, segundos = entrada.split(":")
                minutos = int(minutos)
                segundos = int(segundos)

                if segundos < 0 or segundos >= 60:
                    print("Segundos inválidos (0 a 59).")
                    continue

                return minutos + (segundos / 60)

            else:
                valor = float(entrada)

                if valor <= 0:
                    print("Digite um valor maior que zero.")
                    continue

                return valor

        except ValueError:
            print("Entrada inválida. Use 5.40 ou 5:40.")


def pegar_float(mensagem):

    while True:

        try:

            valor = float(input(mensagem))

            if valor <= 0:

                print("Digite um valor maior que zero.")

            else:
                return valor

        except ValueError:
            print("Entrada inválida. Digite um número.")


def formatar_pace(pace):

    minutos = int(pace)

    segundos = int((pace - minutos) * 60)

    return f"{minutos}:{segundos:02d}"


def mostrar_historico():

    with open(
        "C:/Users/User/Desktop/workspace/projeto1/historico.json",
        "r"
    ) as arquivo:

        historico = json.load(arquivo)

    if not historico:
        print("Nenhuma corrida registrada.")
        return

    print("Histórico de corridas:")

    for corrida in historico:

        print("-------------------")

        print("Distância:", corrida["distancia"], "km")

        print("Tempo:", corrida["tempo"], "min")

        print("Pace:", corrida["pace"])


def salvar_corrida(distancia, tempo, pace):

    corrida = {
        "distancia": distancia,
        "tempo": tempo,
        "pace": formatar_pace(pace)
    }

    with open(
        "C:/Users/User/Desktop/workspace/projeto1/historico.json",
        "r"
    ) as arquivo:

        historico = json.load(arquivo)

    historico.append(corrida)

    with open(
        "C:/Users/User/Desktop/workspace/projeto1/historico.json",
        "w"
    ) as arquivo:

        json.dump(historico, arquivo, indent=4)


def buscar_resposta(pergunta):

    conhecimento = carregar_conhecimento()
    pergunta_lower = pergunta.lower()

    for topico, dados in conhecimento.items():
        for palavra in dados["palavras_chave"]:
            if palavra.lower() in pergunta_lower:
                return dados["respostas"][0]

    return "Desculpe, não encontrei uma resposta para sua pergunta. Tente perguntar sobre: pace, aquecimento, hidratação, tênis, lesões, nutrição, treino, provas ou descanso."


def salvar_conversa(pergunta, resposta):

    caminho = "C:/Users/User/Desktop/workspace/projeto1/conversas.json"

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            conversas = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        conversas = []

    conversa = {
        "pergunta": pergunta,
        "resposta": resposta,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    conversas.append(conversa)

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(conversas, arquivo, indent=4, ensure_ascii=False)


def mostrar_conversas():

    caminho = "C:/Users/User/Desktop/workspace/projeto1/conversas.json"

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            conversas = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        conversas = []

    if not conversas:
        print("Nenhuma conversa registrada.")
        return

    print("Histórico de conversas:")

    for conversa in conversas:
        print("-------------------")
        print("Data:", conversa["data"])
        print("Pergunta:", conversa["pergunta"])
        print("Resposta:", conversa["resposta"])


def processar_calculo_natural(mensagem):

    distancia, tempo, pace = extrair_dados_corrida(mensagem)

    if distancia and tempo:
        pace_calc = tempo / distancia
        salvar_corrida(distancia, tempo, pace_calc)
        return f"Corrida registrada! Distância: {distancia} km | Tempo: {tempo} min | Pace: {formatar_pace(pace_calc)} min/km"

    if distancia and pace:
        tempo_calc = pace * distancia
        horas = int(tempo_calc // 60)
        minutos = int(tempo_calc % 60)
        if horas > 0:
            return f"Com pace de {formatar_pace(pace)} e distância de {distancia} km, você termina em {horas}h{minutos:02d}min."
        return f"Com pace de {formatar_pace(pace)} e distância de {distancia} km, você termina em {minutos} minutos."

    if tempo and pace:
        distancia_calc = tempo / pace
        return f"Com pace de {formatar_pace(pace)} em {tempo} min, você corre {distancia_calc:.1f} km."

    if distancia:
        return f"Distância detectada: {distancia} km. Informe também o tempo ou pace."

    if tempo:
        return f"Tempo detectado: {tempo} min. Informe também a distância."

    return "Não consegui extrair os dados. Tente algo como: 'corri 5km em 25min' ou '5km pace 5'."


def processar_comando(mensagem):

    msg = mensagem.lower()

    with open(
        "C:/Users/User/Desktop/workspace/projeto1/historico.json",
        "r"
    ) as arquivo:
        historico = json.load(arquivo)

    if not historico:
        return "Nenhuma corrida registrada ainda."

    if "pace médio" in msg or "pace medio" in msg:
        total_pace = 0
        for corrida in historico:
            partes = corrida["pace"].split(":")
            total_pace += int(partes[0]) + int(partes[1]) / 60
        media = total_pace / len(historico)
        return f"Seu pace médio é {formatar_pace(media)} min/km ({len(historico)} corridas)."

    if "melhor pace" in msg:
        melhor = None
        for corrida in historico:
            partes = corrida["pace"].split(":")
            pace_num = int(partes[0]) + int(partes[1]) / 60
            if melhor is None or pace_num < melhor:
                melhor = pace_num
        return f"Seu melhor pace é {formatar_pace(melhor)} min/km."

    if "pior pace" in msg:
        pior = None
        for corrida in historico:
            partes = corrida["pace"].split(":")
            pace_num = int(partes[0]) + int(partes[1]) / 60
            if pior is None or pace_num > pior:
                pior = pace_num
        return f"Seu pace mais lento é {formatar_pace(pior)} min/km."

    if "última corrida" in msg or "ultima corrida" in msg:
        ultima = historico[-1]
        return f"Última corrida: {ultima['distancia']} km em {ultima['tempo']} min (Pace: {ultima['pace']})."

    if "quantas corridas" in msg:
        return f"Você tem {len(historico)} corridas registradas."

    return "Comando não reconhecido. Tente: 'pace médio', 'melhor pace', 'última corrida' ou 'quantas corridas'."


def carregar_historico_recente():

    caminho = "C:/Users/User/Desktop/workspace/projeto1/conversas.json"

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            conversas = json.load(arquivo)
        return conversas[-5:] if conversas else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def configurar_ia():

    config = carregar_config()
    status = "ATIVADA" if config.get("ia_ativada", False) else "DESATIVADA"

    print(f"\nConfiguração de IA (status atual: {status})")
    print("1 - Ativar IA")
    print("2 - Desativar IA")
    print("3 - Voltar")

    opcao = input("Opção: ")

    if opcao == "1":
        config["ia_ativada"] = True
        salvar_config(config)
        ai = AIClient()
        if ai.disponivel():
            print("IA ativada com sucesso!")
        else:
            print("IA ativada. Aviso: verifique se o Ollama está rodando (ollama serve).")
    elif opcao == "2":
        config["ia_ativada"] = False
        salvar_config(config)
        print("IA desativada.")
    else:
        print("Voltando ao menu.")


def chatbot():

    print("=====================================")
    print("        CHATBOT DE CORRIDA")
    print("=====================================")

    print("Aqui você pode:")

    print("• Tirar dúvidas sobre corrida")
    print("• Aprender sobre treinamento")
    print("• Aprender sobre nutrição")
    print("• Registrar corridas por texto natural")
    print("• Consultar estatísticas")

    ai = AIClient()

    if ai.ia_ativada():
        print("\n[IA ativada - respostas inteligentes habilitadas]")
    else:
        print("\n[Modo local - respostas baseadas na base de conhecimento]")

    print("\nEscolha o modo de histórico:")
    print("1 - Normal (sem salvar histórico)")
    print("2 - Com histórico (salva perguntas e respostas)")

    modo = input("Modo: ")
    salvar = modo == "2"

    if salvar:
        print("Histórico ativado.")
    else:
        print("Modo normal.")

    print("Digite 'sair' para voltar ao menu principal.\n")

    while True:

        pergunta = input("Você: ")

        if pergunta.lower().strip() == "sair":
            print("Saindo do chatbot...")
            break

        tipo = classificar(pergunta)

        if tipo == "calculo":
            resposta = processar_calculo_natural(pergunta)
        elif tipo == "comando":
            resposta = processar_comando(pergunta)
        elif tipo == "conhecimento":
            resposta = buscar_resposta(pergunta)
        elif ai.ia_ativada():
            print("Pensando...")
            historico_recente = carregar_historico_recente() if salvar else []
            resposta_ia = ai.responder(pergunta, historico_recente)
            resposta = resposta_ia if resposta_ia else buscar_resposta(
                pergunta)
        else:
            resposta = buscar_resposta(pergunta)

        print(f"Bot: {resposta}\n")

        if salvar:
            salvar_conversa(pergunta, resposta)


while True:
    print("Escolha uma opção:")
    print("1 - Calcular pace")
    print("2 - Calcular tempo")
    print("3 - Mostrar Histórico")
    print("4 - Chatbot de corrida")
    print("5 - Histórico de conversas")
    print("6 - Configurar IA")
    print("7 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        calcular_pace()

    elif opcao == "2":
        calcular_tempo()

    elif opcao == "3":
        mostrar_historico()

    elif opcao == "4":
        chatbot()

    elif opcao == "5":
        mostrar_conversas()

    elif opcao == "6":
        configurar_ia()

    elif opcao == "7":
        print("Programa encerrado")
        break

    else:
        print("Opção inválida")

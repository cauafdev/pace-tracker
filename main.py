def calcular_pace():

    print("Calcule seu pace: ")

    distancia = pegar_float("Distância (km): ")
    tempo = pegar_float("Tempo (min): ")

    pace = tempo / distancia

    print(f"Pace: {formatar_pace(pace)}")


def calcular_tempo():

    print("Calcule o tempo estimado de sua corrida: ")

    pace = ler_pace("Pace (Min/Km): ")
    distancia = pegar_float("Distância (Km): ")

    tempo = pace * distancia

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


while True:
    print("Escolha uma opção:")
    print("1 - Calcular pace")
    print("2 - Calcular tempo")
    print("3 - Sair")
    opcao = input("Digite uma opção: ")

    if opcao == "1":
        calcular_pace()

    elif opcao == "2":
        calcular_tempo()

    elif opcao == "3":
        print("Programa encerrado")
        break
    else:
        print("Opção inválida")

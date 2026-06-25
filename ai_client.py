import json
import os
import urllib.request
import urllib.error

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_CONFIG = os.path.join(BASE_DIR, "config.json")

SYSTEM_PROMPT = (
    "Você é um assistente amigável dentro de um app de corrida. "
    "Converse de forma natural e casual em português. "
    "Se o usuário só disser 'oi' ou 'olá', responda de forma simpática e pergunte como pode ajudar. "
    "NÃO dê dicas de corrida a menos que o usuário pergunte sobre isso. "
    "Quando perguntarem sobre corrida, aí sim ajude com treino, nutrição, lesões e motivação. "
    "Respostas curtas e diretas, no máximo 2-3 frases."
)


def carregar_config():
    try:
        with open(CAMINHO_CONFIG, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"ia_ativada": False, "modelo": "llama3.2:1b"}


def salvar_config(config):
    with open(CAMINHO_CONFIG, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)


class AIClient:

    def __init__(self):
        self.config = carregar_config()
        self.url = "http://localhost:11434/api/chat"

    def disponivel(self):
        try:
            req = urllib.request.Request("http://localhost:11434/api/tags")
            urllib.request.urlopen(req, timeout=3)
            return True
        except (urllib.error.URLError, OSError):
            return False

    def ia_ativada(self):
        return self.config.get("ia_ativada", False) and self.disponivel()

    def responder(self, pergunta, historico_recente=None):
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        if historico_recente:
            for msg in historico_recente[-5:]:
                messages.append({"role": "user", "content": msg["pergunta"]})
                messages.append({"role": "assistant", "content": msg["resposta"]})

        messages.append({"role": "user", "content": pergunta})

        body = json.dumps({
            "model": self.config.get("modelo", "llama3.2:1b"),
            "messages": messages,
            "stream": False,
        }).encode("utf-8")

        req = urllib.request.Request(
            self.url,
            data=body,
            headers={"Content-Type": "application/json"},
        )

        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["message"]["content"]
        except Exception as e:
            return f"Erro ao consultar IA: {e}"

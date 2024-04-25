# Quiz de Conhecimento Geral em Python

# Função para fazer uma pergunta e verificar a resposta
def fazer_pergunta(pergunta, opcoes, resposta_correta):
    print(pergunta)
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    resposta_usuario = input("Escolha a opção correta (digite o número): ").strip()
    if resposta_usuario == str(resposta_correta):
        print("Correto!")
        return True
    else:
        print(f"Incorreto. A resposta correta é a opção {resposta_correta}.")
        return False

# Pontuação inicial
pontuacao = 0

# Lista de perguntas, opções e respostas
perguntas = [
    {
        "pergunta": "Qual é a capital da Austrália?",
        "opcoes": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "resposta_correta": 3
    },
    {
        "pergunta": "Quem escreveu 'Dom Quixote'?",
        "opcoes": ["Miguel de Cervantes", "William Shakespeare", "Charles Dickens", "Fyodor Dostoevsky"],
        "resposta_correta": 1
    },
    {
        "pergunta": "Qual é o elemento mais abundante na crosta terrestre?",
        "opcoes": ["Ferro", "Oxigênio", "Silício", "Alumínio"],
        "resposta_correta": 3
    },
    {
        "pergunta": "Quem pintou 'A Noite Estrelada'?",
        "opcoes": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "resposta_correta": 1
    },
    {
        "pergunta": "Qual é o país com a maior área territorial do mundo?",
        "opcoes": ["China", "Canadá", "Rússia", "Estados Unidos"],
        "resposta_correta": 3
    }
]

# Iterar sobre as perguntas e fazer as perguntas
for pergunta_obj in perguntas:
    pergunta = pergunta_obj["pergunta"]
    opcoes = pergunta_obj["opcoes"]
    resposta_correta = pergunta_obj["resposta_correta"]
    if fazer_pergunta(pergunta, opcoes, resposta_correta):
        pontuacao += 1

# Exibir pontuação final
print("Pontuação final:", pontuacao, "de", len(perguntas))

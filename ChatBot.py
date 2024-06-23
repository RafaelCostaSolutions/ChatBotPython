from flask import Flask, request, jsonify

app = Flask(__name__)

# Respostas padrão do bot
responses = {
    "oi": "Olá! Como posso ajudar você?",
    "tchau": "Tchau! Tenha um bom dia!",
    "como você está?": "Estou apenas um bot, mas estou funcionando perfeitamente!"
}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    # Busca a resposta do bot
    bot_response = responses.get(user_message, "Desculpe, não entendi o que você disse.")

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)

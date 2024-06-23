Como funciona:

O código cria uma API web usando Flask.
A rota /chat espera uma requisição POST com uma mensagem do usuário.
O bot responde com base nas mensagens pré-definidas no dicionário responses.
Se a mensagem não estiver no dicionário, o bot responde com "Desculpe, não entendi o que você disse.

Este chat bot é um exemplo simples que ilustra como construir um serviço básico de chatbot usando Python e Flask. Aqui estão os detalhes do que ele é capaz de fazer:

Funcionalidades do Chat Bot
Responder a Mensagens Pré-definidas:

O bot tem um conjunto de respostas pré-definidas armazenadas em um dicionário chamado responses.
Quando o bot recebe uma mensagem de um usuário, ele procura essa mensagem no dicionário.
Se a mensagem estiver no dicionário, ele retorna a resposta correspondente.
Mensagens Suportadas:

"oi": O bot responde com "Olá! Como posso ajudar você?".
"tchau": O bot responde com "Tchau! Tenha um bom dia!".
"como você está?": O bot responde com "Estou apenas um bot, mas estou funcionando perfeitamente!".
Mensagens Não Reconhecidas:

Se a mensagem do usuário não está no dicionário responses, o bot responde com "Desculpe, não entendi o que você disse."

Limitações
Respostas Limitadas: O bot só pode responder às mensagens que estão explicitamente definidas no dicionário responses.
Interações Simples: Não há lógica avançada ou aprendizado de máquina. O bot não aprende com as interações e não tem memória de conversação.
Case Insensitive: A busca é case insensitive, mas a lógica não trata variações linguísticas ou erros ortográficos.
Este exemplo serve como um ponto de partida e pode ser expandido para incluir mais funcionalidades, como integração com APIs externas, processamento de linguagem natural (NLP), ou armazenamento de dados de conversas.

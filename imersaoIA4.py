#Configurações iniciais
import google.generativeai as genai


def listarModelosDisponiveis():
    #Listando os modelos disponíveis
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)


debug = False

GOOGLE_API_KEY="Coloque a chave da API aqui"
genai.configure(api_key=GOOGLE_API_KEY)

if debug == True:
    listarModelosDisponiveis()

generation_config = {
  "candidate_count": 1, # Quantidade de respostas
  "temperature": 0.5,   # Nivel de 'conservadorismo'(o quanto ele sera criativo) do Gemini
}

safety_settings={
    'HATE': 'BLOCK_NONE',       # Nivel de conteudo de ódio
    'HARASSMENT': 'BLOCK_NONE', # Nivel de conteudo assédio
    'SEXUAL' : 'BLOCK_NONE',    # Nivel de conteudo sexual
    'DANGEROUS' : 'BLOCK_NONE'  # Nivel de conteudo sensível
}

#Adicionando as configurações do gemini para a model
model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                                  generation_config=generation_config,
                                  safety_settings=safety_settings,)

chat = model.start_chat(history=[])

prompt = input('Esperando prompt: ')

#Sera feito um laço e enquanto o usuário não escrever a palavra "fim" não encerrara o programa
while prompt != "fim":
  response = chat.send_message(prompt)
  print("Resposta:", response.text, '\n\n')
  prompt = input('Esperando prompt: ')

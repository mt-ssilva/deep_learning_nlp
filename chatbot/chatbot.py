import numpy as np
import tensorflow as tf
import re
import time


#--- Pré-processamento dos dados ---
#Importação da base de dados

linhas = open('C:\Desenvolvimento\spyder-workspace\deep_learnig_nlp_chatbot\chatbot\movie_lines.txt').read().split('\n')
conversas = open('C:\Desenvolvimento\spyder-workspace\deep_learnig_nlp_chatbot\chatbot\movie_conversations.txt').read().split('\n')

#Criação de um dicionário para mapear cada linha com seu ID
id_para_linha = {}
for linha in linhas:
    _linha = linha.split(' +++$+++ ')
    if len(_linha) == 5:
        id_para_linha[_linha[0]] = _linha[4]

#Criação de uma lista com todas as conversas
conversas_id = []
for conversa in conversas[:-1]:
    _conversa = conversa.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
    conversas_id.append(_conversa.split(','))
    
#Separação das perguntas e respostas
perguntas = []
respostas = []
for conversa in conversas_id:
    for i in range(len(conversa)-1):
        perguntas.append(id_para_linha[conversa[i]])
        respostas.append(id_para_linha[conversa[i+1]])
        

def limpa_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"i'm", "i am", texto)
    texto = re.sub(r"he's", "he is", texto)
    texto = re.sub(r"she's", "she is", texto)
    texto = re.sub(r"that's", "that is", texto)
    texto = re.sub(r"what's", "what is", texto)
    texto = re.sub(r"where's", "where is", texto)
    texto = re.sub(r"\'ll", " will", texto)
    texto = re.sub(r"\'ve", " have", texto)
    texto = re.sub(r"\'re", " are", texto)
    texto = re.sub(r"\'d", " would", texto)
    texto = re.sub(r"won't", "will not", texto)
    texto = re.sub(r"can't", "cannot", texto)
    texto = re.sub(r"[-()#/@;:<>{}~+=?.|,]", "", texto)
    return texto
    
#Limpeza das perguntas e respostas
perguntas_limpas = []
for pergunta in perguntas:
    perguntas_limpas.append(limpa_texto(pergunta))

respostas_limpas = []
for resposta in respostas:
    respostas_limpas.append(limpa_texto(resposta))

#Criação de um dicionário que mapeia cada palavra e o número de ocorrências
palavras_contagem = {}
for pergunta in perguntas_limpas:
    for palavra in pergunta.split():
        if palavra not in palavras_contagem:
            palavras_contagem[palavra] = 1
        else:
            palavras_contagem[palavra] += 1

for resposta in respostas_limpas:
    for palavra in resposta.split():
        if palavra not in palavras_contagem:
            palavras_contagem[palavra] = 1
        else:
            palavras_contagem[palavra] += 1
        
#Remoção das palavras não frequentes e tokenização (dois dicionários)
limite = 20
perguntas_palavras_int = {}
numero_palavra = 0
for palavra, contagem in palavras_contagem.items():
    if contagem >= limite:
        perguntas_palavras_int[palavra] = numero_palavra
        numero_palavra += 1
        
respostas_palavras_int = {}
numero_palavra = 0
for palavra, contagem in palavras_contagem.items():
    if contagem >= limite:
        respostas_palavras_int[palavra] = numero_palavra
        numero_palavra += 1
        
#Adição de tokens no dicionário
tokens = ['<PAD>', '<EOS>', '<OUT>', '<SOS>']
for token in tokens:
    perguntas_palavras_int[token] = len(perguntas_palavras_int) + 1

for token in tokens:
    respostas_palavras_int[token] = len(respostas_palavras_int) + 1

#Criação do dicionário inverso com dicionário de respostas
respostas_int_palavras = {p_i: p for p, p_i in respostas_palavras_int.items()}

#Adição do token final de sentença <EOS> para o final de cada resposta
for i in range(len(respostas_limpas)):
    respostas_limpas[i] += ' <EOS>'


















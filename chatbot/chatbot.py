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

























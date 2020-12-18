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
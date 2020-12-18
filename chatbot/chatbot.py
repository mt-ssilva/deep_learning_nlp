import numpy as np
import tensorflow as tf
import re
import time


#--- Pré-processamento dos dados ---
#Importação da base de dados

linhas = open('movie_lines.txt').read().split('\n')
conversas = open('movie_conversations.txt').read().split('\n')


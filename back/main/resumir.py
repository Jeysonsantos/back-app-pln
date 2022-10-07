from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest
import re
import nltk
nltk.download('stopwords')
stopwords1 = set(stopwords.words('portuguese') + list(punctuation))

def resumir(link,stopwords1):
    try:
        link = Request(link,
                    headers={'User-Agent': ""})
        pagina = urlopen(link).read().decode('utf-8', 'ignore')
        
        soup = BeautifulSoup(pagina, "lxml")
        try:
            texto = soup.find(id="noticia").text
        except:
            texto = ""
            for paragraph in soup.find_all('p'):
                texto += paragraph.text

        sentencas = sent_tokenize(texto)
        palavras = word_tokenize(texto.lower())
        
        
        palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords1]
        palavras_sem=[]
        for w in palavras:
            if w not in stopwords1:
                palavras_sem.append(w)
        
        frequencia = FreqDist(palavras_sem_stopwords)
        
        sentencas_importantes = defaultdict(int)
        
        for i, sentenca in enumerate(sentencas):
            for palavra in word_tokenize(sentenca.lower()):
                if palavra in frequencia:
                    sentencas_importantes[i] += frequencia[palavra]
        
        
        idx_sentencas_importantes = nlargest(10, sentencas_importantes, sentencas_importantes.get)
        resumo_texto=''
        for i in sorted(idx_sentencas_importantes):
                resumo_texto=resumo_texto + sentencas[i]
            
        return resumo_texto
    except:
        return 'Não foi possível resumir esta URL, verifique-a.'
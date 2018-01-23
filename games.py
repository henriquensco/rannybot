from urllib.request import *
from bs4 import BeautifulSoup
import urllib
from paylib import payloadTextoSimples

def AguardadosDoAno(time, linkTime):
	siteIgn = "http://br.ign.com/ign-reportagens/56963/feature/os-18-games-mais-aguardados-de-2018"
	site = siteIgn + linkTime
	html = urlopen(site)
	bsObj = BeautifulSoup(html, "html.parser")

	blocoNome = bsObj.findAll('h3')
	print('Noticias: {}'.format(time))
	retorn = []
	for i in range(18):
		noticia = blocoNome[i].string

		retorno.append("Noticia: {}".format(noticia))

	return retorno
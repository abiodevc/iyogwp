from random import choice
import unidecode

def listapalavras():
    lista = '''açucena advogado    afta
alambique   alcachofra	algarismo
almanaque   almofariz	almoxarife
alquimia    altivez	alvíssaras
amendoim	amnésia	amplificar
ampulheta	ansioso	aplaudir
ascensão	asterisco	atlas
balacobaco	bandolim	barulhento
basquetebol	batráquio	beneficente
berimbau	bicarbonato	brusquidão
bugiganga	bumerangue  burocracia
caatinga	caboclo	cacareco
cacto	cadarço	cãibra
calibrado	camuflagem	candelabro
cassetete	catalisador	catequizar
cérebro	chamariz	cicatriz
cleptomaníaco	coincidência	companhia
condescender	consciente	crepúsculo
cronologia	deglutir	depredar
destruído	diapasão	digladiar
diretriz	dobradiça	ecossistema
embaixador	empecilho	entretido
entrevista	envernizar	enxaqueca
enxerido	escangalhado	escaravelho
escombro	esculacho	esfirra
espinafre	esplendor	estapafúrdio
estetoscópio	exceção	excêntrico
excepcional	faniquito	fascículo
flexível	frustrado	gargantilha
glândula	glicerina	glorioso
gnomo	grampeador	hamster
helicóptero	hemisfério	herdeiro
hermético	hierárquico	hieróglifo
hipocrisia	humanizar	idolatrada
imbróglio	inexorável	inflamado
influência	insignificância	interruptor
invertebrado	iogurte	irascível
lantejoula	licenciado	losango
madrasta	magnético	manteigueira
marimbondo	mesclar	meteorologia
mexerico	micróbio	microfone
microscópio	milionário	mordaz
nebulizador	oscilação	paralisado
pedágio	pernóstico	perturbar
piripaque	plissado	pneumático
pneumonia	poliomielite	potiguar
prescindir	presságio	privilégio
prodígio	prostração	prurido
psicanálise	psicólogo	quadriciclo
quádruplo	quinquilharia	reciclar
reflorescer	reivindicar	rescindir
retrógrado	retrovisor	ritmo
seborreia	sensatez	serelepe
serpentina	simplório	simulacro
sincrônico	sobrevivente	subsídio
supérfluo	suscetível	termômetro
torácico	travesseiro	trilogia
universidade	vangloriar	vaporizador
ventilador	xilindró	ziguezague
ziquizira	zodíaco	zumbido'''
    lista = unidecode.unidecode(lista)
    lista = lista.split()
    
    escolha = choice(lista)

    return escolha
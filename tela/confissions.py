import PySimpleGUI as sg
import requests
import time

def api():
	url = 'http://localhost:8000/'

	resp = requests.get(url)
	return resp.json()

def tela_get():
	sg.change_look_and_feel('Topanga')
	layout = [
		[sg.Text('A cada Clique uma nova Confissão',font=("Helvetica", 15))],
	    [sg.Button('Clique para Vê Confissões', font=("Helvetica",15))],
	    [sg.Output(size=(80,20),font=("Helvetica", 16))]

	]

	janela = sg.Window('Confissões').layout(layout)
	data = api()
	n = 0
	while True:
		Button, values = janela.Read()
		if Button == None:
			break
		if n == len(data):
			print('Não existe mais confissões. Feche para retornar a tela inicial\n')
			continue
		print(f'''
	===============================================
		titulo: {data[n]['title']}
		Confissão =>> {data[n]['confissions']}
	===============================================
			"\n"''')
		n+=1

def tela_post():
	url = 'http://localhost:8000/'
	sg.change_look_and_feel('Topanga')
	layout = [
		[sg.Text('Digite o titulo da Confissão: ', font=("Helvetica", 15)),sg.Input(size=(20,10), key='title')],
	    [sg.Text()],
	    [sg.Text('Digite Sua Confissão: ',font=("Helvetica", 15)),sg.Input(size=(30,0), key='confissions')],
	    [sg.Text()],
	    [sg.Button('Enviar Informações')],
	    [sg.Output(size=(64,20),font=("Helvetica", 16))]
	]
	janela = sg.Window('Envio de Informações',layout=layout)

		
	event, values = janela.Read()

	title = values['title']
	confissions = values['confissions']

	data = {
	'csrfmiddlewaretoken': '3bOMcHPChTWzi6CN01aoNRVrTnOUYVWafIO8eIPXuhMGUcL50iC8Adw6swmiILnh',
	'title': title,
	'confissions': confissions
	}

	resp = requests.post(url, data=data)

	if resp.status_code != 201:
		print('Mensagem não enviada. Feche e abra novamente essa janela para poder enviar.')
	else:
		print('Mensagem enviada com sucesso, para voltar feche essa janela.')
	time.sleep(3)



def tela_inicio():
	sg.change_look_and_feel('Topanga')
	layout = [
		[sg.Text('Esse é um programa de confissões e comentários. Deixe um comentário sobre sua vida ou veja de outras pessoas.',font=("Helvetica", 15))],
	    [sg.Text()],
	    [sg.Text('Quer enviar sua confissão? Clique Aqui => ',font=("Helvetica", 15)),sg.Button('Enviar Confissão',font=("Helvetica", 15))],
	    [sg.Text()],
	    [sg.Text('Quer vê outras confissões? Clique Aqui => ',font=("Helvetica", 15)) ,sg.Button('Vê Confissões',font=("Helvetica", 15))],
	]
	janela = sg.Window('Tela Inicial').layout(layout)
	while True:
		Button, values = janela.Read()
		if Button == None:
			break
		
		elif Button == 'Enviar Confissão':
			tela_post()
		elif Button == 'Vê Confissões':
			tela_get()


tela_inicio()

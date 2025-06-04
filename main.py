import pyperclip
import pyshorteners
import FreeSimpleGUI as sg
from numpy.ma.core import around
from win32con import BLACKNESS

sg.theme('DarkGray15')
layout_fixo = [
    [sg.Text('Encurte sua url!', size=(40, 1),  justification='center', font=('Arial', 20, 'bold'))],
    [sg.Text('Insira sua url:', size=(40, 1), justification='center',font=('Arial', 15))],
    [sg.Input(key='-URL_INPUT-', size=(45, 1), justification='center',font=('Arial', 15))],
    [sg.Push(), sg.Button('Encurtar', font=('Arial', 15), border_width=0), sg.Button('Copiar',font=('Arial', 15), border_width=0), sg.Push()],
    [sg.Text('Sua Url:', size=(40, 1), justification='center',font=('Arial', 15))],
    [sg.Input(key='-URL_SHORT-', size=(45, 1), text_color='Black', justification='center',disabled=True,font=('Arial', 15))]
]

def urlshortener():
    shortener = pyshorteners.Shortener().tinyurl.short(valores['-URL_INPUT-'])
    window['-URL_SHORT-'].update(shortener)

def copyclipboard():
    urlToCopy = window['-URL_SHORT-'].get()
    pyperclip.copy(urlToCopy)

window = sg.Window('Url Shortner', layout_fixo, finalize=True, element_justification='c')

while True:
    try:
        evento, valores = window.read()

        if evento == sg.WIN_CLOSED:
            break

        if evento == 'Encurtar':
            if not valores['-URL_INPUT-']:
                sg.popup('Por favor, insira uma URL correta para encurtar.', title='ERRO')
                continue

            if not valores['-URL_INPUT-'].startswith(('http://', 'https://')):
                sg.popup('URL inválida. A URL deve começar com http:// ou https://', title='ERRO')
                continue

            urlshortener()

        if evento == 'Copiar':
            if not valores['-URL_SHORT-']:
                sg.popup('Nenhuma URL encurtada para copiar.', title='ERRO')
                continue
            copyclipboard()

    except Exception as e:
        sg.popup(f'Ocorreu um erro: {str(e)}', title='ERRO')
        continue

window.close()
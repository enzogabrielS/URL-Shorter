import pyperclip
import pyshorteners
import FreeSimpleGUI as sg

sg.theme('DarkGray15')
layout_fixo = [
    [sg.Text('Encurte sua url!', size=(40, 1), justification='center')],
    [sg.Text('Insira sua url:', size=(40, 1), justification='center')],
    [sg.Input(key='-URL_INPUT-', size=(40, 1), justification='center')],
    [sg.Push(), sg.Button('Encurtar'), sg.Button('Copiar'), sg.Push()],
    [sg.Text('Sua Url:', size=(40, 1), justification='center')],
    [sg.Input(key='-URL_SHORT-', size=(40, 1), text_color='Black', justification='center',disabled=True)]
]

def urlshortener():
    shortener = pyshorteners.Shortener().tinyurl.short(valores['-URL_INPUT-'])
    window['-URL_SHORT-'].update(shortener)

def copyclipboard():
    urlshort = window['-URL_SHORT-'].get()
    pyperclip.copy(urlshort)

window = sg.Window('Url Shortner', layout_fixo, finalize=True, element_justification='c')

while True:
    evento, valores = window.read()


    if evento == sg.WIN_CLOSED:
        break

    if evento == 'Encurtar':
        if not valores['-URL_INPUT-']:
            sg.popup('Por favor, insira uma URL correta para encurtar.', title='ERROR')
            continue


        urlshortener()

    if evento == 'Copiar':
        copyclipboard()


window.close()
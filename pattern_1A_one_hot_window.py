import PySimpleGUI as sg


layout = [[sg.Text('My one-shot window.')],
                 [sg.InputText(key=None), ]
                 # [sg.InputText(key='-IN-'), ],
                 [sg.Submit(), sg.Cancel()]]

window = sg.Window('Window Title', layout)

event, values = window.read()
window.close()

# by key, or by value
text_input = values[0]  #  with [sg.InputText(key=None), ]
# text_input = values['-IN-']  # [sg.InputText(key='-IN-'), ],

sg.popup('You entered', text_input)

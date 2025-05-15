import FreeSimpleGUI as sg

def convert(feet, inches):
    meters = feet * .3048 + inches * 0.0254
    return meters

labelft = sg.Text("Ingresa los Pies: ")
inputft = sg.InputText(key="inputft")

labelin = sg.Text("Ingresa las Pulgadas: ")
inputin = sg.InputText(key="inputin")
button = sg.Button("Convertir")

output = sg.Text(key="output")

exit = sg.Button("Salir")

window = sg.Window("Convertidor", layout=[[labelft, inputft], [labelin, inputin], [button, output], [exit]])

while True:
    event, values = window.read()
    print(event, values)
    ft = float(values["inputft"])
    inc = float(values["inputin"])
    result = convert(ft, inc)
    window["output"].update(f"{result}m")
    if event == exit:
        break

window.close()



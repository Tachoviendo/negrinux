import subprocess

def changeLayout():
    comando = ["setxkbmap","-query"]
    cositas= subprocess.run(comando, capture_output=True, text=True)
    return cositas

cadena = changeLayout().stdout.split()
layout = cadena[len(cadena)-1]

if layout == 'us':
    subprocess.run(['setxkbmap', 'latam'])
else:
    subprocess.run(['setxkbmap','us'])


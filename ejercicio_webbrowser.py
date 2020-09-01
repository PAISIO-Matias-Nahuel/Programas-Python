import webbrowser, sys, pyperclip

sys.argv

# checkear si la linea de comando fue escrita

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open(r'https://www.google.com.ar/maps/' + address)


import os
import urllib.request
import zipfile
currentversion = 4

def updatejexirnow():
    updates = input('Do you want to check for updates?\n(this will require a internet connection\ny/n')
    if updates == 'y':
        url = 'https://drive.google.com/uc?export=download&id=1PYNBTEYPZ4Y-Rs7oLLlWGzpyJ0Rs1df_'
        urllib.request.urlretrieve(url, 'update.txt')
        with open('update.txt') as f:
            contents = f.read()
            if int(contents) >= int(currentversion):
                yni = input('Update Available Do you want to Go to Install Page?y/n\n')
                if yni == 'y':
                    url = 'https://drive.google.com/uc?export=download&id=1B4XWFj9HPNHKnPSYz97hXEUDY1LAWuMZ'
                    urllib.request.urlretrieve(url, 'wthwat.txt')
                    with open('wthwat.txt') as f:
                        contents1 = f.read()
                        urllib.request.urlretrieve(contents1, 'Jexir.zip')
                        jexir_zip = zipfile.ZipFile('Jexir.py.zip')
                        jexir_zip.extractall()

                    jexir_zip.close()
                    os.remove('Jexir.py.zip')
                    os.remove('wthhat.txt')
                    os.remove('update.txt')

                if yni == 'n':
                    print('Ok')
            if int(contents) == currentversion:
                print('You Are Using the current version of Jexir')
            if int(contents) > currentversion:
                print("Error The Version You Are Using Does not E?")

    if updates == 'n':
        print('Ok')

import webbrowser
from random import randint


def webzite():
    randomn = randint(0, 5)
    web = input('Which Website\nNetflix(1)\nSearch Engine(2)\nGitHub(3)\nWiki(4)\nCustom(0)\n')
    if web == '1':
        webbrowser.open('http://netflix.com', new=2)
    if web == '2':
        webbrowser.open('https://duckduckgo.com/', new=2)
    if web == '3':
        webbrowser.open('https://github.com/TheSammyJam1/', new=2)
    if web == '4':
        webbrowser.open('https://en.wikipedia.org/', new=2)
    if web == '0':
        ex = 'this should never happen'
        if randomn == 0:
            ex = 'duckduckgo.com'
        if randomn == 1:
            ex = 'github.com'
        if randomn == 2:
            ex = 'voice.google.com'
        if randomn == 3:
            ex = 'mail.google.com'
        if randomn == 4:
            ex = 'www.wunderground.com/forecast/us/or/woodburn/97071'
        if randomn == 5:
            ex = 'youtube.com'

        cus = 'https://' + input('Enter Web Address\nex:' + ex + '\n')
        webbrowser.open(cus, new=2)

# Import What Needed
from functions.updatejex import currentversion
from functions.options import canthelpmeo, jokeo, matho, webo, feedbacko, domylaundryo, updatejexo, jwikio, getwatero, commando

print('Hello, I am JexirTheAssistant V.' + str(currentversion))
print('I am Still In Closed Beta so you Might encounter issues')
print('If so Please contact me on my discord channel')
print('https://sammyjam1.000webhostapp.com/jexir-feedback.html')

print('How may I help you')


def jexir():
    def anny():
        print('\nAnything else')
        jexirqa()

    def jexirqa():
        # Which Command To Execute
        print('Type which number collates with your Reply\nOr type 0 For list of commands')
        jexirq = input()
        # List of Commands
        if jexirq == commando:
            from functions.commands import commands
            commands()
            jexirqa()
        # 1 Cant Help You
        if jexirq == canthelpmeo:
            print('Sorry')
            input('Hit Enter to Quit')
            quit()
        # 3 get me water
        if jexirq == getwatero:
            print('No Can Do\nCant get you water\nSorry')
            anny()
        # 4 tell me a joke
        if jexirq == jokeo:
            from functions.joke import joke
            joke()
            anny()
        # 5 math
        if jexirq == matho:
            from functions.math import math
            math()
            anny()
        # Website
        if jexirq == webo:
            from functions.web import webzite
            webzite()
            anny()
        # Leave Feedback
        if jexirq == feedbacko:
            from functions.feedback import feedback
            feedback()
        # Do My Laundry
        if jexirq == domylaundryo:
            from functions.domylaundry import domylaundry
            domylaundry()
        # Update
        if jexirq == updatejexo:
            from functions.updatejex import updatejexirnow
            updatejexirnow()
        # JWiki
        if jexirq == jwikio:
            from functions.jwiki import jwiki
            jwiki()
        # Quit via q
        if jexirq == 'q':
            quit()
        anny()

    jexirqa()


jexir()

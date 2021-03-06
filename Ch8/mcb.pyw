#! python3
# mcb.pyw - saves and loads pieces of text to the clipboard
# usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - loads keyword to clipboard
#        py.exe mcb.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2

    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()

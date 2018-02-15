#! python3
# pw.py - An insecure password locker app.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

# first item in sys.arv is string containing app's filename
# second item is the first command line arg
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python password.py [account] - copy account password')
    sys.exit()

    account = sys.arv[1] # first command line arg is the account name
   
    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)



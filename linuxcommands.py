from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as request

# loading results
client = request('https://phoenixnap.com/kb/linux-commands-cheat-sheet')
page = client.read()
client.close()
results = soup(page, 'html.parser')

# simplifying and processing results
h = results.findAll('p')
work = h[10:144]
task = []
for each in work:
    task.append(each.text.strip())
unprocessedcommands = results.findAll('pre')
commands = []

for each in unprocessedcommands:
    commands.append(each.code.text.strip())

for _ in task:
    if 'Note' in _ or (':' not in _):
        del task[task.index(_)]
del task[task.index('Chown command in Linux changes file and directory ownership.')]

# displaying results
for i in range (126):
    print(str(i+1) + ' ' + task[i])
    print(" ")
    print(commands[i])
    print(" ")
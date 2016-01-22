import subprocess as sub
from os import listdir
files_to_recompile = listdir('blog_text')
links = open('links.txt')
linksTitles = [i.split(' : ')[1] for i in links.read().split('\n')]
links.close()
for i, j in enumerate(files_to_recompile):
	command = sub.Popen('python convertToHTML.py ' + j + ' "' + linksTitles[i] + '"', stdin = sub.PIPE)
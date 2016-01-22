from sys import argv

filename = argv[1]
title = argv[2]
txt = open('blog_text/' + filename)

text = txt.read()
disqus = open('templateFiles/disqus.html')
text += disqus.read()
disqus.close()
txt.close()

defBegin = open('templateFiles/defaultBegin.html')
defaultBegin = defBegin.read()
defBegin.close()

defEnd = open('templateFiles/defaultEnd.html')
defaultEnd = defEnd.read()
defEnd.close()

result = open('blog_posts/' + (filename.split('.')[0] + '.html').split('/')[-1], 'w')
result.write(defaultBegin + '\n' + text + '\n' + defaultEnd)
result.close()

links = open('links.txt', 'r')
linkList = [i.split(' : ')[0] for i in links.readlines()]
links.close()
links = open('links.txt', 'a')
if 'http://u8y7541.github.io/blog_posts/' + (filename.split('.')[0] + '.html').split('/')[-1] not in linkList:
	links.write('\n' + 'http://u8y7541.github.io/blog_posts/' + (filename.split('.')[0] + '.html').split('/')[-1] + ' : ' + title)
links.close()
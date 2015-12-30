filename = input('File to HTMLify: ')
title = input('Title of post: ')
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

links = open('links.txt', 'a')
links.write('\n' + 'http://u8y7541.github.io/blog_posts/' + (filename.split('.')[0] + '.html').split('/')[-1] + ' : ' + title)
links.close()
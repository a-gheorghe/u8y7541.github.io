filename = input('File to HTMLify: ')
title = input('Title of post: ')
resultname = input('Output folder: ')
txt = open(filename)
text = txt.read()
txt.close()
defaultBegin = \
'''<html>
<head>
	<title>u8y7541's Website</title>
	<link rel = 'stylesheet' href = 'main.css'>
	<link rel = 'stylesheet' href = 'prism.css'>
	
	<meta http-equiv="cache-control" content="max-age=0" /> <!--Cache control so I'm always updated-->
	<meta http-equiv="cache-control" content="no-cache" />
	<meta http-equiv="expires" content="0" />
	<meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
	<meta http-equiv="pragma" content="no-cache" />
	<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
	<meta http-equiv="Pragma" content="no-cache" />
	<meta http-equiv="Expires" content="0" />
</head>
<body>
	<a href="https://github.com/u8y7541"> <!--Fork Me On GitHub Ribbon Image-->
		<img style="position: absolute; top: 0; right: 0; border: 0;" src="https://camo.githubusercontent.com/e7bbb0521b397edbd5fe43e7f760759336b5e05f/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f677265656e5f3030373230302e706e67" alt="Fork me on GitHub" data-canonical-src="https://s3.amazonaws.com/github/ribbons/forkme_right_green_007200.png">
	</a>
	<div id = 'nav'>
		<ul>
			<li id = 'gitlinks'>
				<a>Git Repos</a>
				<ul id = 'git'>
				</ul>
			</li>
			<li id = 'profilelinks'>
				<a>Accounts</a>
				<ul id = 'profiles'>
					<li><a href = 'https://plus.google.com/u/0/+u8y7541TheAwesomePerson/posts'>Google+</a></li>
					<li><a href = 'https://stackoverflow.com/users/3917838/python-guy'>Stack Overflow</a></li>
					<li><a href = 'https://github.com/u8y7541'>GitHub</a></li>
					<li><a href = 'https://scratch.mit.edu/users/u8y7541'>Scratch</a></li>
				</ul>
			</li>
			<li id = 'bloglinks'>
				<a>Blog Posts (WIP)</a>
				<ul id = 'blog'>
				</ul>
			</li>
			<li id = 'scratchlinks'>
				<a>Scratch Projects (WIP)</a>
				<ul id = 'scratch'>
				</ul>
			</li>
		</ul>
	</div>
	<div id = 'content'>'''
defaultEnd = \
'''</div>
	<script src = 'gitquery.js'></script>
	<!--Configuring MathJax from the CDN-->
	<script type="text/x-mathjax-config"> 
	MathJax.Hub.Config({
		tex2jax: {
			inlineMath: [ ['$','$'] ],
			processEscapes: true
		}
	});
	</script>
	<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
	<script type = "text/javascript" src = 'prism.js'></script>
</body>
</html>'''
result = open(resultname + '/' + (filename.split('.')[0] + '.html').split('/')[-1], 'w')
result.write(defaultBegin + '\n' + text + '\n' + defaultEnd)
result.close()
links = open('links.txt', 'a')
links.write('\n' + 'http://u8y7541.github.io/blog_posts/' + (filename.split('.')[0] + '.html').split('/')[-1] + ' : ' + title)
links.close()
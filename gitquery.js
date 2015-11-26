var req = new XMLHttpRequest();
req.open('GET', 'https://api.github.com/users/u8y7541/repos', false);
req.send(null);
if (req.status == 200)
  a = req.responseText;
a = JSON.parse(a);
b = [];
for (i in a) {
	b.push(a[i]['name']);
}
result = '';
for (i in b.reverse()) {
	result += '<li><a href = https://github.com/u8y7541/' + b[i] + '>' + b[i] + '</a></li>';
}
document.getElementById('git').innerHTML = result;
req = new XMLHttpRequest();
req.open('GET', 'http://u8y7541.github.io/links.txt', false)
req.send(null);
if (req.status == 200)
	a = req.responseText;
console.log(a);
a = a.split('\n')
result = '';
for (i in a) {
	result += '<li><a href = ' + a[i].split(' ')[0] + '>' + a[i].split(' : ')[1] + '</a></li>'
}
document.getElementById('blog').innerHTML = result;
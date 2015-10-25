var req = new XMLHttpRequest();
req.open('GET', 'https://api.github.com/users/u8y7541/repos', false);
req.send(null);
if(req.status == 200)
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
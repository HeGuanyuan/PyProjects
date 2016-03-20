from urllib import request, parse

url = 'http://httpbin.org/post'
parms = {
    'name1': 'value1',
    'name2': 'value2'
}

# 定义http头
extraHeader = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}

queryString = parse.urlencode(parms)

# 如果是post，
# u = request.urlopen(url + '?' + queryString)

req = request.Request(url, queryString.encode('ascii'), headers=extraHeader)
u = request.urlopen(req)
resp = u.read()
print(u)

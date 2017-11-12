import urllib.request
import urllib.parse
import json

content = input("请输入需要翻译的内容：")

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='
data = {
    'i': content,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1505653077725',
    'sign':'467d88b4cdc9c6adca72855020b6a1e8',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_CLICKBUTTION',
    'typoResult':'true'    
}
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')
target = json.loads(html)

print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))

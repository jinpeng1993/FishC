import urllib.request
import urllib.parse
import json
from tkinter import *

def YouDaoTranslate(event=None):
    content = s_from.get()
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
    s_to = target['translateResult'][0][0]['tgt']
    text_to.delete(0.0,END)
    text_to.insert('end', s_to)
    # print("翻译结果:" + s_to)
    # print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))

frame = Tk()
# print("1")
width = 360
height = 60
screenwidth = frame.winfo_screenwidth()
screenheight = frame.winfo_screenheight()
frame.geometry('%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2))
label_from = Label(frame,text = "翻译内容:")
label_to = Label(frame,text = "翻译结果:")
label_from.grid(row = 0,column = 0)
label_to.grid(row = 1,column = 0)
# print("2")
s_from = StringVar()
text_from = Entry(frame, validate='key', textvariable=s_from, width=35)
# print("3")
#text_from.pack()#can not used with grid
# print("4")
# content = s_from.get()
# print("5")
text_from.bind('<Return>', YouDaoTranslate)
# print("6")
text_to = Text(frame, height=1, width=40)
text_from.grid(row = 0,column = 1)
text_to.grid(row = 1,column = 1)
frame.title("有道在线翻译")
frame.mainloop()
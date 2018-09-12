#socket和GUI  做的可以作为客户端发送，可以作为服务器接收
from tkinter import *
from tkinter import ttk
import socket
import threading
import datetime
from tkinter import filedialog
from PIL import Image,ImageTk

dggram=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
dggram.connect(("114.114.114.114",80))#?????

# dggram.bind(("", 6000))

root=Tk()
root.title("MyQQ")
root.geometry("500x450+100+50")


fm=Frame(height=230, width=110,highlightbackground="#ccc",highlightthickness=1)
fm.pack_propagate(0)#固定frame大小，如果不设置，frame会随着标签大小改变
fm.place(x=20,y=30)

text7=Label(root,text="网络设置",font=("Microsoft JhengHei", 10))
text7.place(x=44,y=18)
#协议类型
text1=Label(root,text="(1) 协议的类型",font=("Microsoft JhengHei", 8))
text1.place(x=32,y=46)
info={
    "UDP",
    "TCPfuwu Client",
    "TCPfuwu Server"
}
text1a=StringVar(value='')
text1a=ttk.Combobox(root,value=tuple(info),textvariable=text1a)
text1a.place(x=30,y=70,width=90,height=20)
text1a.current(1) #设置当前显示第几个

#本地IP地址
text4=Label(root,text="(2) 本地IP地址",font=("Microsoft JhengHei", 8))
text4.place(x=32,y=100)

valuec=StringVar(root, value=dggram.getsockname()[0])
dggram.close()
text4a=Entry(root,textvariable=valuec,state=DISABLED)
text4a.place(x=30,y=124,width=90,height=20)

#本地端口号
text5=Label(root,text="(3) 本地端口号",font=("Microsoft JhengHei", 8))
text5.place(x=32,y=156)

valued=IntVar(root, value='6000')
text5a=Entry(root,textvariable=valued)
text5a.place(x=30,y=180,width=90,height=20)

fm2=Frame(height=150, width=110,highlightbackground="#ccc",highlightthickness=1)
fm2.pack_propagate(0)#固定frame大小，如果不设置，frame会随着标签大小改变
fm2.place(x=20,y=280)

text6=Label(root,text="目标位置",font=("Microsoft JhengHei", 10))
text6.place(x=48,y=268)
#目标IP地址
text2=Label(root,text="(1) 目标IP地址",font=("Microsoft JhengHei", 8))
text2.place(x=32,y=306)

valuea=StringVar(root, value='192.168.3.161')
text2a=Entry(root,textvariable=valuea)
text2a.place(x=30,y=330,width=90,height=20)

#目标端口号
text3=Label(root,text="(2) 目标端口号",font=("Microsoft JhengHei", 8))
text3.place(x=32,y=366)

valueb=StringVar(root, value='8080')
text3a=Entry(root,textvariable=valueb)
text3a.place(x=30,y=390,width=90,height=20)

fm3=Frame(height=150, width=300,highlightbackground="#ccc",highlightthickness=1)
fm3.pack_propagate(0)#固定frame大小，如果不设置，frame会随着标签大小改变
fm3.place(x=150,y=30)

text8=Label(root,text="数据接收区域",font=("Microsoft JhengHei", 10))
text8.place(x=260,y=18)
#接收文本框
text10=Text(root)
text10.place(x=150,y=50,width=300,height=180)

fm4=Frame(height=130, width=300,highlightbackground="#ccc",highlightthickness=1)
fm4.pack_propagate(0)#固定frame大小，如果不设置，frame会随着标签大小改变
fm4.place(x=150,y=280)

text9=Label(root,text="数据发送区域",font=("Microsoft JhengHei", 10))
text9.place(x=260,y=270)
#发送文本框
text11=Text(root)
text11.place(x=150,y=300,width=300,height=110)

#作为客户端发送按钮

def fasong():
    fasongevent.set()
    if not cc.is_alive():
        cc.start()
botton1=Button(root,text="发送",command=fasong)
botton1.config(activebackground="green",activeforeground="#fff")
botton1.place(x=400,y=360,width=50,height=50)


dggram4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
def qidong():
    while True:
        if not fasongevent.isSet():
            fasongevent.wait()
        dizhi = text2a.get()
        duankou = int(text3a.get())
        content=text11.get(0.0, END)
        dggram4.sendto(content.encode("gbk"),(dizhi, duankou))

        fasongevent.clear()

cc=threading.Thread(target=qidong)
fasongevent=threading.Event()

#接受时间选择
showtime=IntVar(value=1)
timecheck=Checkbutton(root,text="显示接受时间",onvalue=1,offvalue=0,variable=showtime)
timecheck.place(x=250,y=240,width=100,height=20)

#保存数据
filename=StringVar(value="")
def savecon():
    filename.set(filedialog.asksaveasfilename(defaultextension=".txt", initialfile="未命名", initialdir="E://"))
    if filename.get():
        message = text10.get(0.0, END)
        fh = open(filename.get(), 'w')
        fh.write(message)
        fh.close()
save=Button(root,text="保存数据",command=savecon)
save.config(fg="blue",bd=0)
save.place(x=355,y=240,width=80,height=20)

#清空接收区域
def clear():
    text10.delete(0.0,END)
clearcheck=Button(root,text="清空",command=clear)
clearcheck.config(activebackground="red",activeforeground="#fff")
clearcheck.place(x=400,y=180,width=50,height=50)

#作为服务器更新按钮
def connecto():
    yilian = Label(root, text="已连接%s端口"%(valued.get()))
    yilian.config(fg="blue")
    yilian.place(x=150, y=240)
    threading.Thread(target=serves).start()
Localconnect = Button(root, text="连接", command=connecto)
Localconnect.config(width=10)
Localconnect.place(x=35, y=215)
def serves():
    while True:
        dggram2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        dggram2.bind((valuec.get(), valued.get()))
        data = dggram2.recvfrom(1024)
        content, address = data
        aa = content.decode(encoding="gbk")
        if showtime.get() == 1:
            nowtime = datetime.datetime.now()
            show = nowtime.strftime('[%Y.%m.%d-%H:%M:%S]:')
            text10.insert(INSERT, show)
            text10.insert(INSERT, aa)
            text10.insert(INSERT, "\n")
        elif showtime.get() == 0:
            text10.insert(INSERT, aa)
            text10.insert(INSERT, "\n")
        dggram2.close()
root.mainloop()




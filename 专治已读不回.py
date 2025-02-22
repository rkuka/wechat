from wxauto import WeChat
import tkinter as tk
from tkinter import messagebox

wx = WeChat()
wx.GetSession()

root = tk.Tk()
root.title("专治已读不回")

def __send__():
    try:
        target = target_entry.get()
        msg = msg_entry.get()
        num = int(num_entry.get())
        wx.ChatWith(target)
        for i in range(num):
            wx.SendMsg(msg)
        messagebox.showinfo("提示","消息发送成功！")
    except Exception as e:
        messagebox.showwarning("WARNING","消息发送失败！")

def __exit__():
    root.destroy()

target_lable = tk.Label(root,text="请输入要发送的用户昵称：")
target_lable.pack()
target_entry = tk.Entry(root)
target_entry.pack()

msg_lable = tk.Label(root,text="请输入要发送的信息：")
msg_lable.pack()
msg_entry = tk.Entry(root)
msg_entry.pack()

num_lable = tk.Label(root,text="请输入要发送的次数：")
num_lable.pack()
num_entry = tk.Entry(root)
num_entry.pack()

send = tk.Button(root,text="确定",command=__send__)
send.pack()

close = tk.Button(root,text="退出",command=__exit__)
close.pack()

root.mainloop()
from wxauto import WeChat

wx = WeChat()
wx.GetSession()

while True:
    target = str(input("请输入要发送到的用户名："))
    msg = input("请输入要发送的信息：")
    num = int(input("请输入要发送的次数："))
    try:        
        wx.ChatWith(target)
        for i in range(num):
            wx.SendMsg(msg)
    except Exception as e:
        break
    if int(input("是否退出(1/0):")) == 1 : break
    else : continue
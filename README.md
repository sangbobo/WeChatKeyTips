# WeChatKeyTips

## 微信消息关键字提醒

## 初衷

  现在用微信的越来越多，公司的一些通知也用微信来进行发送，无奈自己上微信的频率太低，又怕错过重要消息，所以才有了这个软件。
    
  感谢 [ItChat](https://github.com/littlecodersh/ItChat) 提供的微信API接口

## 说明

  
  需要python3.5版本进行运行
  
  需要安装前置
      
      pip install itchat
      
  安装好后运行
      
      python run.py
        
    

## 配置信息

### config.json

  
    {
        "mail_info": {
          "host": "smtp服务器",
          "account": "邮箱账号",
          "password": "密码",
          "sender": "发送者邮箱账号",
          "receivers": "接受者邮箱账号"
        },
        "keys":["桑博","所有人","通知","大家","全体"],
        "log_path":"out.txt"
      }
  
  
  记得开启邮件设置中的smtp

  建议account 和 sender 和 receivers 都一致，自己给自己发邮件，不然有些服务商可能会把你的邮件当做垃圾邮件，导致发送失败。
   
  keys是关键字列表，邮件会发送带有关键字的消息。
    
  如果有什么问题，可以进行提问。
  
## 相关文章

  [微信消息关键字提醒](http://blog.csdn.net/CutelittleBo/article/details/71515006)
  
## 关于一些可能遇到的问题

### 在Linux上邮件发送失败

  看看25邮件端口是发打开，如果没有打开使用命令

    #打开发送邮件的服务器
    service sendmail start
    
### 在Linux上进行登录的问题（参考：[ItChat](https://github.com/littlecodersh/ItChat)）

  命令行二维码

  通过以下命令可以在登陆的时候使用命令行显示二维码：

    itchat.auto_login(enableCmdQR=True)

  部分系统可能字幅宽度有出入，可以通过将enableCmdQR赋值为特定的倍数进行调整：

  如部分的linux系统，块字符的宽度为一个字符（正常应为两字符），故赋值为2

    itchat.auto_login(enableCmdQR=2)


  默认控制台背景色为暗色（黑色），若背景色为浅色（白色），可以将enableCmdQR赋值为负值：

    itchat.auto_login(enableCmdQR=-1)

    

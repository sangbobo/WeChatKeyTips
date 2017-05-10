# WeChatKeyTips


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
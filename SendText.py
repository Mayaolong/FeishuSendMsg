import json
import requests
class FeishuTalk:

    # 机器人webhook
    # chatGPT_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/9077d8e8-8fb1-493f-a04c-1041cdd94313'

    #小虎 https://open.feishu.cn/open-apis/bot/v2/hook/4b5c587f-4a79-49ee-8cdf-933c47672802
    chatGPT_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/4b5c587f-4a79-49ee-8cdf-933c47672802'


    # 发送文本消息
    def sendTextmessage(self, content):
        url = self.chatGPT_url
        headers = {
            "Content-Type": "application/json; charset=utf-8",
        }
        payload_message = {
            "msg_type": "text",
            "content": {
            	# @ 单个用户 <at user_id="ou_xxx">名字</at>
                #"text": content + "<at user_id=\"bf888888\">test</at>"  
                # "text": content   
                # @ 所有人 <at user_id="all">所有人</at>
                 "text": content + "<at user_id=\"all\">所有人</at>"
            }
        }
        # response = requests.post(url=url, data=json.dumps(payload_message), headers=headers)
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload_message))
        print(response.text)
        return response.json
    
 # 执行发送文本消息
if __name__ == '__main__':
     # 执行发送文本消息
    content = "UT 生活不止眼前的苟且，还有诗和远方!"
    FeishuTalk().sendTextmessage(content)

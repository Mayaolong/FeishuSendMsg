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
    "msg_type": "interactive",
    "card": {
  "config": {
    "wide_screen_mode": False
  },
  "header": {
    "title": {
      "tag": "plain_text",
      "content": "今日单元测试结果"
    }
  },
  "elements": [
    {
      "tag": "div",
      "fields": [
        {
          "is_short":True,
          "text": {
            "tag": "plain_text",
            "content": "ExamBE ✅✘✘❌ "
          }
        },
        {
          "is_short": True,
          "text": {
            "tag": "lark_md",
            "content": "**休假类型：**\n年假 "
          }
        },
        {
          "is_short": False,
          "text": {
            "tag": "lark_md",
            "content": ""
          }
        },
        {
          "is_short": False,
          "text": {
            "tag": "lark_md",
            "content": "**时间：**\n2020-4-8 至 2020-4-10（共3天）"
          }
        },
        {
          "is_short": False,
          "text": {
            "tag": "lark_md",
            "content": ""
          }
        },
        {
          "is_short": True,
          "text": {
            "tag": "lark_md",
            "content": "**备注**\n因家中有急事，需往返老家，故请假"
          }
        }
      ]
    },
    {
      "tag": "hr"
    },
    {
      "tag": "action",
      "layout": "bisected",
      "actions": [
        {
          "tag": "button",
          "text": {
            "tag": "plain_text",
            "content": "批准"
          },
          "type": "primary",
          "value": {
            "chosen": "approve"
          }
        },
        {
          "tag": "button",
          "text": {
            "tag": "plain_text",
            "content": "拒绝"
          },
          "type": "primary",
          "value": {
            "chosen": "decline"
          }
        }
      ]
    }
  ]
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

from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.ding import Bot as DingBot, MessageSegment, MessageEvent

markdown = on_command("markdown", to_me())


@markdown.handle()
async def test_handler(bot: DingBot):
    message = MessageSegment.markdown(
        "Hello, This is NoneBot",
        "#### NoneBot  \n> Nonebot 是一款高性能的 Python 机器人框架\n> ![screenshot](https://v2.nonebot.dev/logo.png)\n> [GitHub 仓库地址](https://github.com/nonebot/nonebot2) \n"
    )
    await markdown.finish(message)


actionCardSingleBtn = on_command("actionCardSingleBtn", to_me())


@actionCardSingleBtn.handle()
async def test_handler(bot: DingBot):
    message = MessageSegment.actionCardSingleBtn(
        title="打造一间咖啡厅",
        text=
        "![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png) \n #### 乔布斯 20 年前想打造的苹果咖啡厅 \n\n Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划",
        singleTitle="阅读全文",
        singleURL="https://www.dingtalk.com/")
    await actionCardSingleBtn.finish(message)


actionCard = on_command("actionCard", to_me())


@actionCard.handle()
async def test_handler(bot: DingBot):
    message = MessageSegment.raw({
        "msgtype": "actionCard",
        "actionCard": {
            "title":
                "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
            "text":
                "![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png) \n\n #### 乔布斯 20 年前想打造的苹果咖啡厅 \n\n Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划",
            "hideAvatar":
                "0",
            "btnOrientation":
                "0",
            "btns": [{
                "title": "内容不错",
                "actionURL": "https://www.dingtalk.com/"
            }, {
                "title": "不感兴趣",
                "actionURL": "https://www.dingtalk.com/"
            }]
        }
    })
    await actionCard.finish(message)


feedCard = on_command("feedCard", to_me())


@feedCard.handle()
async def test_handler(bot: DingBot):
    message = MessageSegment.raw({
        "msgtype": "feedCard",
        "feedCard": {
            "links": [{
                "title":
                    "时代的火车向前开1",
                "messageURL":
                    "https://www.dingtalk.com/",
                "picURL":
                    "https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png"
            }, {
                "title":
                    "时代的火车向前开2",
                "messageURL":
                    "https://www.dingtalk.com/",
                "picURL":
                    "https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png"
            }]
        }
    })
    await feedCard.finish(message)


atme = on_command("atme", to_me())


@atme.handle()
async def test_handler(bot: DingBot, event: MessageEvent):
    message = f"@{event.senderNick} at you" + MessageSegment.atMobiles(
        "13800000001")
    await atme.finish(message)


image = on_command("image", to_me())


@image.handle()
async def test_handler(bot: DingBot, event: MessageEvent):
    message = MessageSegment.image(
        "https://static-aliyun-doc.oss-accelerate.aliyuncs.com/assets/img/zh-CN/0634199951/p158167.png"
    )
    await image.finish(message)


textAdd = on_command("t", to_me())


@textAdd.handle()
async def test_handler(bot: DingBot, event: MessageEvent):
    message = "第一段消息\n" + MessageSegment.text("asdawefaefa\n")
    await textAdd.send(message)

    message = message + MessageSegment.text("第二段消息\n")
    await textAdd.send(message)

    message = message + MessageSegment.text(
        "\n第三段消息\n") + "adfkasfkhsdkfahskdjasdashdkjasdf"
    message = message + MessageSegment.extension({
        "text_type": "code_snippet",
        "code_language": "C#"
    })
    await textAdd.send(message)


code = on_command("code", to_me())


@code.handle()
async def test_handler(bot: DingBot, event: MessageEvent):
    raw = MessageSegment.raw({
        "msgtype": "text",
        "text": {
            "content": 'print("hello world")'
        },
        "extension": {
            "text_type": "code_snippet",
            "code_language": "Python",
        }
    })
    await code.send(raw)
    message = MessageSegment.text("""using System;

namespace HelloWorld
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("Hello World!");
    }
  }
}""")
    message += MessageSegment.extension({
        "text_type": "code_snippet",
        "code_language": "C#"
    })
    await code.finish(message)

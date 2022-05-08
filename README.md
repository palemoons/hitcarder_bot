# hitcarder_bot
浙大nCov健康打卡Bot，打卡部分源码来自[ZJU-nCov-Hitcarder](https://github.com/QSCTech-Sange/ZJU-nCov-Hitcarder)

- 可多人
- 可定时
- 默认每次提交上次所提交的内容
- 添加验证码识别
- 添加基于Mirai的QQ Bot交互

# Usage

打卡功能使用方式与之前相同，暂略。

QQ机器人框架选用Mirai，下载[Mirai-Console-Loader](https://github.com/iTXTech/mirai-console-loader)后，添加[mirai-api-http](https://github.com/project-mirai/mirai-api-http)插件，按照文档启动mcl并添加QQ机器人。

最后修改`config.json.tmpl`文件，更名为`config.json`，`python3 main.py`启动服务。

ps. SDK图方便选用[miraicle](https://github.com/Excaive/miraicle)，由于其局限性(写死host=localhost)，该项目**仅支持本地通信**。

## 手动打卡

如果遇到验证码识别有误/其他网络原因导致今日打卡未成功，可向Bot发送`/打卡`让Bot重新为你打卡。

实现效果如下：

![sample](./sample.png)


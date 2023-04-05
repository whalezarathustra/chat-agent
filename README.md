# 简单的OpenAI chatGPT代理

### 安装
```
使用pip安装最新版本，指定到官方pypi源
pip install chat-agent==0.1.6.3 -i https://pypi.org/simple/
```

### 环境变量配置项：
```
必配：
OPENAI_ORGANIZATION_KEY: openai对应的组织id
OPENAI_API_KEY: openai分配的api key
选配：
OPENAI_CHAT_ROUND: 上下文保留轮次，默认3
OPENAI_CHAT_TOKEN_MAX：单次聊天token最大值，适当设置，默认2048
OPENAI_HISTORY_TOKEN_MAX：历史聊天token最大值，适当设置，默认2048
OPENAI_MODEL：模型名，默认gpt-3.5-turbo
OPENAI_TEMPERATURE：采样温度，默认0.7

CHAT_AGENT_HOST_DEFAULT：监听地址，默认0.0.0.0
CHAT_AGENT_PORT：代理端口，默认8080
CHAT_AGENT_HTTPS_PORT：http端口，默认8443
CHAT_AGENT_WEBSOCKET_PORT：websocket端口，默认9080
CHAT_AGENT_WEBSOCKET_WSS_PORT：websocket wss 端口，默认9443
CACHE_CHAT_LOG_EXPIRE：缓存聊天信息的过期时间，默认3600

CHAT_AGENT_HTTPS：是否开启https，默认True
CHAT_AGENT_SSL_CERT_FILE_FULL_PATH：证书文件完整路径，默认cert.pem
CHAT_AGENT_SSL_KEY_FILE_FULL_PATH：证书key文件完整路径，默认key.pem
CHAT_AGENT_STATIC_PATH：静态文件路径，用于进行指定路径的隐藏文件路由，可用于进行certbot的CA服务验证使用
```

### SSL证书
可参考：https://eff-certbot.readthedocs.io/en/stable/using.html#certbot-commands

### 启动代理
##### http or https 使用以下方式启动
```
python -m chat_agent.app
```
##### websocket or websocket wss 使用以下方式启动
```
python -m chat_agent.websocket_app
```

### 使用
通过在浏览器打开以下链接便可使用
```
http://127.0.0.1:8080
```

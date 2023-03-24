# 简单的OpenAI chatGPT代理

### 安装
```
使用pip安装最新版本，指定到官方pypi源
pip install chat-agent==0.1.3 -i https://pypi.org/simple/
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
CACHE_CHAT_LOG_EXPIRE：缓存聊天信息的过期时间，默认3600

```

### 启动代理
```
python -m chat_agent.app
```

### 使用
通过在浏览器打开以下链接便可使用
```
http://127.0.0.1:8080
```

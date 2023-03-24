import openai
import tiktoken

from chat_agent.cache.cache_helper import get_cache, CHAT_LOG, save_cache
from chat_agent.handler import CHAT_ROUND, CHAT_TOKEN_MAX, HISTORY_TOKEN_MAX, MODEL, TEMPERATURE
from chat_agent.logger.logger_helper import get_logger
from chat_agent.util.context import get_thread_context

logger = get_logger(__name__)


def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo-0301":  # note: future models may deviate from this
        num_tokens = 0
        for message in messages:
            num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":  # if there's a name, the role is omitted
                    num_tokens += -1  # role is always required and always 1 token
        num_tokens += 2  # every reply is primed with <im_start>assistant
        return num_tokens
    else:
        raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
  See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")


def get_valid_chat_log(chat_log: []):
    sid = get_thread_context()['sid']
    valid_context_chat_log = []
    for chat in chat_log:
        if 'user' == chat['role']:
            valid_context_chat_log.append(chat)
        elif 'system' == chat['role']:
            valid_context_chat_log.append(chat)
    temp_messages = valid_context_chat_log[-CHAT_ROUND:]
    while len(temp_messages) > 1:
        token_count = num_tokens_from_messages(temp_messages)
        if token_count > HISTORY_TOKEN_MAX:
            temp_messages = temp_messages[1:]
        else:
            logger.debug('sid: {} current token count: {}'.format(sid, token_count))
            break
    return temp_messages


def send_chat_message_with_steam_response(msg: str, chat_log: [] = None):
    sid = get_thread_context()['sid']
    ip = get_thread_context()['remote_ip']
    logger.debug('receive msg, sid: {} ip: {} msg: {}'.format(sid, ip, msg))
    is_need_cache = False
    if not chat_log:
        chat_log = get_cache(CHAT_LOG, sid=sid)
        is_need_cache = True
    cur_msg = {'role': 'user', 'content': msg}
    chat_log.append(cur_msg)
    messages = get_valid_chat_log(chat_log)
    try:
        completion = openai.ChatCompletion.create(
            model=MODEL,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=CHAT_TOKEN_MAX,
            n=1,
            stop=None,
            frequency_penalty=0,
            presence_penalty=0,
            stream=True
        )
        whole_response_msg = ''
        for chunk in completion:
            if chunk['choices'][0]['finish_reason']:
                break
            if 'role' in chunk['choices'][0]['delta']:
                continue
            chunk_text = chunk['choices'][0]['delta']['content']
            if chunk_text:
                whole_response_msg += chunk_text
                yield chunk_text
            else:
                break
        logger.debug('finish chat, sid: {} whole_response: {}'.format(sid, whole_response_msg))
        chat_log.append({
            'role': 'system', 'content': whole_response_msg
        })
        if is_need_cache:
            save_cache(CHAT_LOG, sid=sid, data=chat_log)
    except Exception as e:
        logger.error('send message has exception, msg: ' + e)

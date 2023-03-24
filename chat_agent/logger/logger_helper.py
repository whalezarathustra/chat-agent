import logging
import os.path
from logging import handlers

from chat_agent.util import file


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='debug', when='D', back_count=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        sh = logging.StreamHandler()
        sh.setFormatter(format_str)
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=back_count,
                                               encoding='utf-8')
        th.setFormatter(format_str)
        self.logger.addHandler(sh)
        self.logger.addHandler(th)


def get_logger(name: str):
    exec_path = file.get_exec_path()
    path = '{}/logs/'.format(exec_path)
    filename = '{}{}.log'.format(path, name)
    if not os.path.exists(path):
        os.makedirs(path)
    return Logger(filename=filename).logger


if __name__ == '__main__':
    logger = get_logger('test')
    logger.debug('debug')
    logger.info('info')
    logger.warning('警告')
    logger.error('报错')
    logger.critical('严重')

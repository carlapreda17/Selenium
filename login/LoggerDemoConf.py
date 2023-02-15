
import logging
import logging.config

class LoggerDemoConf():
    def test_log(self):
        #create logger
        logging.config.fileConfig('logging.conf')
        logger=logging.getLogger(LoggerDemoConf.__name__)

        #loggin messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')

run_test=LoggerDemoConf()
run_test.test_log()
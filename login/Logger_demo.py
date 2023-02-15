import logging

class LoggerDemo():

    def test(self):
        #create logger
        logger=logging.getLogger(LoggerDemo.__name__)
        logger.setLevel(logging.INFO)

        #creare console handlers and set level to info
        chandler=logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        #create formatter
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

        #add formater to console handler->chandler
        chandler.setFormatter(formatter)

        #add console handler to logger
        logger.addHandler(chandler)

        #login messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')

run_tests=LoggerDemo()
run_tests.test()

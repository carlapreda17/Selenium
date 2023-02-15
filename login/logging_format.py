import logging

logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s",datefmt='%m/%d/%y %I:%M:%S %p',level=logging.DEBUG) #cum se afiseaza mesajul,data
logging.warning("waring message")
logging.info("info message")
logging.error("error_message")


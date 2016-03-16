import logging
import os

# log 的加入路径
logging_file = os.path.join('H://BackUps/', 'myTestLog.log')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")

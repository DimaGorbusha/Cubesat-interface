import logging

rec_data_logger = logging.getLogger("RECIEVED")
system_logger = logging.getLogger("SYSTEM")

rec_data_logger.setLevel(logging.INFO)
system_logger.setLevel(logging.INFO)
 
logger_system_fh = logging.FileHandler("backend/logs/system_log.log")

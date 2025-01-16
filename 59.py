# Log messages using logging module
import logging

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("This is an informational message.")
logging.error("This is an error message.")
print("Logged info and error messages to app.log")
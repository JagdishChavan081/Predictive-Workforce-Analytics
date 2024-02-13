from src.Predictive_Workforce_Analytics.logger import logging
from src.Predictive_Workforce_Analytics.exception import CustomException
import sys


if __name__ == "__main__":
    logging.info("The execution has started")

try:
    a = 1 / 0
except Exception as e:
    logging.info("custome Exception")
    raise CustomException(e, sys)

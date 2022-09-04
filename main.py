import sys
from typing import List

from classes.hea_alloy import HEA_Alloy

from services.csv_service import CsvService
from services.logger import logger


def parser( fpath : str, delimiter : str = ','):
    # get data from csv file
    data : List[ str ] = CsvService.get_data_from_csv(fpath, delimiter)

    # write parsed output to csv
    CsvService.write_data_to_csv("Parser.csv", map(lambda row: HEA_Alloy(row), data))

# HELLO
if __name__ == '__main__':
    try:
        fpath = sys.argv[1]
        delimiter= sys.argv[2]
        logger.info(f"entered parameters: \n fpath: {fpath}, \n delimiter: {delimiter}")
        parser(fpath, delimiter)
    except IndexError as e:
        error_message : str = "must call script with arguments: <filepath> <csv-delimiter>"
        message  = {e: error_message}
        raise Exception(message)

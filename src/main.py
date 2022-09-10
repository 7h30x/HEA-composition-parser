import sys
from typing import List

from hea_alloy import HEA_Alloy
from services.csv_service import CsvService
from services.logger import logger


def csv_to_composition_vec ( fpath : str, 
                            delimiter : str = ',',
                            write_csv : bool = True ) -> List[float] :
    # get data from csv file
    data : List[ HEA_Alloy ] = map(lambda row: HEA_Alloy(row), CsvService.get_data_from_csv(fpath, delimiter))
    composition_vectors : List[float] = map(lambda x: x.get_composition_vector() , data)
    # write parsed output to csv
    if write_csv: CsvService.write_data_to_csv("Parser.csv", composition_vectors )
    return list(composition_vectors)


if __name__ == '__main__':
    try:
        fpath = sys.argv[1]
        delimiter= sys.argv[2]
        write_to_csv = sys.argv[3]
        logger.info(f"entered parameters: \n fpath: {fpath}, \n delimiter: {delimiter}")
        csv_to_composition_vec(fpath, delimiter, write_to_csv)
    except IndexError as e:
        error_message : str = "Must call main.py with parameters: [filepath: str] [csv-delimiter: str] [write-to-csv: bool]"
        message  = {e: error_message}
        raise Exception(message)
    except Exception as e: 
        raise e

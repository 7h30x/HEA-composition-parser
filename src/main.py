import sys
from typing import List

from hea_alloy import HEA_Alloy
from services.csv_service import CsvService
from services.logger import logger
from transformer import Transformer

#TODO:update use instructions
#TODO:update docstrings


def csv_to_composition_vec ( fpath : str, 
                            delimiter : str = ',') -> List[float] :
    # get data from csv file
    csv_data  = list(map(lambda row: HEA_Alloy(row), CsvService.get_data_from_csv(fpath, delimiter))) #map is a stateful iterator
    composition_vectors : map[List[float]] = map(lambda x: x.get_composition_vector() , csv_data)
    row_data: map[List[str]] = map(lambda x: x.get_row(), csv_data)
    headers : List[str] = CsvService.get_headers(fpath=fpath)

    # write parsed output to csv
    CsvService.write_data_to_csv("Parser.csv", list(map(list.__add__, composition_vectors, row_data)), Transformer.elements+ headers )

def csv_to_empirical_parameter_input ( fpath : str, 
                            delimiter : str = ','
                             ) -> List[float] :
    # get data from csv file
    csv_data  = list(map(lambda row: HEA_Alloy(row), CsvService.get_data_from_csv(fpath, delimiter))) #map is a stateful iterator
    headers : List[str] = csv_data[0].get_param_headers()

    # write parsed output to csv
    CsvService.write_data_to_csv("Empirical_Params.csv", list( map(lambda x: x.get_params(), csv_data)), headers)


if __name__ == '__main__':
    try:
        fpath = sys.argv[1]
        delimiter= sys.argv[2]
        parser = sys.argv[3]
        calculator = sys.argv[4]
        logger.info(f"entered parameters: \n fpath: {fpath}, \n delimiter: {delimiter}")
        logger.info(f"entered parameters: \n run_parser: {parser}, \n run_params_calculator: {calculator}")
        if parser:
            csv_to_composition_vec(fpath, delimiter)
        if calculator:
            csv_to_empirical_parameter_input(fpath, delimiter)
    except IndexError as e:
        error_message : str = "Must call main.py with parameters: [filepath: str] [csv-delimiter: str] [run_parser: Bool] [run_params_calculator: Bool]"
        message  = {e: error_message}
        raise Exception(message)
    except Exception as e: 
        raise e

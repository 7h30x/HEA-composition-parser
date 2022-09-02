import os
from typing import List
import _csv
from classes.hea_alloy import HEA_Alloy
from services.logger import logger

class CsvService:
    @staticmethod
    def get_data_from_csv(fpath: str, delimiter = ',') -> List[ str ]:
        '''   
        Retrieves alloy composition data from a .csv file given as input.

        Parameters:
            fpath: absolute path to the file
            delimiter

        Returns:
            List with elements as each row in the .csv
        '''

        if not os.path.exists(fpath):
            raise OSError(filename=fpath)
        # logger.info(f"Opening {fpath}")
        # Using utf-8-sig to read a file will treat BOM as file info instead of a string.
        with open(fpath, newline='', encoding='utf-8-sig') as csvfile:
            reader = _csv.reader(csvfile, delimiter = delimiter, quotechar='"')
            data = [row[0] for row in reader if len(row) > 0]
        logger.info(f"Loaded {fpath} containing {len(data)} items")
        logger.info(f"first 10 items: {data[0::20]}")
        return data
    
    #TODO : create this function
    @staticmethod
    def write_data_to_csv(fpath: str,  data : List [HEA_Alloy], delimiter=',') -> None:
        '''
        Writes alloy composition data to a given file.

        Parameters:
            fpath: relative / absolute path to the output file
            data: list of element vectors with molar ratios of each element [0, 0.8, 0, 0, 0.2, ...]

        Returns:
            None
        '''
        
        with open(fpath, 'w', newline='\n') as outfile:
            writer = _csv.writer(outfile, delimiter = delimiter)
            writer.writerows( map(lambda x: x.get_composition_vector() , data))



    
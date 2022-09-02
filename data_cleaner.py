import re
import logging as logger
import HEA_Alloy
class DataCleaner:
   
    @staticmethod
    def normalize_molar_ratios  ( ratios : "list[float]") -> "list[float]" :
        """ 
        Normalizes a list of molar ratio values to sum up to 1.

        Parameters: 
            List [float]: A list of molar ratios.
                e.g. [1, 0.5, 0.5, 1, 1]

        Returns: 
            List [float]: A normalized version of the list.
                e.g. [0.25 , 0.125, 0.125, 0.25, 0.25]
        """
        total_moles = sum(ratios)
        return map( lambda ratio : ratio / total_moles , ratios )
        
    @staticmethod
    def composition_to_molar_elements (row: str) -> "dict[str:float]" :
        row = DataCleaner.clean_row(row)
        ret = {}
        pattern="([A-Z][a-z]?[0-9.]*)"
        # split into elements and their molar 
        # e.g. [Ag, Au2, Cr0.5]
        raw_elements_list = re.findall(pattern, row)
        for e in raw_elements_list:
            # split string into element and molar ratio tokens 
            element, mole = e.findall('\\d+\.?\\d*|\\D+', maxsplit=1)
            # check tokens in element whitelist
            if element not in HEA_Alloy.elements:
                raise Exception(f"The element {element} in the composition {e} was not found in whitelist.")
            ret[element] =  float(mole[0]) if mole else 1
        return ret

    @staticmethod
    def clean_row (row : str) :
        remove_chars = ['+','-',' ']
        row = row.strip()
        # remove +/- signs and spaces
        return ''.join([row[i] for i in range(len(row)) if i not in remove_chars])     
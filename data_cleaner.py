import re
import logging as logger
class DataCleaner:
    # list of all possible elements in a HEA composition formula.
    elements = ['Ag', 'Al', 'Au', 'B', 'Be', 'Bi', 'C', 'Cd', 'Ce', 'Co', 'Cr', \
    'Cu', 'Dy', 'Er', 'Fe', 'Gd', 'Ge', 'Hf', 'Ho', 'In', 'Ir', 'La', 'Li', \
    'Lu', 'Mg', 'Mn', 'Mo', 'N', 'Nb', 'Nd', 'Ni', 'Os', 'Pb', 'Pd', \
    'Pr', 'Pt', 'Re', 'Rh', 'Ru', 'Sb', 'Sc', 'Si', 'Sm', 'Sn', 'Sr', \
    'Ta', 'Tb', 'Ti', 'Tm', 'V', 'W', 'Y', 'Yb', 'Zn', 'Zr', 'Ga','S']
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
        print(f'ratios is {ratios}')
        total_moles = sum(ratios)
        return list(map( lambda ratio : ratio / total_moles , ratios ))
        
    @staticmethod
    def composition_to_molar_elements (row: str) -> "dict[str:float]" :
        """ 
       Takes a composition str e.g. "Cu0.5Zn0.5" and returns a dictionary of 
       elements and their molar ratio .  

        Parameters: 
            A string e.g. "Cu0.5Zn0.5"

        Returns: 
            Dict [str: float] 
            e.g.
            {
                Cu : 0.5
                Zn : 0.5
            }
        """
        row = DataCleaner._clean_row(row)
        ret = {}
        pattern="([A-Z][a-z]?[0-9.]*)"
        # split into elements and their molar 
        # e.g. [Ag, Au2, Cr0.5]
        raw_elements_list = re.findall(pattern, string=row)
        for e in raw_elements_list:
            # split string into element and molar ratio tokens 
            print(e)
            
            tokens = re.findall('\\d+\.?\\d*|\\D+', string=e)
            element = tokens[0]
            if len(tokens) == 2:
                mole = tokens[1][0] 
            else: mole = 1
            # check tokens in element whitelist
            if element not in DataCleaner.elements:
                raise Exception(f"The element {element} in the composition {e} was not found in whitelist.")
            ret[element] =  float(mole) 
        return ret

    @staticmethod
    def _clean_row (row : str) :
        """ 
        Takes a composition string and returns a cleaned version.
        Removes all whitespaces and +/-/_ signs

        """
        remove_chars = ['+','-',' ','_']
        row = row.strip()
        # remove +/- signs and spaces
        return ''.join([row[i] for i in range(len(row)) if i not in remove_chars])     
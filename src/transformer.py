import re
from services.logger import logger

class Transformer:
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
        logger.debug(f'Molar ratios is {ratios}')
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
        row = Transformer._clean_row(row)
        logger.debug(f"Row string is {row}")
        ret = {}
        
        # replace paranthesized elements with explicit formula 
        parenthesis_pattern="(\(((?:[A-Z]{1}[a-z]{0,1})+)\)(\d*\.?\d+))"
        praw = re.findall(parenthesis_pattern, string=row)
        #print(praw)
        for p in praw: #ex. ["(AlCo)2","(NbCr)0.3]"
            elements_p=re.findall('[A-Z][a-z]?',p[0])
            #print(elements_p)
            n = 1 / len(elements_p)
            if len(p)==3:
                n :float = float(p[2]) / len(elements_p)
           # print(f"n is {n}")
            replacement_string = str(n).join(elements_p) + str(n)
            row = row.replace(p[0],replacement_string, 1)
            
        # split into elements and their molar 
        # e.g. [Ag, Au2, Cr0.5]
        pattern="([A-Z][a-z]?[0-9.]*)"
        raw= re.findall(pattern, string=row)
        for r in raw:
            # split string into element and molar ratio tokens 
            molar_tokens = re.findall('\\d+\.?\\d*|\\D+', string=r)
            logger.debug(f'Row tokens are {molar_tokens}')
            element = molar_tokens[0]
            if len(molar_tokens) == 2:
                mole = molar_tokens[1] 
            else: mole = 1
            # check element whitelist
            if element not in Transformer.elements:
                raise Exception(f"The element {element} in the composition {e} was not found in whitelist.")
            ret[element] =  float(mole) 
        return ret

    @staticmethod
    def _clean_row (row : str) :
        """ 
        Takes a composition string and returns a cleaned version.
        Removes all whitespaces and +/-/_ signs

        """
        remove_chars = ['+','-',' ','_','?']
        row = row.strip()
        # remove +/- signs and spaces
        return ''.join([row[i] for i in range(len(row)) if row[i] not in remove_chars])     
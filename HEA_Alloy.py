from data_cleaner import DataCleaner


class HEA_Alloy:

    # list of all possible elements in a HEA composition formula.
    elements = ['Ag', 'Al', 'Au', 'B', 'Be', 'Bi', 'C', 'Cd', 'Ce', 'Co', 'Cr', \
    'Cu', 'Dy', 'Er', 'Fe', 'Gd', 'Ge', 'Hf', 'Ho', 'In', 'Ir', 'La', 'Li', \
    'Lu', 'Mg', 'Mn', 'Mo', 'N', 'Nb', 'Nd', 'Ni', 'Os', 'Pb', 'Pd', \
    'Pr', 'Pt', 'Re', 'Rh', 'Ru', 'Sb', 'Sc', 'Si', 'Sm', 'Sn', 'Sr', \
    'Ta', 'Tb', 'Ti', 'Tm', 'V', 'W', 'Y', 'Yb', 'Zn', 'Zr']

    
    def __init__ (self, row : str) -> None :
        
        self._composition: list[ float ] = [0] * len(HEA_Alloy.elements)
        self._elements_dict : dict[str: float] = DataCleaner.composition_to_molar_elements(row) 
        self._composition_str : str = row
        # fill in composition with molars from row data
        elements = self._elements_dict.keys
        molars = DataCleaner.normalize_molar_ratios(self._elements_dict.values)
        for j, el in elements:
            el_idx = HEA_Alloy.elements.index(el)
            if el_idx == -1 :
                raise Exception(f"The element {el} was not found in the whitelist {HEA_Alloy.elements}.") 
            self.composition[el_idx] = molars[j]

    def __str__(self):
        return self._composition_str

    def get_molar_elements  (self) -> "dict[str: float]":
        return self._elements_dict

    def get_composition_vector (self) -> "list[float]":
        return self._composition
    
  

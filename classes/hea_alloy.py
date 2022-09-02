from data_cleaner import DataCleaner


class HEA_Alloy:
    
   
    def __init__ (self, row : str) -> None :
        
        self._composition: list[ float ] = [0] * len(DataCleaner.elements)
        self._elements_dict : dict[str: float] = DataCleaner.composition_to_molar_elements(row) 
        self._composition_str : str = row

        # fill in composition with molars from row data
        elements = list(self._elements_dict.keys())
        print(f'elements is {elements}')
        molars   = DataCleaner.normalize_molar_ratios(list(self._elements_dict.values()))
        for j, el in enumerate(elements):
            el_idx = DataCleaner.elements.index(el)
            if el_idx == -1 :
                raise Exception(f"The element {el} was not found in the whitelist {DataCleaner.elements}.") 
            self._composition[el_idx] = molars[j]

    def __str__(self):
        return self._composition_str

    def get_molar_elements  (self) -> "dict[str: float]":
        return self._elements_dict

    def get_composition_vector (self) -> "list[float]":
        return self._composition
    
  

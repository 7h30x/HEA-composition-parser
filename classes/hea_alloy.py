from classes.transformer import Transformer
from services.logger import logger


class HEA_Alloy:
    
    def __init__ (self, row : str) -> None :
        
        self._composition: list[ float ]        = [0] * len(Transformer.elements)
        self._elements_dict : dict[str: float]  = Transformer.composition_to_molar_elements(row) 
        self._composition_str : str             = row

        # fill in composition with molars from row data
        elements = list(self._elements_dict.keys())
        logger.debug(f'Created a HEA_Alloy with elements: {elements}')
        molars   = Transformer.normalize_molar_ratios(list(self._elements_dict.values()))
        for j, el in enumerate(elements):
            el_idx = Transformer.elements.index(el)
            if el_idx == -1 :
                raise Exception(f"The element {el} was not found in the whitelist {Transformer.elements}.") 
            self._composition[el_idx] = molars[j]

    def __str__(self):
        return self._composition_str

    def get_molar_elements  (self) -> "dict[str: float]":
        return self._elements_dict

    def get_composition_vector (self) -> "list[float]":
        return self._composition
    
  

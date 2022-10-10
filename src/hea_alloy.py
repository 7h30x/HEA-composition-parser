from typing import List
from transformer import Transformer
from services.logger import logger
from empirical_params import EmpiricalParams
from pymatgen.core.periodic_table import Element

class HEA_Alloy:
    
    def __init__ (self, row : str) -> None :
        self._composition_str : str             = row[0]
        self._row : str = row
        self._composition: list[ float ]        = [0] * len(Transformer.elements)
        self._elements_molars : dict[str: float]  = Transformer.composition_to_molar_elements(self._composition_str) 
        
        #elements_list = list(map(lambda x : x.strip(), list(self._elements_molars.keys())))
        elements_list = list(map(lambda x : Element(x.strip()), list(self._elements_molars.keys())))
        mol_ratio   = Transformer.normalize_molar_ratios(list(self._elements_molars.values()))
        
        self._params: EmpiricalParams = EmpiricalParams(element_list=elements_list, mol_ratio=mol_ratio)
        
        logger.info(elements_list)
        logger.debug(f'Created a HEA_Alloy with elements: {elements_list}')
        
        # fill in composition attribute with row data
        for j, el in enumerate(elements_list):
            whitelist_idx = Transformer.elements.index(el.symbol)
            if whitelist_idx == -1 :
                raise Exception(f"The element {el} was not found in the whitelist {Transformer.elements}.") 
            self._composition[whitelist_idx] = mol_ratio[j]

    def __str__(self):
        return self._composition_str

    def get_molar_elements  (self) -> "dict[str: float]":
        return self._elements_molars

    def get_composition_vector (self) -> List[float]:
        return self._composition
    def get_row (self) -> List[str]:
        return self._row
    def get_param_headers(self) -> List[str]:
        return self._params.params_list
    def get_params(self) -> List[float]:
        alloy = self._params
        return [ alloy.mix_enthalpy, alloy.std_enthalpy, 100 * alloy.delta, alloy.omega,
                         alloy.mix_entropy, 100 * alloy.Tm, alloy.std_Tm, alloy.x, 100 * alloy.std_x, alloy.vec,
                         alloy.vec_std, alloy.density, alloy.price]
    
    
  

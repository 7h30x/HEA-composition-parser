import math
from transformer import * 
from services.logger import logger
def test_normalize_molar_ratios ():
    r1 =  Transformer.normalize_molar_ratios([1.0, 0.5, 0.3, 0.2,  0, 0, 1.0])
    nr1 = [1/3, 1/6, 1/10,1/15, 0,0, 1/3 ]

    for (x,y) in zip(r1 , nr1):
        assert math.isclose(x,y)
    assert sum(r1) == 1 
    assert len(r1) == len(nr1)


compositions = ['Nb20Ni20Ti+20+Co_20-Zr20', 'Nb1.50Ni10Ti', '(FeCrNiCo)Al0.75Cu0.25 ']
compositional_elements = [{ #1
    "Nb": 20.0, 
    "Ni":20,
    "Ti":20,
    "Co":20,
    "Zr":20 
    }, 
    { #2
    "Nb": 1.50, 
    "Ni":10.0,
    "Ti":1.0,
    },
    { #3
        "Fe": 1.0,
        "Cr": 1.0,
        "Ni":1.0,
        "Co" : 1.0,
        "Al" : 0.75,
        "Cu" : 0.25
    }
]
composition_test_zip = zip(compositions, compositional_elements)

def test_composition_to_molar_elements ():
    for res in composition_test_zip:
        e, ans = res
        assert Transformer.composition_to_molar_elements(e) == ans 


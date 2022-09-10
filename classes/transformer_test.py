from transformer import * 
def normalize_molar_ratios_test ():
    r1 = [1, 0.5, 0.3, 0.2,  0, 0, 1]
    nr1 = [1/3, 1/6, 1/10,1/15, 0,0,1/3]
    assert Transformer.normalize_molar_ratios(r1) == nr1
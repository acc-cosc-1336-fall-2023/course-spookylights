import unittest

from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement

dna1 = "GAGCCTACTAACGGGAT"
dna2 = "CATCGTAATGACGGCCT"
dna =  "AAAACCCGGT"

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        self.assertEqual(7, get_hamming_distance(dna1, dna2))
    
    def test_get_dna_complement(self):
        self.assertEqual("ACCGGGTTTT", get_dna_complement(dna))
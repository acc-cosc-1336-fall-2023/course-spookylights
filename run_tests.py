import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.homework.b_in_proc_out import tests_in_proc_out
#from tests.examples.c_decisions import tests_decisions
#from tests.homework.c_decisions import tests_decisions
#from tests.examples.d_repetition import tests_repetition
#from tests.homework.d_repetition import tests_repetition
#from tests.examples.e_functions import tests_functions
from tests.homework.e_functions import tests_functions

suite = unittest.TestLoader().loadTestsFromModule(tests_functions)
unittest.TextTestRunner(verbosity=2).run(suite)

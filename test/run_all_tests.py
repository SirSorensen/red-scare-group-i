import unittest
import pathlib

class CustomTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        # Assuming the test case has an attribute `expected` and `actual`
        if hasattr(test, 'expected') and hasattr(test, 'actual'):
            self._write_status(test, "Success")
        else:
            super().addSuccess(test) # might want to do this line manualy
            
    def _write_status(self, test, status):
        if hasattr(test, 'solutionType'):
            self.stream.writeln(f"{test.solutionType}  {test.file}\tExpected: {test.expected}, Actual: {test.actual}\t{status}")

    def addError(self, test, err):
        self._write_status(test, "Error")
        
    def addFailure(self, test, err):
        self._write_status(test, "Fail")
    
    def startTest(self, test):
        super(unittest.TextTestResult, self).startTest(test)
        if self.showAll:
            self.stream.flush()
            self._newline = False

# Discover all test cases in the current directory
test_folder = pathlib.Path(__file__).resolve().parent
test_loader = unittest.TestLoader()
test_suite = test_loader.discover(start_dir=test_folder, pattern='*_tests.py')

# Run the test suite and redirect the output to a file
with open('test_results.txt', 'w') as f:
    test_runner = unittest.TextTestRunner(stream=f, verbosity=2, resultclass=CustomTestResult)
    test_runner.run(test_suite)
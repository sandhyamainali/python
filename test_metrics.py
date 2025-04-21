import pytest 
import sys
sys.argv = ['']  # Clear any arguments
pytest.main(['test_metrics.py', '--maxfail=1', '--disable-warnings', '-q'])

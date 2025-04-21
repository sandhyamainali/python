import pytest
import sys
sys.argv = ['']
pytest.main(['test_metrics.py', '--maxfail=1', '--disable-warnings', '-q'])

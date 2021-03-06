import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import logging
import Colorer
logging.basicConfig(level=logging.DEBUG,format='%(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

import ast_parse
import z3
from pyPath import Path
from pyPathGroup import PathGroup
import pytest
from pyObjectManager.Int import Int
from pyObjectManager.Real import Real
from pyObjectManager.BitVec import BitVec
from pyObjectManager.List import List
from pyState.z3Helpers import Z3_MAX_STRING_LENGTH

test1 = """
s = pyState.Real()
s2 = pyState.Real(123)
s3 = pyState.Real(123.5)
"""


def test_function_pyState_Real():
    b = ast_parse.parse(test1).body
    p = Path(b,source=test1)
    pg = PathGroup(p)

    pg.explore()
    assert len(pg.completed) == 1
    
    s = pg.completed[0].state.getVar('s')
    s2 = pg.completed[0].state.getVar('s2')
    s3 = pg.completed[0].state.getVar('s3')

    assert type(s) == Real
    assert type(s2) == Real
    assert type(s3) == Real

    assert s.canBe(123.0)
    assert s2.getValue() == 123.0
    assert s3.getValue() == 123.5

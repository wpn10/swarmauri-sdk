import pytest
from swarmauri.standard.chains.concrete.ChainStep import ChainStep
from swarmauri.standard.tools.concrete.AdditionTool import AdditionTool

@pytest.mark.unit
def test_ubc_resource():
    tool = AdditionTool()
    step = ChainStep(key='test', method=tool, args=(1,2), kwargs={}, ref=None)
    assert step.resource == 'ChainStep'

@pytest.mark.unit
def test_method_args_only_call():
    tool = AdditionTool()
    args = (1,2)
    kwargs = {}
    step = ChainStep(key='test', method=tool, args=args, kwargs=kwargs, ref=None)
    result = step.method(*step.args, **step.kwargs)
    assert result[0] == args


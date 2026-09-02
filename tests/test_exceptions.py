"""异常体系测试。"""
import pytest

from contextloom.exceptions import (ConfigurationError, ContextLoomError,
                                    LLMBackendError)


def test_base_exception():
    e = ContextLoomError("boom")
    assert e.code == "contextloom_error"
    assert str(e) == "boom"


def test_specific_exception_code():
    assert ConfigurationError("x").code == "configuration_error"
    assert LLMBackendError("x").code == "llm_backend_error"


def test_catchable():
    with pytest.raises(ContextLoomError):
        raise ConfigurationError("bad")

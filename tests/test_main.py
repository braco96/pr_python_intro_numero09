import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


@pytest.mark.parametrize("s,esperado", [
    ("10", 10),
    ("x", None),
    (None, None),
])
def test_safe_int(s, esperado):
    assert mod.safe_int(s, default=None) == esperado

import pytest
def test_prediction_requires_tensorflow():
    pytest.importorskip("tensorflow")

import pytest

from ..validates import validate_date


class TestValidate(object):

    def test_should_validate_correct_date(self):
        validate_date('02-06-2017 10:00')

    def test_should_except_when_date_is_incorrect_format(self):
        with pytest.raises(ValueError):
            validate_date('2017-03-02')

    def test_should_except_when_date_is_not_string(self):
        with pytest.raises(ValueError):
            validate_date(2017)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import unittest
from betbright.lottery.validates import validate_date


class TestValidate(unittest.TestCase):

    def test_should_validate_correct_date(self):
        date = validate_date('02-06-2017 10:00')
        self.assertEqual(date, datetime.datetime(2017, 6, 2, 10, 0))

    def test_should_except_when_date_is_incorrect_format(self):
        with self.assertRaises(ValueError):
            validate_date('2017-03-02')

    def test_should_except_when_date_is_not_string(self):
        with self.assertRaises(ValueError):
            validate_date(2017)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from betbright.lottery.lottery_draw import calculate_next_draw_date


class TestLotteryDraw(unittest.TestCase):

    def test_should_return_calculate_valid_next_date(self):
        next_date = calculate_next_draw_date('03-06-2017 13:40')
        self.assertEqual(next_date, '07-06-2017 Wednesday 08:00')

    def test_should_return_date_when_date_is_in_the_same_day(self):
        next_date = calculate_next_draw_date('03-06-2017 08:00')
        self.assertEqual(next_date, '03-06-2017 Saturday 08:00')

        next_date = calculate_next_draw_date('07-06-2017 08:00')
        self.assertEqual(next_date, '07-06-2017 Wednesday 08:00')

    def test_should_return_calculate_when_no_date_informed(
        self
    ):
        next_date = calculate_next_draw_date()
        self.assertIsInstance(next_date, str)

    def test_should_return_except_when_date_format_is_wrong(
        self
    ):
        with self.assertRaises(ValueError):
            calculate_next_draw_date('ewqeqweqew')

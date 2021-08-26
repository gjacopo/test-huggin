#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script for sentiment analysis in KNIME
"""

from test_huggin.nodes import KSentiment

sentiment = KSentiment()
output_table_1 = sentiment(input_table_1)

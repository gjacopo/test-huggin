#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script for summarization in KNIME
"""

from test_huggin.nodes import KSummary

summary = KSummary()
output_table_1 = summary(input_table_1)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script for entity recognition in KNIME
"""

from test_huggin.nodes import KNER

ner = KNER()
output_table_1 = ner(input_table_1)

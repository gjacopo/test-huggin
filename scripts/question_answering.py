#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script for question_answering in KNIME
"""

from test_huggin.nodes import KQA

qa = KQA()
output_table_1 = qa(input_table_1)

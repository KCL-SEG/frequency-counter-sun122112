"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter


def frequencies(items):
    # Your code goes here
    itemsToString = map(str, items)
    return dict(Counter(itemsToString))





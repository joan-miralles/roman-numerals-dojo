#!/usr/bin/env python

class RomanNumerals:
    def convert_from_integer(self, integer):
        if integer >= 10:
            return "X"
        elif integer >= 5:
            return "V"
        else:
            return "I" * integer




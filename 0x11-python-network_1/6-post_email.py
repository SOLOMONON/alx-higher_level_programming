#!/usr/bin/python3

"""
This module sends a POST request to a given URL with an email
as a parameter,and displays the body of the response.
"""

import requests
import sys


def main():
    # Check that the script is called with two arguments
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <URL> <email>")
        return

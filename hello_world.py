#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:02:43 2024

@author: chris
"""

import os
import sys
#from typing import List

#from actions import io


def main(): #args: List[str]) -> None:
    """main function

    Args:
        args: STDIN arguments
    """

    # reading the name variable from `with`
    name = os.environ.get("INPUT_NAME")

    print('Hello World ' + name)
    


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:02:43 2024

@author: chris
"""

import os
import sys
from typing import List

#from actions import io


def main(args: List[str]) -> None:
    """main function

    Args:
        args: STDIN arguments
    """

    # reading the name variable from `with`
    #name = os.environ["INPUT_NAME"]

    # writing to the buffer
    #io.write_to_output({"phrase": f"Hello {name}"})
    print('Hello World ') # + name)
    # now, people can echo `phrase`


if __name__ == "__main__":
    main(sys.argv)
#!/usr/bin/env python3

import atheris
import sys
import os

with atheris.instrument_imports():
    from dataclasses import dataclass
    from io import BytesIO
    
@dataclass
class SearchRequest():
    query = ""
    page_number = 0
    result_per_page = 0

def TestOneInput(input):
    fdp = atheris.FuzzedDataProvider(input)
    try:
        SearchRequest.read_from(BytesIO(fdp.ConsumeBytes(fdp.ConsumeIntInRange(1, 4096))))
    except Exception:
        return

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()

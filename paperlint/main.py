#!/usr/bin/python
import sys
import traceback

from paperlint.linter import main

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        print(traceback.format_exc())
        raise SystemExit from BaseException

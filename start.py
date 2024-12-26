import runpy
import sys

if __name__ == "__main__":
    module_name = 'bot'
    runpy.run_module(module_name, run_name="__main__")
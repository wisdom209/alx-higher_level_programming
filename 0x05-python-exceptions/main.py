#!/usr/bin/python3 -u
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]
l = [b'Word 1', b'Word 2', 3.0]
lib.print_python_list(l)
del l[1]
lib.print_python_list(l)

#!/usr/bin/python3
import ctypes
lib = ctypes.CDLL("./libPython.so")
# let us give the parameters
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]


s = b"Holberton"
lib.print_python_bytes(s)

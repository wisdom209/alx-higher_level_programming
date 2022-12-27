#!/usr/bin/python3
import ctypes
lib = ctypes.CDLL("./libPython.so")
# let us give the parameters
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]


s = b"HBTN"
lib.print_python_bytes(s)
b = b'C is fun'
lib.print_python_bytes(b)
b = b'b in front'
lib.print_python_bytes(b)

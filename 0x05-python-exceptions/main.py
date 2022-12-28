#!/usr/bin/python3 -u
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]
f=1.41592653588893238462643383279502884197169399375105820974944592
lib.print_python_float(f)

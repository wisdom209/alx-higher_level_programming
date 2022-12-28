#!/usr/bin/python3 -u
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]
l = [b'Holberton', b'School']
lib.print_python_list(l)
del l[1]
lib.print_python_list(l)
l = l + [1, 2, 3.4, (1, '8'), [0, -1, 2048], b"H", "Python"]
lib.print_python_list(l)

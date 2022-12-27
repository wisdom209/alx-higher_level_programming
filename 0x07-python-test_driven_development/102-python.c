#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Python.h>

void print_python_string(PyObject *p)
{
	// Check if p is NULL
	if (p == NULL)
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
	}
	else if (PyUnicode_Check(p))
	{

		if (PyUnicode_IS_ASCII(p))
		{
			const char *a = PyUnicode_AsUTF8(p);
			printf("[.] string object info\n");
			printf("  type: compact ascii\n");
			printf("  length: %ld\n", strlen(a));
			printf("  value: %s\n", a);
		}
		else
		{
			const char *a = PyUnicode_AsUTF8(p);
			printf("[.] string object info\n");
			printf("  type: compact unicode object\n");
			printf("  length: %ld\n", PyUnicode_GetLength(p));
			printf("  value: %s\n", a);
		}
	}
	else
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
	}
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - prints python string in shared lib
 * @p: Pyobject
 *
 * Return: void
 */
void print_python_string(PyObject *p)
{
	if (p == NULL || !PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
	}
	else
	{

		const char *type, *value;
		int len;

		if (PyUnicode_IS_ASCII(p))
		{
			type = "compact ascii";
			value = PyUnicode_AsUTF8(p);
			len = strlen(value);
		}
		else
		{
			type = "compact unicode object";
			value = PyUnicode_AsUTF8(p);
			len = PyUnicode_GetLength(p);
		}
		printf("[.] string object info\n");
		printf("  type: %s\n", type);
		printf("  length: %d\n", len);
		printf("  value: %s\n", value);
	}
}

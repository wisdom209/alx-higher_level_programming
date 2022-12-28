
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

/**
 * print_python_bytes - print bytes
 * @p: PyObject
 *
 * Return:void
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytesObject *bytes = (PyBytesObject *)p;
	size_t byte_size = ((PyVarObject *)bytes)->ob_size;
	char *str = bytes->ob_sval;
	size_t strlength = strlen(str);
	char print_str[100];
	size_t whole_len = byte_size < 10 ? byte_size + 1 : 10;

	fflush(stdout);
	for (size_t i = 0; i < strlength; i++)
		print_str[i] = isprint(str[i]) ? str[i] : '?';

	print_str[strlength] = '\0';

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", byte_size);
	printf("  trying string: %s\n", print_str);
	printf("  first %ld bytes: ", whole_len);

	for (size_t i = 0; i <= byte_size && i < 10; i++)
	{
		if (i < 10)
		{
			if (i == 9 || i == byte_size)
				printf("%02hhx", str[i]);
			else
				printf("%02hhx ", str[i]);
		}
		else
			printf("00");
	}
	printf("\n");
}

/**
 * print_python_float - print floats
 * @p: PyObject
 *
 * Return:void
 */
void print_python_float(PyObject *p)
{
	if (PyFloat_Check(p))
	{
		PyFloatObject *item = (PyFloatObject *)p;
		float f = item->ob_fval;

		printf("[.] float object info\n");

		if (ceil(f) == floor(f))
			printf("  value: %.1f\n", f);
		else
			printf("  value: %.16g\n", f);
	}
	else
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
	}
}

/**
 * print_python_list - print lists
 * @p: PyObject
 *
 * Return:void
 */
void print_python_list(PyObject *p)
{
	fflush(stdout);
	if (PyList_Check(p))
	{
		PyListObject *list = (PyListObject *)p;
		size_t allocated_space = list->allocated, i = 0;
		size_t list_size = list->ob_base.ob_size;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", list_size);
		printf("[*] Allocated = %ld\n", allocated_space);

		for (i = 0; i < list_size; i++)
		{

			const char *type = list->ob_item[i]->ob_type->tp_name;

			if (strcmp(type, "float") == 0)
			{
				printf("Element %ld: %s\n", i, type);
				print_python_float((PyObject *)list->ob_item[i]);
			}
			else if (strcmp(type, "bytes") == 0)
			{
				printf("Element %ld: %s\n", i, type);
				print_python_bytes((PyObject *)list->ob_item[i]);
			}
			else
			{
				printf("Element %ld: %s\n", i, type);
			}
		}
	}
	else
	{
		printf("[*] Python list info\n");
		printf("  [ERROR] Invalid List Object\n");
	}
}

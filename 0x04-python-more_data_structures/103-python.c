#include <Python.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

/**
 * print_python_bytes - print a python byte object
 * @p: PyObject
 *
 * Return: void
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
	char *str = bytes->ob_sval, print_str[100];
	size_t strlength = strlen(str);
	size_t whole_len = byte_size < 10 ? byte_size + 1 : 10;

	fflush(stdout);

	for (size_t i = 0; i < strlength; i++)
	{
		if (isprint(str[i]))
			print_str[i] = str[i];
		else
		{
			print_str[i + 1] = '\0';
			break;
		}
	}
	print_str[strlength] = '\0';
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", byte_size);
	printf("  trying string: %s\n", print_str);
	printf("  first %ld bytes: ", whole_len);
	for (size_t i = 0; i <= byte_size && i < 10; i++)
	{
		if (i < 10)
			printf("%02hhx ", str[i]);
		else
			printf("00");
	}
	printf("\n");
}

/**
 * print_python_list - print a python list object
 * @p: PyObject
 *
 * Return: void
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
		printf("[*] Size of Python List = %ld\n", list_size);
		printf("[*] Allocated = %ld\n", allocated_space);

		for (i = 0; i < list_size; i++)
		{

			const char *type = list->ob_item[i]->ob_type->tp_name;

			if (strcmp(type, "bytes") == 0)
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

#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *obj;

    size = Py_SIZE(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        printf("Element %ld: ", i);
        obj = PyList_GetItem(p, i);
        printf("%s\n", obj->ob_type->tp_name);
    }
}

#define PY_SSIZE_T_CLEAN
#include <Python.h>

typedef double my_kind_of_function(double, double);



static PyObject *
tosti_run(PyObject *self, PyObject *args)
{
    size_t addr;
    my_kind_of_function* f;
    double x;

    if (!PyArg_ParseTuple(args, "n", &addr)) {
        return NULL;
    }

    printf("Got address %zu\n", addr);
    f = (my_kind_of_function*)addr;

    x = f(2.0, 10.345);

    return PyFloat_FromDouble(x);
}



static PyMethodDef TostiMethods[] = {
    {"run", tosti_run, METH_VARARGS, "Run a runny thing."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};


static struct PyModuleDef tostimodule = {
    PyModuleDef_HEAD_INIT,
    "tosti",   /* name of module */
    "This module is a toasti", /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    TostiMethods
};


PyMODINIT_FUNC
PyInit_tosti(void)
{
    return PyModule_Create(&tostimodule);
}

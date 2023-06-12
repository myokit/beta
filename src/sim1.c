#define PY_SSIZE_T_CLEAN
#include <Python.h>

typedef double my_kind_of_function(double, double);



static PyObject *
sim1_run(PyObject *self, PyObject *args)
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



static PyMethodDef Sim1Methods[] = {
    {"run", sim1_run, METH_VARARGS, "Run a runny thing."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};


static struct PyModuleDef sim1_module = {
    PyModuleDef_HEAD_INIT,
    "sim1",   /* name of module */
    "Performs a sumulation", /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    Sim1Methods
};


PyMODINIT_FUNC
PyInit_sim1(void)
{
    return PyModule_Create(&sim1_module);
}

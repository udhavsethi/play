#define PY_SSIZE_T_CLEAN
#include <Python.h>

int
main(int argc, char *argv[])
{
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }
    Py_SetProgramName(program);  /* optional but recommended */ // inform the interpreter about paths to Python run-time libraries
    Py_Initialize();	// initialize the Python interpreter
    PyRun_SimpleString("from time import time,ctime\n"
                       "print('Today is', ctime(time()))\n");	// call the interpreter by passing a string containing Python statements
    								// Alternatively, getting the Python code from a file can be done using PyRun_SimpleFile()
    if (Py_FinalizeEx() < 0) {	// Py_FinalizeEx shuts the interpreter down
        exit(120);
    }
    PyMem_RawFree(program);
    return 0;
}

// pytest.c

// Assuming you built Python from source and installed in the `~/py` directory.
// Reference: https://www.devdungeon.com/content/how-build-python-source

// Compile with:
// gcc pytest.c -I ~/py/include/python3.9 -L ~/py/lib -lpython3.9 -lpthread -ldl -lm -lutil

// Run with:
// PYTHONHOME=~/py ./a.out

// C code adapted from https://docs.python.org/3.9/extending/embedding.html
#define PY_SSIZE_T_CLEAN
#include <Python.h>

int main(int argc, char *argv[])
{
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }
    Py_SetProgramName(program);  /* optional but recommended */
    Py_Initialize();
    PyRun_SimpleString("import sys\n"
                       "print(sys.path)\n");
    if (Py_FinalizeEx() < 0) {
        exit(120);
    }
    PyMem_RawFree(program);
    return 0;
}

#include <Python.h>

static PyObject * jay_hello(PyObject *self, PyObject *args) {
	const char *person;
	int sts;
	if (!PyArg_ParseTuple(args, "s", &person))
		return NULL;
	printf("Hello, %s. I'm Jay.\n", person );
	return Py_None;
/*
	sts = printf("Hello, %s. I'm Jay.\n", person );
	return Py_BuildValue("i", sts);
*/
}

static PyMethodDef JayMethods[] = {
	{"hello",  jay_hello, METH_VARARGS,
	"Say hello to a person from Jay."},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initjay(void) {
	PyImport_AddModule("jay");
	(void) Py_InitModule("jay", JayMethods);
}


int main(int argc, char *argv[]) {
	/* Pass argv[0] to the Python interpreter */
	Py_SetProgramName(argv[0]);

	/* Initialize the Python interpreter.  Required. */
	Py_Initialize();

	/* Add a static module */
	initjay();
	Py_Exit(0);
}

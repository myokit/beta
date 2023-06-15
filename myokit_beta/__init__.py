#!/usr/bin/env python
"""
This is the main module.
"""

#
# Paths
#

# Myokit root
import os, inspect, platform  # noqa
try:
    frame = inspect.currentframe()
    DIR_MYOKIT = os.path.abspath(os.path.dirname(inspect.getfile(frame)))
finally:
    # Always manually delete frame
    # https://docs.python.org/2/library/inspect.html#the-interpreter-stack
    del frame

# Binary data files
DIR_DATA = os.path.join(DIR_MYOKIT, '_bin')

# Point Windows to included DLLs
if platform.system() == 'Windows':  # pragma: no linux cover
    libd = [os.path.join(DIR_DATA, 'sundials-win-vs')]

    # Add to path
    path = os.environ.get('path', '')
    if path is None:
        path = ''
    os.environ['path'] = os.pathsep.join([path] + libd)

    # Add DLL directories (3.8+)
    try:
        for path in libd:
            if os.path.isdir(path):
                os.add_dll_directory(path)
    except AttributeError:
        pass

    del libd, path

# Don't expose standard libraries as part of Myokit
del os, inspect, platform





from . import _sim
from ._cvodes import Simulation






def hi():
    """ Returns hello. """
    return 'Hello!'


def sum(a=10.345, b=2):
    """ Does a sum. """

    from llvmlite import ir
    from ._sim import sim1

    import llvmlite.binding as llvm

    # Create some useful types
    double = ir.DoubleType()
    fnty = ir.FunctionType(double, (double, double))

    # Create an empty module...
    module = ir.Module(name=__file__)
    # and declare a function named "fpadd" inside it
    func = ir.Function(module, fnty, name="fpadd")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    x, y = func.args
    result = builder.fadd(x, y, name="res")
    builder.ret(result)

    # Print the module IR

    # All these initializations are required for code generation!
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()  # yes, even this one

    def create_execution_engine():
        """
        Create an ExecutionEngine suitable for JIT code generation on
        the host CPU.  The engine is reusable for an arbitrary number of
        modules.
        """
        # Create a target machine representing the host
        target = llvm.Target.from_default_triple()
        target_machine = target.create_target_machine()

        # And an execution engine with an empty backing module
        backing_mod = llvm.parse_assembly("")
        engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
        return engine


    def compile_ir(engine, llvm_ir):
        """
        Compile the LLVM IR string with the given engine.
        The compiled module object is returned.
        """
        # Create a LLVM module object from the IR
        mod = llvm.parse_assembly(llvm_ir)
        mod.verify()

        # Now add the module and make sure it is ready for execution
        engine.add_module(mod)
        engine.finalize_object()
        engine.run_static_constructors()
        return mod


    engine = create_execution_engine()
    mod = compile_ir(engine, str(module))

    # Look up the function pointer (a Python int)
    func_ptr = engine.get_function_address("fpadd")

    return _sim.sim1.run(func_ptr, a, b)


def sim(plot=False):
    import myokit
    p = myokit.load_protocol('example')
    s = Simulation(p)
    d = s.run(500)

    import matplotlib.pyplot as plt
    plt.figure()
    plt.plot(d.time(), d['membrane.V'])
    plt.show()

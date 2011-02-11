#!/usr/bin/python2.4
# vim:ts=2:sw=2:softtabstop=0:tw=74:smarttab:expandtab
#
# Copyright The Android Open Source Project

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at 
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Modified by Keith Dart to conform to Pycopia style.

"""Common utility methods and objects for Droid.
"""

__author__ = 'keith@kdart.com (Keith Dart)'
__original__author__ = 'dart@google.com (Keith Dart)'

import sys


class ModuleImportError(ImportError):
    """Raised when a test module could not be located."""

class ObjectImportError(ImportError):
    """Raised when a test object could not be located."""


def Import(modname):
    """Improved import function that handles subpackage."""
    try:
        return sys.modules[modname]
    except KeyError:
        pass
    mod = __import__(modname)
    pathparts = modname.split(".")
    for part in pathparts[1:]:
        mod = getattr(mod, part)
    sys.modules[modname] = mod
    return mod


def get_module(name):
    """
    Use the Python import function to get a Python package module by name.
    Raises ModuleImportError if the module could not be found.

    Arguments:
        name: A string. The name of the module to import and run.

    Returns:
        A python module.
    """
    try:
        return sys.modules[name]
    except KeyError:
        pass
    try:
        mod = __import__(name)
    except ImportError as err:
        raise ModuleImportError("Error loading: %s (%s)." % (name, err))
    else:
        components = name.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod


def get_object(name):
    """Get an object from a Python module, or a module itself.

    Arguments:
        name:
            Python path name of object. Usually a module or a class in a module.

    Returns:
        An object identified by the given path name. may raise AttributeError
        or ModuleImportError if name not found.
    """
    try:
        return sys.modules[name]
    except KeyError:
        pass
    i = name.rfind(".")
    if i >= 0:
        try:
            mod = __import__(name, globals(), locals(), ["*"])
        except ImportError:
            pass
        else:
            return mod # path is a package module
        mod = get_module(name[:i]) # module name component
        try:
            return getattr(mod, name[i+1:]) # path is an object inside module
        except AttributeError:
            raise ObjectImportError("%r not found in %r." % (name[i+1:], mod.__name__))
    else:
        return get_module(name) # basic module name


def get_class(path):
    """Get a class object.

    Return a class object from a string specifiying the full package and
    name path.
    """
    [modulename, classname] = path.rsplit(".", 1)
    mod = Import(modulename)
    return getattr(mod, classname)


def get_objects(namelist):
    """Return a list of objects.

    Arguments:
        namelist:
            A list of object names, as strings.

    Returns:
        A list of object instances corresponding to the given names. May be
        shorter than the provided list due to objects not being found.
    """
    rv = []
    errors = []
    for name in namelist:
        try:
            obj = get_object(name)
        except ModuleImportError as err:
            errors.append(err)
        else:
            rv.append(obj)
    return rv, errors


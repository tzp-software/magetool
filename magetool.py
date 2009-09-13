#!/usr/bin/env python
#
# Copyright (c) 2009, Jacob Kragh
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials
#    provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""A CLI utility to automate repetitive tasks in Mage development."""

__author__ = "jhckragh@gmail.com (Jacob Kragh)"
__version__ = "0.1.0"

from optparse import OptionParser, SUPPRESS_HELP

def main():
    usage = """Usage: magetool [OPTION]... ACTION COMMAND ARG

The following commands are supported:
    block
    controller
    helper
    model
    module

See 'magetool help COMMAND' for more information on a specific command."""
    version = "%prog version " + __version__
    parser = OptionParser(usage=usage, version=version, add_help_option=False)
    parser.add_option("-h", "--help", action="store_true", dest="show_help")
    parser.add_option("-o", "--override", action="store_true", dest="override",
                      default=None)
    parser.add_option("-s", "--superclass", dest="superclass")
    parser.add_option("-r", "--router", dest="router")

    options, args = parser.parse_args()
    if options.show_help:
        print usage
        return
    if not len(args) > 1:
        parser.error("incorrect number of arguments")
    kwargs = dict([(k, v) for k, v in options.__dict__.items()
                  if not k.startswith("__") and v != None])

    method, module = [arg.lower() for arg in args[:2]]
    cls = module.capitalize()
    module_import = "from commands.%s import %s as cls" % (module, cls)
    try:
        exec module_import
        cls = cls(**kwargs)
    except ImportError:
        parser.error("command %s not implemented" % module)
    getattr(cls, method)(*args[2:])

if __name__ == "__main__":
    main()

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

from libraries.global_ import Global

class Model(Global):
    def help(self):
        """Print a help message describing this command."""
        print """Usage: magetool create model NAME

Description:
  Define a PHP class in Model/NAME.php and register the presence of model
  classes in the module's configuration file if this has not already been done.

Options:
  -s, --superclass=SUPERCLASS  Make the model extend SUPERCLASS.
                               Default: Mage_Core_Helper_Abstract.

  -o, --override               If --superclass=SUPERCLASS is used,
                               tell Mage that the model overrides
                               SUPERCLASS.

Examples:
  magetool create helper Data
        Define a PHP class in Model/Data.php and update the module's
        configuration accordingly.

  magetool -s Mage_Customer_Model_Address_Abstract create model Address
        Define a PHP class in Model/Address.php which extends the class
        Mage_Customer_Model_Address_Abstract and update the module's
        configuration file accordingly.

  magetool -os Mage_Customer_Model_Customer create model Customer
        Define a PHP class in Model/Customer.php which extends and overrides
        Mage_Customer_Model_Customer."""
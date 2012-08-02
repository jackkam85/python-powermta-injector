"""
Copyright (c) 2012, William Betts
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 
3. Redistributions of source code must reproduce the author lines at the top 
   of the original files. You may add to them (i.e. mention you modified the 
   file), but you may not subtract from them.
4. If redistributed in binary form you may not strip the author lines from any
   files before compiling.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies, 
either expressed or implied, of the FreeBSD Project.

Author: William Betts
File: injectorcli.py
Date: 8-01-2012

Comment:
    This class handles the parsing of the cli arguments.
"""

import argparse, sys

class InjectorCLI(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description = 'PowerMTA Injector')
        parser.add_argument('-l', '--list', required = True, help = 'The email list to inject', metavar = 'email_list.txt')
        parser.add_argument('-c', '--campaign', required = True, help = 'The campaign to send', metavar = 'example-campaign')
        parser.add_argument('-s', '--hostname', required = False, help = 'The hostname or IP address of the PMTA server to inject to. If this option is omited it defaults to 127.0.0.1', metavar = '127.0.0.1')
        parser.add_argument('-p', '--port', required = False, help = 'The port the PMTA server is listening on. If this option is omited it defaults to 25', metavar = '25')
        parser.add_argument('-f', '--use-from-as-redirect', required = False, help = 'If set to true it will use domains in the domains file as the campaigns template variable. If set to false or left blank it will use the domain part of the from address.')
        self.args = parser.parse_args()

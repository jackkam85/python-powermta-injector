A CLI injector for PowerMTA by Port25.

PowerMTA Configuration:
   PowerMTA needs to be setup to pattern match based on the mail-from.
   The from addresses in the froms file will be matched to determine
   which VMTA the will be route out of.
    
   Because of a bug in the API I'm using to submit email to PowerMTA
   you need to have a source setup for 127.0.0.1 and PowerMTA needs
   to be listening on that IP.

Setup:
    There needs to be 2 directories created lists and campaigns.

    lists/
        email-list-one.txt
        email-list-two.txt
        ... (the lists can be named anything)

    campaigns/
        <name of a campaign>/
            domains (redirect domains)
            friendly_froms (Bob Johnson, epicheals, ...)
            froms   (user@domain.com, user@domain1.com, ...)
            subjects
            bodies/
                body1.txt
                body2.txt
                ... (these can be named anything)


Body Template Variables:
    [friendlyfrom] will be replaced by a line from the friendly_froms file
    [from] will be replaces by a line from the froms file
    [to] is who you're sending the email to
    [subject] is a line from the subjects file
    [date] is the current date
    [rdomain] is either a domain from the domains file or the domain part of the from address 


<=== PROJECT LICENSE ===>

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



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
            friendly_froms (Bob Johnson, epicheals, ...)
            froms   (user@domain.com, user@domain1.com, ...)
            subjects
            bodies/
                body1.txt
                body2.txt
                ... (these can be named anything)

Bugs:
    For some reason I'm getting connection refused when I set the
    smtp server to use. Currently this has to be ran from the same box
    that PowerMTA is being ran on. PowerMTA also has to be listening
    on 127.0.0.1.

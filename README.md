
# Zekaric: Manage Your Tasks (ZMYT or My Tea)


## Table Of Contents

**1 - Summary**<br />
**2 - Discussion**<br />
**3 - Goals**<br />
**4 - Compormises**<br />
**5 - Design**<br />
**6 - Warning**<br />
**7 - Install**<br />

# 1 - Summary


"My Tea" or "Mighty" is a web based task manager for an internal network.

# 2 - Discussion


I had made attempts before using JavaScript and PHP.  First time just ham fisting a solution where there was JavaScript and PHP used together but that ended up being a mess of who does what.  Second time trying to be more heavy on the client side and light on the PHP/server side.  Sort of worked.  Hard to maintain.  Then very light on the client side and majority of the work in PHP on the server side.  That was the state of the last incarnation.  It worked but was difficult to maintain and PHP was a pain.

In the end, none of the above was simple enough and PHP was not my language of choice.  I was using it so that I could have the web site hosted by my NAS which has a web server that can only do PHP.  I have given up on that idea and tried Python for this incarnation.  This project basically uses no JavaScript (for the most part.  One line is needed for the pulldown <select> HTML items for immediate processing on a change but that's it.  It is all Python and simple text files on the server.

This incarnation of MYT when very fast compared to PHP.  Mainly because I solved a lot of the issues with the last PHP solution but all in all, working with Python instead of PHP was much more pleasing for me in general.  Python being closer to what I am used to (C programming language) with sane rules and such.  For my needs, it is fast enough.

# 3 - Goals


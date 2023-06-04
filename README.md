
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

In the end, none of the above was simple enough and PHP was not my language of choice.  I was using it so that I could have the web site hosted by my NAS which has a web server that can only do PHP.  I have given up on that idea and tried Python for this incarnation.  This project basically uses no JavaScript (for the most part.  One line is needed for the pulldown &lt;select&gt; HTML items for immediate processing on a change but that's it.)  It is all Python and simple text files on the server.

This incarnation of MYT is very fast compared to PHP.  Mainly because I solved a lot of the issues with the last PHP solution but all in all, working with Python instead of PHP was much more pleasing for me in general.  Python being closer to what I am used to (C programming language) with sane rules and such.  For my needs, it is fast enough.

# 3 - Goals



* Simple coding.

* Simple design.

* Simple maintenance.

* Short development time.

# 4 - Compormises


Performance.

When the number of tasks become large, manipulation will become quite a bit slower.  I am not too concerned about this because it is not intended to be used in a multi-user environment or for millions of tasks.  Most people have maybe at most a hundred tasks.  At that amount the performance will never be noticeable.

# 5 - Design


Keeping it stupidly simple (KISS)

The data will be found in plain text files, fields will be tab delimited since no input will have tabs used in their value so parsing of a record/line of the file will be trivial.

# 6 - Warning


This code is intended to be run in a sercure environment.  Meaning on an internal network and not open to the public.  It is not coded in a way for public access.

This program is intended to be used by a single person.  Multiple users may work but it is not guaranteed because there is no file locking to prevent file corruption.  There is also no user subsystem to identify who is currently using the program.

# 7 - Install


Copy the files to a folder.

Create an environment variable "MYT_DIR" where the files live.

Run from the command line or create a bat file with this inside it...

```
	python "%MYT_DIR%/myt.py"
```

In your browser go to...

```
	localhost:8000
```

You should now see the MYT interface.

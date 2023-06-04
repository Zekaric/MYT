################################################################################
# file:         myt.py
# author:       Robbert de Groot
# copyright:    2023, Robbert de Groot
#
# description:
# Python based web server instead of using a dedicated server.  This should make
# the code a little simpler.  This should make the app feel a bit faster in the
# browser.
################################################################################

################################################################################
# import
################################################################################
import http.server
import urllib.parse

import os

import MytState
import MytProjList
import MytTaskList
import MytDisplay
import MytCommand

################################################################################
# local
# variables
################################################################################
_hostName   = "localhost"
_port       = 8000

################################################################################
# Server class
################################################################################
class MytServer(http.server.BaseHTTPRequestHandler):

    ############################################################################
    # Process the GET call.
    def do_GET(self):

        cmd     = self.path
        cmdPart = cmd[0:2]
        command = ""
        id      = 0
        value   = ""

        # Nothing to do.  Display default screen.
        if (cmd == "/"):
            self._Display()
            return

        # Perform a command and redisplay the screen.
        if (cmdPart == "/?"):
            params = urllib.parse.parse_qs(cmd[2:])
            MytCommand.Process(params)
            self._Display()
            return

        # Browser is asking for a file.
        self._ProcessSendFile()

    ############################################################################
    # Send the new display
    def _Display(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes(MytDisplay.Process(), "utf-8"))

    ############################################################################
    # Send a file to the browser.
    def _ProcessSendFile(self):

        file               = self.path[1:]
        fileName, fileExt  = os.path.splitext(file)
        fileExt            = fileExt.lower()
        mime               = ""

        if   (fileExt == ".css"):
            mime = "text/css"
        elif (fileExt == ".ico"):
            mime = "image/ico"
        elif (fileExt == ".png"):
            mime = "image/png"
        elif (fileExt == ".jpg" or fileExt == ".jpeg"):
            mime = "image/jpeg"
        elif (fileExt == ".svg"):
            mime = "image/svg+xml"
        elif (fileExt == ".gif"):
            mime = "image/gif"
        elif (fileExt == ".webp"):
            mime = "image/webp"
        else:
            # failure
            self.send_responce(404)
            self.end_headers()
            return

        self.send_response(200)
        self.send_header("Content-type", mime)
        self.end_headers()

        file = open(file, "rb")
        content = file.read()
        file.close()
        self.wfile.write(content)

################################################################################
# global
# program
################################################################################
################################################################################
# main program
################################################################################
if __name__ == "__main__":
    # Get the environment variable for the location of the data files.
    mytDir = os.environ["MYT_DIR"]
    os.chdir(mytDir)

    # Start the program bits.
    MytState.Start()
    MytProjList.Start()
    MytTaskList.Start()

    # Start the server.
    webServer = http.server.HTTPServer((_hostName, _port), MytServer)
    print("Server start: http://%s:%s" % (_hostName, _port))

    # Process input
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    # Stop the server
    webServer.server_close()
    print("Server stop :")
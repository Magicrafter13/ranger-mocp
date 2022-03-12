from ranger.api.commands import *
#import os

#FNULL = open(os.devnull, 'w')

def get_files(fm):
    ftd = fm.thisdir
    selected_files = ftd.get_selection()
    active_file = fm.thisfile if not selected_files else None

    if not selected_files and not active_file:
        return
    else:
        file_objs = selected_files if selected_files else [active_file]
    return file_objs

class mocp_server(Command):
    def execute(self):
        #os.system("mocp --server")
        #self.fm.execute_command(["mocp", "--server"], stdout=FNULL, stderr=FNULL)
        self.fm.execute_command(["mocp", "--server"])
        self.fm.notify("mocp server started")

class mocp_enqueue(Command):
    def execute(self):
        """ Add selected files or folders to queue """

        file_objs = get_files(self.fm)
        mocp = ["mocp", "--enqueue"]
        mocp.extend([f.path for f in file_objs])
        self.fm.execute_command(mocp)
        self.fm.notify("Files were sent to mocp queue")
        self.fm.thisdir.mark_all(False)

class mocp_clear(Command):
    def execute(self):
        self.fm.execute_command(["mocp", "--clear"])
        self.fm.notify("Cleared playlist")

class mocp_play(Command):
    def execute(self):
        self.fm.execute_command(["mocp", "--play"])
        self.fm.notify("Started from beginning of playlist")

class mocp_playit(Command):
    def execute(self):
        """ Add selected files or folders to playlist """
        file_objs = get_files(self.fm)

        mocp = ["mocp", "--playit"]
        mocp.extend([f.path for f in file_objs])
        self.fm.execute_command(mocp)
        self.fm.notify("Sent files to mocp")
        self.fm.thisdir.mark_all(False)

class mocp_stop(Command):
    def execute(self):
        self.fm.execute_command(["mocp", "--stop"])
        self.fm.notify("Stopped playing")

class mocp_next(Command):
    def execute(self):
        self.fm.execute_command(["mocp", "--next"])
        self.fm.notify("Skipping track")

class mocp_previous(Command):
    def execute(self):
        self.fm.execute_command(["mocp", "--previous"])
        self.fm.notify("Replaying previous track")

class mocp_exit(Command):
    def execute(self):
        self.fm.execute_command(["mocp", "--exit"])
        self.fm.notify("Shutting down mocp server")

class mocp_pause(Command):
    def execute(self):
        self.fm.execute_command(["mocp", "--pause"])
        self.fm.notify("Paused mocp")

class mocp_unpause(Command):
    def execute(self):
        self.fm.execute_command(["mocp", "--unpause"])
        self.fm.notify("Unpaused mocp")

class mocp_toggle_pause(Command):
    def execute(self):
        self.fm.execute_command(["mocp", "--toggle-pause"])
        self.fm.notify("Toggled play/pause mocp")

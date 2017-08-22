import os
import sys
import signal

def waitpid():
    (pid, status) = os.waitpid(-1,
                               os.WUNTRACED | os.WCONTINUED)
    if os.WIFSTOPPED(status):
        s = "stopped sig=%i" % os.WSTOPSIG(status)
    elif os.WIFCONTINUED(status):
        s = "continued"
    elif os.WIFSIGNALED(status):
        s = "exited signal=%i" % os.WTERMSIG(status)
    elif os.WIFEXITED(status):
        s = "exited status=%i" % os.WEXITSTATUS(status)
    print "waitpid received: pid=%i %s" % (pid, s)

childpid = os.fork()
if childpid == 0:
    # Child
    os.kill(os.getpid(), signal.SIGSTOP)
    sys.exit()

waitpid()
os.kill(childpid, signal.SIGCONT)
waitpid()
waitpid()

import pexpect ##import pexpect to interact on our behalf
PROMPT = ['#', '>>> ', '> ', '\$ '] ##look for these prompts
def send_command(child, cmd):
    child.sendline(cmd) ##Open cmd
    child.expect(PROMPT) ##Look for prompt
    print(child.before)
def connect(user, host, password):
    ssh_newkey = "Are you sure you want to coninue connecting?" #Define SSH_newkey prompt
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr) ##Create child application and pass connStr as start creds
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0: ##If remote console returns 0 by timeout or not asking for ssh_newkey, show that there was an error connecting
        print("[-] Error connecting")
        return
    else:
        child.sendline("yes") ##Otherwise look for password prompt
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
        if ret == 0: ##If no password prompt return error
            print("[-] Error connecting")
            return
    child.sendline(password) ##Send password
    child.expect(PROMPT) ##Look for prompt from cmd
    return child
def main():
    host = 'localhost' ##hostname to pass
    user = 'root' ##username to pass
    password = 'toor' #password to pass
    child = connect(user, host, password) ##pass above variables to connect function to get child
    send_command(child, 'cat /etc/shadow | grep root')
if __name__ == '__main__':
    main()
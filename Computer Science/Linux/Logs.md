# Logging in Linux

Linux systems come with built-in logging systems that are both flexible and powerful, which can record almost anything that is going on within systems.

System administrators need to be able to see and analyze what is going on with their system(s), and UNIX and Linux certainly provide an extensive set of logs from a number of logging utilities. The primary utility is the syslog, which handles logging messages that are generated by processes such as the kernel, File Transfer Protocol (FTP), use of the su command, and log-in or log-out activities. To keep track of what has been happening to the system, UNIX and Linux maintain log files that, in the first versions, simply recorded who logged in and logged out and what they did in between; however, modern versions have expanded logging to record information such as file transfers (especially over a network), users who are trying to become superusers (both successful and failed), and many more.

The majority of log files are simple plaintext files that are written by system programs in a line-by-line format. For example, each time that a user attempts to use the su command to become root, the su process appends another line to the sulog log file, recording whether that su attempt succeeded or failed.

Log files are important building blocks of system security that provide a record of a computer's history, something that can make it easier to troubleshoot problems—both constant and intermittent—and various cyberattacks. Log files can also help piece together the information to determine the source of a bug, what happened during a break-in, how much damage occurred, and—possibly—what to do to ensure that it does not happen again. Alternatively, those logs can help in rebuilding the system, conducting further investigation, recovering data files, or performing needed service.

| Common Log Files | Description |
| ---------------- |------------ |
| acct or pacct |	This records commands that are run by every user. This is a special kind of logging called process accounting and is normally when users are billed for central processing unit (CPU) time, or after a break-in, to help determine the commands that a user executed (provided that the log file was not deleted). This command has a lot of other purposes, such as checking if anyone is using old or illegal software or if anyone is playing games on the system. |
| access_log |	This is the log of Internet pages and files accessed. This is used by the National Center for Supercomputing Applications (NCSA) HyperText Transfer Protocol daemon (HTTPd) server, which is particularly common. Every Web server package has some way to log accesses. This usually logs where the hostname access was from, remote log in and username, time of access, the HTTP command executed, and the number of bytes sent. This is usually in plaintext and thus can be edited with a standard text editor. |
| aculog |	This is the log of dial-out modem use. |
| lastlog |	This logs each user's most recent successful log-in time and sometimes also saves the last unsuccessful log in. The time of each login is logged, but the contents of the file are overwritten at each login. |
| loginlog |	This records bad log-in attempts (i.e., a bad password entry three or five times in a row). |
| messages |	This records the output (display) to the system console and other messages that are generated from the syslog facility. |
| sulog |	This is the log of the use of the su command (both successful and unsuccessful attempts). |
| utmp |	This records all of the users who are currently logged in. This is a binary file that maintains a record of every active tty process. The line contents of this file are displayed by the who command. This is often stored in the /etc directory in UNIX. |
| utmpx |	This is the extended utmp and includes details such as the hostname where the user(s) logged in from, the device, and session name. |
| wtmp |	This is the permanent record of each time that a user logs in or out (including via FTP), plus each time that the system was started up, rebooted, or shut down. The last utility program displays the contents of this file in a human-readable format. |
| vold.log |	This logs errors that are encountered with the use of external media (e.g., floppy disks, tapes, CD-ROMs, and DVDs). |
| xferlog |	This logs the FTP access. |

## Logging Facilities

The system logger operates in a quite straightforward manner. Programs and processes send their messages to syslog daemon (syslogd), which writes the message to the correct log file(s).

Four basic syslog terms:

- Facility: This identifies the application or process that submits the message to be logged, such as the kernel, su, or the FTP program.
- Priority: This indicates the message’s importance. This is defined as levels that range from things as simple as common announcements to debug information and all the way up to critical events.
- Selector: This identifies combinations of one or more facilities and levels. When an incoming message matches a selector’s set of facilities and levels, syslogd performs an action.
- Action: This identifies what syslogd does to an incoming message that matches a selector, such as writing the message to a log file, echoing the message to the console (terminal screen) or another device, writing the message to a user, forwarding the message to another syslog on another server somewhere on the network, or some combination of these actions (e.g., logging and echoing, logging and forwarding, and so on).
UNIX and Linux define a finite set of facilities that can be used for the selector. As with the common log files, not all facilities are the same on all versions.

| Facility | Description |
| -------- | ----------- |
| auth | Processes that are related to requesting names and passwords (e.g., getty, su, or login). |
| authpriv | Same as auth but is logged to a file that can only be read by selected users. |
| console | Used to capture messages that are echoed to the system console. |
| cron | Messages from the crond daemon (cron system scheduler). |
| daemon | System daemon catch-all. |
| ftp | Messages relating to the FTP daemon. |
| kern | Kernel messages. |
| local0...local7 | Local facilities defined per site. |
| lpr | Messages from the line printing system. |
| mail | Messages relating to the mail system. |
| mark | Pseudo-event that is used to generate time stamps in log files. |
| news | Messages relating to Network News Transfer Protocol (NNTP). |
| ntp | Messages relating to Network Time Protocol. |
| user | Regular user processes. |
| uucp | UNIX-to-UNIX Copy (UUCP) subsystem. |

## Logging Priorities

UNIX and Linux define nine logging priorities, as follows:

| Priority | Description |
| -------- | ----------- |
| emerg | This stands for emergency; a condition that should be broadcast to all users, such as an impending system crash, exists. |
| alert | A condition that should be addressed immediately, such as a corrupted system database, exists. |
| crit | This stands for critical; a condition that should be addressed, such as a hardware error, exists. |
| err | This stands for error; an ordinary condition that should be addressed exists. |
| Warning | A condition that should be addressed exists. |
| notice | A condition that is not an error but should be addressed exists. |
| info | This stands for informational message. |
| debug | This stands for debugging information and refers to messages that are used for debugging programs. |
| none | This refers to the pseudopriority that is used to specify when not to log messages. |

## Viewing the Logs

The lastcomm or acctcom program displays the contents of the acct or pacct file in a human-readable format, as follows:

![image](https://user-images.githubusercontent.com/73081144/145924048-200ac8e9-37b3-422c-967e-39f4b7c0e317.png)

Running the last command with no arguments displays all logins and logouts on every device and will continue to display the entire file until it is aborted by entering "Ctrl + C" (interrupt).

![image](https://user-images.githubusercontent.com/73081144/145924057-6ffc09ca-f5cc-4931-9397-0e461ec2b261.png)

UNIX logs all failed log-in attempts in the loginlog; failed log-in attempts are defined as a log-in attempt with a bad password multiple times in a row. It is a plaintext file, so it can be displayed with the cat command, as follows:

![image](https://user-images.githubusercontent.com/73081144/145924067-dfd36d53-6c3f-4808-8741-aad45c6616a9.png)

Many versions of UNIX place a copy of any message printed on the system console in a file called messages, which can be in /var/log or /var/adm. In the following example, computer ctu8 is having a problem with a full directory, which is most likely a full-disk issue:

![image](https://user-images.githubusercontent.com/73081144/145924076-c429c53d-5e85-4b50-a53f-5c9fc4f0d4d7.png)

UNIX records the use of the su command by printing to the console (which logs it in the messages log file) and to the log file sulog. Failed attempts of su create a bad su error, and successful ones create a su message. The following is a sample sulog:

![image](https://user-images.githubusercontent.com/73081144/145924087-97fab82a-022d-4a74-a18e-66fd30bb2a8c.png)

In this example, user starsong does not know the superuser password because he or she failed in every attempt, but user redstar seems to have merely mistyped the superuser password on the first attempt and typed it correctly on the second.

Checking sulog is a good way to figure out if anyone is trying to become the superuser too much. Dozens of su attempts from one user, or from one who is not supposed to need superuser access, might rate further investigation.

## System Log

In addition to the various logging facilities previously discussed, UNIX and Linux provide a general-purpose logging facility called syslog. The syslog utility is commonly and extensively used to log user activity to standard log files. The syslogd daemon is the heart of the syslog facility, and the syslog daemon must be running to send and receive log messages. The syslog facility can monitor the kernel, user processes, mail, printer usage, any processes that need a username or password, system daemons, and up to seven other things, as defined by sysadmin—that is, it can monitor almost anything. The daemon is started via a script, such as /etc/init.d/syslog.

The syslog process is started by the system during start-up. When syslog starts, it reads its config file (/etc/syslog.conf), which states what to monitor, and then listens for syslog messages. Each message consists of four parts, as follows:

- Program name
- Facility
- Priority
- Log message

Consider the following example:

![image](https://user-images.githubusercontent.com/73081144/145924351-51fcfc95-82d9-40a4-8eb1-f4ee5f874720.png)

The message shows a syslog message from the log-in program, saying that someone tried to log in to terminal tty8 as root. The authorization and the critical error level are not shown.

The syslog uses a conf (configuration) file, such as /etc/syslog.conf, to define what messages are logged and where. A typical syslog.conf file looks something like the following, although the format of the syslog.conf file tends to vary from system to system:

![image](https://user-images.githubusercontent.com/73081144/145924450-10494e8b-b2bd-41e5-addd-d79b9a732381.png)

The left-hand column is the selector column and has two parts: facility and priority. The combination of the facility and the priority identifies which messages are to be logged. For example, the entry kern.debug selects all of the debug messages (priority) that are generated by the kernel (facility). A splat (*, or asterisk) in place of either the facility or priority indicates all—that is, *.debug means all debug messages, kern.* means all of the messages that are generated by the kernel, and so on. Commas separate multiple facilities. For example, daemon,auth.notice selects the notice messages (priority) that are generated by both daemon and auth (facilities). A semicolon (;) groups two or more selectors together. For example, err;kern.debug;auth.notice selects *.err, kern.debug and the auth.notice selectors together on one line.

The right-hand column is the action field and specifies one of the following five actions:

- Log to a file or a device. The action field contains an absolute address pathname, such as /var/adm/lpd-errs or /dev/console.
- Send a message to a user. The action field contains a username (such as root), or usernames; multiple usernames must be separated with commas (root, starsong, redstar, tanya).
- Send a message to all users. This is indicated by an asterisk (*).
- Pipe the message to a program. The action field contains a UNIX pipe symbol (|) followed by the program name (e.g., |devtalker means pipe—that is, send the message as input to the program devtalker).
- Send the message to the syslog on another host. The action field contains an at sign (@) followed by the destination hostname (e.g., @prep.ai.ctu.edu).

Note that by default, syslog will accept any log messages sent by any host to the local syslogd User Datagram Protocol (UDP) port.

In the first line of the example above (i.e., *.err;kern.debug;auth.notice /dev/console*), the selector column (i.e., *.err;kern.debug;auth.notice*) tells syslog to log all error messages (*.err*), all kernel debug messages (*kern.debug*), and all notice messages that are generated by the authorization process (i.e., *auth.notice*). The second column, the action (i.e., */dev/console*), indicates that the messages are to be logged to the console device—that is, displayed on the main system console’s screen.

## The syslog Messages

The following list summarizes some typical messages (Gite, 2014):

| Program |	Message | Meaning |
| ------- | ------- | ------- |
| halt | halted by <user> | <user> used the halt command to shut down the system. |
| login | ROOT LOGIN REFUSED ON <tty> [FROM <hostname>] | The root tried to log in to a terminal that is not secure. |
| login | REPEATED LOGIN FAILURES ON <tty> [FROM <hostname>] <user> | Somebody tried to log in as <user> and supplied a bad password more than five times. |
| reboot | rebooted by <user> | <user> rebooted the system with the /etc/reboot command. |
| su | BAD SU <user> on <tty> | Somebody tried to su to the superuser and did not supply the correct password. |
| shutdown | reboot, halt, or shutdown by <user> on <tty> | <user> used the /shutdown command to reboot, halt, or shut down the system. |
| date | date set by <user> | <user> changed the system date. |
| login | ROOT LOGIN <tty> [FROM <hostname>] | The root logged in. |
| su | <user> on <tty> | <user> used the su command to become the superuser. |
| getty | <tty> | /bin/getty was unable to open. |

## Log File Names

Logs are usually stored under the /var/log directory, but the configuration file for the syslog program can put the log files anywhere. The command ls -lt /var/log uses the -t (time last modified) option to the ls -l command and shows which log files have been changed recently.

The following table shows some common Linux log file names and what they are used for:

| Log | Purpose |
| --- | ------- |
| /var/log/auth.log | Authentication logs. |
| /var/log/boot.log | System boot log. |
| /var/log/cron | Crond logs (from the cron daemon’s cron jobs, or scheduled operations). |
| /var/log/httpd/ | Web server access and error logs directory. |
| /var/log/kern.log | Kernel logs. |
| /var/log/lighttpd/ | Lighttpd access and error logs directory. |
| /var/log/maillog | Mail server logs. |
| /var/log/messages | General message and system-related messages (e.g., errors). |
| /var/log/mysqld.log | MySQL database server log file. |
| /var/log/qmail/ | Qmail log directory (more files inside this directory). |
| /var/log/syslog | General message and system-related messages (e.g., errors). |
| /var/log/secure or /var/log/auth.log | Authentication log. |
| /var/log/utmp or /var/log/wtmp | Log-in records file. |
| /var/log/yum.log | Yum command log file. |

Most of the logs have multiple copies. The copies are the backups and archives of the logs. For example, the messages logs are the following:

![image](https://user-images.githubusercontent.com/73081144/145925647-bf504f20-8842-4956-8bfd-5fa8179a30ad.png)

The *messages* file is the current, active messages log. The *messages-yyyymmdd* files are weekly backups, and the *messages-yyyymmdd.gz* files are archived files. The .gz file extension stands for GNU zip (GZIP), which is a standard archive format for compressed files used on UNIX- and Linux-based computers.

Looking at /var/dev in long format, you can see the dates of files and the time of the backup or archive that was made (pretty much the same time every day), as follows:

![image](https://user-images.githubusercontent.com/73081144/145925668-df880d0b-252d-471b-9042-f6983e45524a.png)

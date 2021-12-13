# Linux CLI Commands

## pwd

pwd - prints path of the current directory.

## ls

ls - lists files in the currect directory.

- -l - shows details about files
- -a - shows all files, even hidden ones
- The first character gives the file type, and the next nine characters are the permission mask, or permission bits, that shows (and controls) who can read, write (change), and execute the file and its contents.
- Next comes the link count, which is the number of links to the file’s inode (something that stores the metadata—all of the information about the file except its name). This is followed by the file’s owner’s username, which tells who owns the file and who is most responsible for that file. This can be any user’s name, be it a regular user, a system user or daemon, or even an application name.
- The group name shows the group that the file is associated with and gives the permissions for all of the members in that group.
- The next attribute shown is the file’s size, which is given in either bytes or blocks (in UNIX, the default size for a block of data is 4096 bytes).
- The next attribute is the time stamp for when the file was created or when it was modified or changed. This time stamp is given in a date and a time format, as shown with month (three characters), day (2 characters), and four digits for the time, two for the hour on a 24-hour clock (e.g., 1:00 p.m. = 13, 6:00 p.m. = 18, and so on), and two for the minute, separated by a colon.
- Finally, the name of the file is shown.
- If it is a link file, the name of the file linked to is shown (mtab -> /proc/mounts).

![image](https://user-images.githubusercontent.com/73081144/145730485-4bf9128d-e2a8-4219-9bfb-57fc1ca2fba0.png)

## cd

cd 'dir' - move to other directory.

## cat

cat 'file' - shows the contents of the file.

## chmod

chmod - changes the permissions mask on a file or directory.

- chmod –[options] mode filename
- -R (recursive) - this includes all of the files in the directory and in all subdirectories.
- -f (force) - this forges ahead with all of the objects even if errors occur.
- -v (verbose) - this displays feedback on all of the files processed and the changes made.
  
Symbolic permissions coding allows you to add or remove permissions by specifying the set of permissions (user, group, or other) that you want to change. When using symbolic permissions, the chmod format is as follows:

chmod [references][operator][modes] filename

References refer to the set of permissions: u for user, g for group, o for other, and a for all, which includes all three. Operator refers to adding or removing permissions: + for add, - for remove, and = for changing the set of permissions for that reference. Modes are the permissions themselves: r, w, or x. For example, if you want to add write to the group permissions for the file lotsofun, the chmod command would be as follows:

chmod g+w lotsofun

To remove write permissions (w) for all sets (a), use the following command:

chmod a-w lotsofun

To set the permissions for the owner and the group (ug) to read and execute (rx) only (no write permission), use the following command:

chmod ug=rw lotsofun

## chown

chown - this is used for changing the ownership (and group assignment)

- chown [– options] newowner filename
- newowner can be either a log-in name or a user ID, and it can also take the form of newowner:newgroup and change the group as well as the owner.
- h: This changes soft links.
- help: This shows the help message for chown.
- R: This stands for recursive. (i.e., change the owner of all files from this directory down; does not work with filenames)
- V,c: This stands for verbose and displays feedback on all of the files processed and the changes made.

For example, you own willie.txt, but you want to give it to another user on the system named ww543267. You would use the following command:

chown ww543267 willie.txt

You want to change both the owner and the group of willie.txt to that of ww543267 and ww543267's group, lumpagroup. Using chown to change both the owner and group, you would use the following:

chown ww543267: lumpagroup willie.txt

## chgrp

chgrp - this is used for just changing the group assignment.

- chgrp [-options] newgroup filenames
- f: This enables silent mode, which means that errors are not printed.
- R: This stands for recursive. (i.e., change the group of all files from this directory down; does not work with file names)
- v: This stands for verbose. Changes are described.
- help: This displays a help message and text.

For example, if you want to change the owning group of the file gloop.txt to the group named bucket, the command would look like the following:

chgrp bucket gloop.txt

To change the owning group of the directory /gobstopper/testing and all of the files and subdirectories inside it to the group slugworth, the following command is used:

chgrp -R slugworth /gobstopper/testing

## mount & unmount

mount - the mount command maps a directory, which can be an entire file system, into the existing directory tree.

- mount [option…] directory or mount [option…] device or mount filesystem mount_point

- -h - prints a help message.
- -V - prints the mount's version information.
- [-t type] - lists all mounted file systems (of file type “type”). The option -l adds labels to this listing ([-l] [-t type]).
- -a - mounts all regular file systems listed in the file system catalog, that is, all the file systems listed in the /etc/<filesystem>. This is usually executed by the startup scripts at boot time.
  
For example, the following command will connect the file system stored on the disk partition represented by /dev/sda4 to the path /usr/empty1:

mount /dev/sda3 /usr/empty1

The command ls /usr/empty1 will show the file system’s contents as long as it stays mounted.

![image](https://user-images.githubusercontent.com/73081144/145738037-6ec475d9-3672-48e1-a5a5-669a33449484.png)

1. Make a mount point (mkdir /usr/empty1).
Note: Doing an ls -l on the new mount point shows that it is empty.

2. Mount the new file system (mount /dev/sda3 /usr/empty1).

3. Doing an ls -l on the new mount point now shows the file system from /dev/sda1.

To access the files on a CD-ROM, mount the CD-ROM in the following directory tree:

mount /dev/cdrom /media/cdrom

In this command, the CD-ROM is /dev/cdrom, and its mount point is /media/cdrom. After the command is run, any file located on the CD-ROM is now accessible to the system.

unmount - used to disconnect file systems from the directory tree.

- umount /dev/sda3 (unmount device sda3) or umount /usr/empty1 (unmount mount point /usr/empty1)

Both the mount and umount commands require root (superuser) privileges to run successfully.

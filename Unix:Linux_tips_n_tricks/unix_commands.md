## Useful terminal *(zsh, bash)* commands on UNIX based systems.
### Tested on **Ubuntu server 20.04** and on **MacOS Big Sur**
1. **Processes overview.**
    - How to list processes by user name
        -  ``ps -U user_name``
    - How to list processes by group
        - ``ps -G group_name``
    - Processes display details
        - ``ps -r -u `whoami` -o comm,pcpu,pmem,pid,ppid,lstart,user,state | head -n 6``
        - E.g of what the output looks like
            ```
            COMM              %CPU %MEM   PID  PPID STARTED   USER     STAT
            /Applications/Vi   3.9  1.5  7774  7765 Sat  4 Sep 20:15:12 2021     peterpan R
            /System/Applicat   0.9  0.9  1318     1 Wed  1 Sep 18:53:27 2021     peterpan S
            /System/Applicat   0.9  1.3  3735     1 Thu  2 Sep 20:38:48 2021     peterpan S
            ps                 0.9  0.0  8895  7990 Sat  4 Sep 21:22:47 2021     root     R+
            /Applications/Vi   0.9  1.1  7765     1 Sat  4 Sep 20:15:11 2021     peterpan S
            ```
        - Further explanations about the states **STAT**: See ps man, section **state**
    - Find process details given its pid
        - ``ps -p ‹pid›``
1. **Display open ports**
    - ``lsof -i``  Tool available in both MacOS and Ubuntu
        - i:  selects the listing of files any of whose Internet address matches the address specified in i. e.g: -i4, -i6.
    - ``lsof -i tcp``  Specific protocol filtered
    - Look for specific port
        - ``lsof tcp:443``
    - ``nc -vv -z localhost 1-65535 > scan_results.txt 2>&1 && cat scan_results.txt | grep succeeded``
        - z: Tells netcat to scan only for open ports without sending any data
        - v: Tells netcat to run in verbose mode
        - `> scan_results.txt 2>&1` : redirects both sterr and stout to scan_results.
        - `| grep succeeded` : greps opened ports.
    - Note [netstat](http://netstat.net) is not installed by default in Ubuntu server.
    - Note that [ss](https://www.man7.org/linux/man-pages/man8/ss.8.html) is not installed by default on MacOS.
1. Search specific words in text
    - **Note:** To perform this grep can be used. Note however that MacOS uses by default the BSD grep, whereas other UNIX based OSs, such as Ubuntu
    use the GNU version or even other versions by default. The commands below were tested in both MacOS and Ubuntu and the version difference
    was meaningless, at least at the time of writing.
    - In MacOS:
        -
        ```
        peterpan@Pedros-MBP ~ % grep --version
        grep (BSD grep) 2.5.1-FreeBSD
        ```
    - In Ubuntu server:
        -
        ```
        ubuntu@ubuntu:~$ grep --version
        grep (GNU grep) 3.4
        Copyright (C) 2020 Free Software Foundation, Inc.
        License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.
        Written by Mike Haertel and others; see
        <https://git.sv.gnu.org/cgit/grep.git/tree/AUTHORS>.
        ```
    - Search for word in a file, ignoring letter cases
        - ``grep -i "‹word_to_search›" file_name``
            - -i: Ignores letters cases, i.e., match abc, Abc, ABC
    - Recursively search string in all files of current dir and all files of sub-dirs
        - ``grep -i -r "‹word_to_search›" ./dir_path/``
            - **Note:** If there's a match the name of the file is output in front of it.
            To avoid this, use the option ``-h``
    - Multiple search patterns
        - ``grep -e how -e to -e forge *.txt``
            - **Note:** The -e option is useful if the word to search also has an hyphen.
    - Search exact matches
        - ``grep -w "exact_match" file_name``
    - Search X different words
        - ``egrep -w "X1|X2|X2" file_name``
    - Output total number of word X in a file.
        - ``grep -c "X" file_name``
    - Output line where match was found
        - ``grep -n -w "test_data" file.txt``
    - Match only lines that do not contain the specified word
        - ``grep -v par /path/to/file``
    - Display name of files that do not contain search pattern
        - ``grep -L "pattern_to_search" *.txt
    - List file names whose contents mention a specific word
        - ``grep -l 'primary' *.c``
    - Display output in specific colors
        - ``grep --color root /etc/passwd``
            - **Note:** The color in the output == the GREP_COLOR environment variable.
    - Limit grep output lines *(in this case 3 lines)*
        - ``grep "how" -m3 testfile1.txt``
    - Regex search
        - ``grep -G ".*data" *.txt``
1. Find files
    - Search file by name, case insensitive.
        - ``find . -iname "file_name"``
    - Search for empty files
        - ``find - iname -empty``
    - Search based on time
        - mtime *(Modification time)*: When the file’s content was modified last time.
        - atime *(Access time)*: When the file was accessed last time.
        - ctime *(Change time)*: When the file attributes were modified last time.
        - E.g: ``find . -atime -2h30min`` : Search for files accessed less then 2h30min ago.
    - Search based on size, e.g: Finds files bigger than 2 Megabytes.
        - ``find . -size +2M``
        - Details about the -size option:
            - k kilobytes (1024 bytes)
            - M megabytes (1024 kilobytes)
            - G gigabytes (1024 megabytes)
            - T terabytes (1024 gigabytes)
            - P petabytes (1024 terabytes)
    - Search based on permissions
        - ``find . -type f -perm 777``
        - **Note:** f if for files, d if for directories in the *-type* option.
1. Close or open ports
    - Check open ports in section **Display open ports**
    - Get PID of process related to the port.
    - Kill process
        - ``kill -9 PID``
    - Use the option -t of lsof to get only the PIDs
        - ``lsof -t -i tcp | xargs -Iarg1 kill -9 arg1``
            - t: specifies  that lsof should produce terse output with process identifiers only and no header - e.g., so that the output may be piped to kill(1).  -t selects the -w option.
1. Create a new user and a new group
    - Create new user
        - MacOS: ``sysadminctl -addUser user_test -newPassword -``
        - Linux: ``adduser user_test``
    - Delete user
        - MacOS: ``sysadminctl -deleteUser user_test``
        - Linux: ``userdel -r -f test_user``
            - r: remove home directory and mail spool.
            - f: force removal of files.
    - Check user groups
        - ``groups user_name``
    - Create new group
        - MacOS: ``sudo dseditgroup -o create test_group``
        - Linux: ``groupadd test_group``
    - Add user to group
        - MacOS: ``sudo dseditgroup -o edit -a peterpan -t user test_group``
        - Linux: ``sudo usermod -a -G sudo geek``
    - Delete group
        - MacOS: ``sudo dseditgroup -o delete test_group``
        - Linux: ``groupdel test_group``

1. Change file/folder permissions and ownership
    - Change ownership of folder/file
        - ``sudo chown -R user_test:staff test_folder``
            - Where user_test is the new owner, staff the new group and test_folder the folder to change permissions.
            - R: Recursively apply the changes to files and sub-folders.
    - Change folder/file permissions
        - ``sudo chmod u-x,g+w -R test_folder``
            - R: Recursively apply the changes to files and sub-folders.
            - u-x: Removes execute permissions for the user
            - g+w: Grants write permissions for the group
            - Further explanations:
                ```
                u - The file owner.
                g - The users who are members of the group.
                o - All other users.
                a - All users, identical to ugo.
                - Removes the specified permissions.
                + Adds specified permissions.
                = Changes the current permissions to the specified permissions. If no permissions are specified after the = symbol,
                all permissions from the specified user class are removed.
                ```
1. Check storage in human format
    - ``df -H -a``
        - H: "Human-readable" output.  Use unit suffixes: Byte, Kilobyte, Megabyte, Gigabyte, Terabyte and Petabyte in order to reduce the number of digits to three or less using base 10
        for sizes.
        - a: Show all mount points, including those that were mounted with the MNT_IGNORE flag.
1. Nice/re-nice process
    - **Some theory**
        - Priority value — The priority value is the process’s actual priority which is used by the kernel to schedule a task.
        System priorities are 0 to 139 in which 0 to 99 for real-time and 100 to 139 for users.
        - Nice values are user-space values that we can use to control the priority of a process. The nice value range is -20 to +19
        where -20 is highest, 0 default and +19 is lowest.
        - The relation between nice value and priority is as such - Priority_value = Nice_value + 20
    - Check priority and niceness of processes for some user
        - ``ps -u user -o pri,ni,ppid,pid,comm``
            - pri: Priority value
            - ni: Niceness value
            - ppid: Parent process ID.
            - pid: Process ID.
            - comm: Command used to launch process.
        - **Note:** htop is a good alternative to visualize in real time the above. To install it:
            - MacOS: ``brew install htop``
    - Launch a process with specific niceness
        - ``nice -n <nice_value> ./program``
    - Change niceness of running process
        - ``sudo renice -n <nice value -20 to 19> <PID>``

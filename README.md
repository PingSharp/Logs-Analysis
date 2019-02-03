# Logs Analysis Project

An internal reporting tool that use information from the database to discover what kind of articles the site's readers like and the favorite authors.

## Getting Started

### for Mac or Linux 
regular terminal program on your computer
### for Windows
you need to use Git Bash terminal for this Project,if you don't have ,[click here to install](https://git-scm.com/downloads)

1. install VirtualBox ,[You can download it from here.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.
2. download Vagrant from [here](https://www.vagrantup.com/downloads.html).Install the version for your operating system.
3. download this Logs-Analysis project zip file from github,there is the VM configuration in this project.Unzip the file,This will give you a directory called Logs-Analysis-master.
4. under this Logs-Analysis-master directory find and change to the vagrant directory,run the command
```
vagrant up
```
This will cause Vagrant to download the Linux operating system and install it. This may take quite a while.when vagrant up is finished running,you can run 
```
vagrant ssh
```
to log in to your newly installed linux VM.
5. find the files for this Project
inside the VM,change directory to /vagrant/news.
6. run the python programm
```
 python newsdb.py
```
then you will see the 3 questions and their answers.





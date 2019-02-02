# Logs Analysis Project

An internal reporting tool that use information from the database to discover what kind of articles the site's readers like and the favorite authors.

## Getting Started

###for Mac or Linux 
regular terminal program on your computer
###for Windows
you need to use Git Bash terminal for this Project,if you don't have ,[click here to install](https://git-scm.com/downloads)

1.install VirtualBox ,[You can download it from here.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.
2.install Vagrant,[You can download it from here.](https://www.vagrantup.com/downloads.html)
3.download the vm configuration zipfile and unzip it[download here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)This will give you a directory called FSND-Virtual-Machine.
4.find and change to the vagrant directory,run the command
```
vagrant up
```
This will cause Vagrant to download the Linux operating system and install it. This may take quite a while.when vagrant up is finished running,you can run 
```
vagrant ssh
```
to log in to your newly installed linux VM.
5.find the files for this Project
inside the VM,change directory to /vagrant/news.
6.run the python programm
```
 python newsdb.py
```






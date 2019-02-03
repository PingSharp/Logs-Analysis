# Logs Analysis Project

An internal reporting tool that use information from the database to discover what kind of articles the site's readers like and the favorite authors.

## Getting Started

### for Mac or Linux 
regular terminal program on your computer
### for Windows
you need to use Git Bash terminal for this Project,if you don't have ,[click here to install](https://git-scm.com/downloads)
### next steps for all
1. install VirtualBox ,[You can download it from here.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.
2. download Vagrant from [here](https://www.vagrantup.com/downloads.html). Install the version for your operating system.
3. download this Logs-Analysis project as zip file from github or use git clone. Inside this project is the VM configuration. In case you download it as zip file, Unzip the file. This will give you a directory called Logs-Analysis-master. Also if you git cloned it. 
4. download the sql data
[download here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant/news directory which is under Logs-Analysis-master directory.
5. Open a terminal or git bash. Under the Logs-Analysis-master directory find the vagrant directory and change to this location. After run the command
```
vagrant up
```
This will cause Vagrant to download a Linux operating system image and install it. This may take quite a while.when vagrant up is finished running,you can run 
```
vagrant ssh
```
to log in to your newly installed linux VM.

6. To execute the reporting tool first we need to fill the data into the local database, so first
```
cd /vagrant/news
```
to change into the vagrant directory and use the command 
```
psql -d news -f newsdata.sql
```
to connect to your installed database server and execute the SQL commands from the downloaded file "newsdata.sql", creating tables and fill them with data.

7. run the python programm with this command
```
 python newsdb.py
```
or
```
./newsdb.py
```
then you will see the 3 questions and their answers.

Beside there exist already a db.log file in the same folder show the results.




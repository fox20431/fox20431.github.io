- Go to /usr/local/share/ca-certificates/
- Create a new folder, i.e. "sudo mkdir school"
- Copy the .crt file into the school folder
- Make sure the permissions are OK (755 for the folder, 644 for the file)
- Run "sudo update-ca-certificates"



https://askubuntu.com/questions/645818/how-to-install-certificates-for-command-line
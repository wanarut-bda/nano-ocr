# Jetson Production Auto-Running Step
## `disable` auto-update (gui setting > Software & Updates > Updates > `Auto check updates: Never`)
## `disable` suspend 5 minutes (gui setting > Brrightness & Lock > `'Turn screen off'=Never` & `Lock=OFF`)
## `enable` auto-login (gui setting>User Accounts > Unlock > Automatic `Login=ON`)
## `add` startup app `terminal` => `gnome-terminal`
### install zsh & nano
`$ sudo apt install -y zsh nano`
### change default shell to zsh
`$ chsh -s $(which zsh)` <br>
## After reboot shell will change to zsh select 0 to creating the file ~/.zshrc
### disable sudo password
`$ sudo visudo` <br>
### add new line in file
>`$USER ALL=(ALL) NOPASSWD:ALL`

<!-- # Allow members of group sudo to execute any command
#%sudo  ALL=(ALL:ALL) ALL
%sudo ALL=(ALL) NOPASSWD:ALL
# See sudoers(5) for more information on "#include" directives: -->

### clone OCR & Website Built-in code
`$ git clone https://github.com/wanarut-bda/nano-ocr.git`
### edit .zshrc file
`$ sudo nano .zshrc`
>`cd /home/jetson/nano-ocr` <br>
`git pull` <br>
`sh autorun.sh`
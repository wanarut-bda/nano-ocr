# Jetson Production Auto-Running Step
## `disable` auto-update (gui setting)
## `disable` suspend 5 minutes (gui setting)
## `enable` auto-login (gui setting)
### disable sudo password
`$ sudo nano /etc/sudoers` <br>
>\# %sudo  ALL=(ALL:ALL) ALL <br>
`%sudo ALL=(ALL) NOPASSWD:ALL`
### install zsh
`$ sudo apt install zsh nano`
### change default shell to zsh
`$ chsh -s $(which zsh)` <br>
### clone OCR & Website Built-in code
`$ git clone https://github.com/wanarut-bda/nano-ocr.git`
### edit .zshrc file
`$ sudo nano .zshrc`
>`cd /home/jetson/nano-ocr` <br>
`git pull` <br>
`sh autorun.sh`
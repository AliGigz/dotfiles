<h1 align="center">Dotfiles</h1>

<div align="center">
    <span> • </span>
    <a href="https://github.com/AliGigz/dotfiles-installation?tab=readme-ov-file#--installation">Installation</a>
    <span> • </span>
    <p></p>
</div>

<div align="center">
<img style="margine: 10px;" src="https://img.shields.io/github/contributors/AliGigz/dotfiles?style=for-the-badge&label=%EF%82%9B%20Contributors&labelColor=%231a1b26&color=%23a9b1d6" alt="Contributors">
<img style="margine: 10px" src="https://img.shields.io/github/last-commit/AliGigz/dotfiles?style=for-the-badge&label=%EF%82%9B%20Last%20Commit&labelColor=%231a1b26&color=%23a9b1d6" alt="Last Commit">
<img style="margine: 10px" src="https://img.shields.io/github/discussions/AliGigz/dotfiles?style=for-the-badge&label=%EF%82%9B%20Discussions&labelColor=%231a1b26&color=%23a9b1d6" alt="Discussions">
<img style="margine: 10px" src="https://img.shields.io/github/repo-size/AliGigz/dotfiles?style=for-the-badge&label=%EF%82%9B%20Size&labelColor=%231a1b26&color=%23a9b1d6" alt="Repo Size">
<img style="margine: 10px" src="https://img.shields.io/github/stars/AlIGigz/dotfiles?style=for-the-badge&label=%EF%82%9B%20Stars&labelColor=%231a1b26&color=%23a9b1d6" alt="Repo Stars">
</div>

## 📷  Screenshots
<div align="center">
    <h4>DWM</h4>
    <br>
    <img src="https://github.com/AliGigz/dotfiles/blob/master/screenshots/jesus-dwm.png">
    <br>
    <br>
    <img src="https://github.com/AliGigz/dotfiles/blob/master/screenshots/jesus-dwm-nvim.png">
    <br>
    <h4>BSPWM</h4>
    <br>
    <img src="https://github.com/AliGigz/dotfiles/blob/master/screenshots/bspwm-eww.png">
</div>

## 🔨  Installation

### DWM
First backup your neovim config. with the command below:
```sh
git clone https://github.com/AliGigz/dotfiles ~/.config/
```
Now remove .git, README and screenshots from the config directory. Enter command below:
```sh
rm -rf ~/.config/dotfiles/{.git,README.md,screenshots}
```
Now go to the directory of each package and make them:
```sh
cd ~/.config/dwm/ && make clean install
cd ~/.config/dmenu/ && make clean install
cd ~/.config/st/ && make clean install
cd ~/.config/slstatus/ && make clean install
```

### BSPWM
Just copy `bspwm,sxhkd,eww` to `~/.config`.

## ✏️  Colors
-   Catppuccin: https://github.com/catppuccin

## 🚀  Packages
-   dwm: https://dwm.suckless.org
-   dmenu: https://tools.suckless.org/dmenu
-   st: https://st.suckless.org
-   slstatus: https://tools.suckless.org/slstatus
-   bspwm: https://github.com/baskerville/bspwm
-   bspwm: https://github.com/baskerville/sxhkd
-   eww: https://github.com/elkowar/eww


import os,time

'''
Agregar esta linea arriba del todo en ~/.config/bspwm/bspwmrc
-   pi
'''

username = "apollo"

print('-----------------------------------------------------------')
print('---------------------ACTUALIZAR SISTEMA--------------------')
print('-----------------------------------------------------------')

os.system("sudo apt update")
os.system("sudo parrot-upgrade")
os.system("sudo apt install build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y")
os.system("sudo apt install gedit -y")
os.system("git clone https://github.com/baskerville/bspwm.git")
os.system("mv bspwm ~/Descargas")
os.system("git clone https://github.com/baskerville/sxhkd.git")
os.system("mv sxhkd ~/Descargas")
os.chdir("Descargas/bspwm/")
os.system("make")
os.system("sudo make install")
os.chdir("../sxhkd/")
os.system("make")
os.system("sudo make install")
os.system("sudo apt install bspwm -y")

print('-----------------------------------------------------------')
print('----------------------BSPWM INSTALADO----------------------')
print('-----------------------------------------------------------')

os.system('mkdir ~/.config/bspwm')
os.system('mkdir ~/.config/sxhkd')
os.chdir('../bspwm/')
os.system('cp examples/bspwmrc ~/.config/bspwm/')
os.system('chmod +x ~/.config/bspwm/bspwmrc')
os.chdir('../../autoParrot')
os.system('cp sxhkdrc ~/.config/sxhkd/')

os.system("mkdir ~/.config/bspwm/scripts/")
os.system("cp bspwm_resize ~/.config/bspwm/scripts/")
os.system("chmod +x ~/.config/bspwm/scripts/bspwm_resize")

print('-----------------------------------------------------------')
print('---------------------BSPWM CONFIGURADO---------------------')
print('-----------------------------------------------------------')


##------------
#Polybar
os.system('sudo apt install polybar -y')
##------------

print('-----------------------------------------------------------')
print('---------------------POLYBAR INSTALADO---------------------')
print('-----------------------------------------------------------')

##------------
#Picom
os.system("sudo apt update")
os.system("sudo apt install libpcre3-dev libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-dpms0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-glx0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl-dev libegl-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev meson -y")
os.chdir('../Descargas/')
os.system("git clone https://github.com/ibhagwan/picom.git")
os.chdir('picom/')
os.system('git submodule update --init --recursive')
os.system('meson setup --buildtype=release . build')
os.system('ninja -C build')
os.system('sudo ninja -C build install')
##------------

print('-----------------------------------------------------------')
print('----------------------PICOM INSTALADO----------------------')
print('-----------------------------------------------------------')

os.system("sudo apt install rofi -y")

print('-----------------------------------------------------------')
print('----------------------ROFI INSTALADO----------------------')
print('-----------------------------------------------------------')


os.system("sudo wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O /usr/local/bin/oh-my-posh")
os.system("sudo chmod +x /usr/local/bin/oh-my-posh")
os.system("mkdir ~/.poshthemes")
os.system("wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/themes.zip -O ~/.poshthemes/themes.zip")
os.system("unzip ~/.poshthemes/themes.zip -d ~/.poshthemes")
os.system("chmod u+rw ~/.poshthemes/*.omp.*")
os.system("rm ~/.poshthemes/themes.zip")
#Escoger Meslo
os.system("oh-my-posh font install")
#ingresar el tema que quieres usar en el ~/.bashrc
os.system("""echo 'eval "$(oh-my-posh init bash --config ~/.poshthemes/hunk.omp.json)"' >> ~/.bashrc""")
#comando para ver la terminal con el oh-my-posh
#os.system("exec bash")

print('-----------------------------------------------------------')
print('--------------------OH MY POSH INSTALADO-------------------')
print('-----------------------------------------------------------')

os.system('sudo apt install feh -y')
os.system('mkdir ~/Desktop/'+ username +' ~/Desktop/'+ username +'/images')
os.system('cp ~/autoParrot/fondoPantalla.jpg ~/Desktop/'+ username +'/images/')
os.system("echo 'feh --bg-fill /home/"+ username +"/Desktop/"+ username +"/images/fondoPantalla.jpg ' >> ~/.config/bspwm/bspwmrc")

#https://www.todofondos.net/downloads/fondo-de-pantalla-4k-sol-neon-para-pc/

print('-----------------------------------------------------------')
print('-----------------------FONDO COLOCADO----------------------')
print('-----------------------------------------------------------')


os.chdir('../../Descargas/')
os.system('git clone https://github.com/VaughnValle/blue-sky.git')
#os.system('mkdir ~/.config/polybar')
os.system('cp blue-sky/polybar/* -r ~/.config/polybar/')
os.system("echo '~/.config/polybar/./launch.sh' >> ~/.config/bspwm/bspwmrc")
os.system('sudo cp blue-sky/polybar/fonts/* /usr/share/fonts/truetype/')

os.system('rm ~/.config/polybar/workspace.ini')
os.system('cp ../autoParrot/workspace.ini ~/.config/polybar/')
os.system('fc-cache -v')

print('-----------------------------------------------------------')
print('----------------------POLYBAR COLOCADO---------------------')
print('-----------------------------------------------------------')

os.system('mkdir ~/.config/picom')
os.system('cp ../autoParrot/picom.conf ~/.config/picom/')
os.system("echo 'bspc config focus_follows_pointer true' >> ~/.config/bspwm/bspwmrc")
os.system("echo 'picom --experimental-backend &' >> ~/.config/bspwm/bspwmrc")
os.system("echo 'bspc config border_width 1.5' >> ~/.config/bspwm/bspwmrc")

print('-----------------------------------------------------------')
print('----------------------PICOM COLOCADO---------------------')
print('-----------------------------------------------------------')

#HASTA AQUI BIEN

os.system('mkdir ~/.config/bin')
os.system('rm -rf ~/.config/polybar/launch.sh')
os.system('rm -rf ~/.config/polybar/current.ini')
os.system('chmod +x ../autoParrot/launch.sh')
os.system('cp ../autoParrot/launch.sh ~/.config/polybar/')
os.system('cp ../autoParrot/current.ini ~/.config/polybar/')

os.system('cp ../autoParrot/ethernet_status.sh ~/.config/bin/')
os.system('cp ../autoParrot/htb_status.sh ~/.config/bin/')
os.system('cp ../autoParrot/target_to_hack.sh ~/.config/bin/')
os.system('chmod +x ~/.config/bin/ethernet_status.sh')
os.system('chmod +x ~/.config/bin/htb_status.sh')
os.system('chmod +x ~/.config/bin/target_to_hack.sh')

os.system('mkdir ~/.config/bin/target')
os.system('touch ~/.config/bin/target/target.txt')
os.system("echo 'function settarget(){' >> ~/.bashrc")
os.system("echo '    ip_address=$1' >> ~/.bashrc")
os.system("echo '    machine_name=$2' >> ~/.bashrc")
os.system("""echo '    echo "$ip_address $machine_name" > /home/apollo/.config/bin/target/target.txt' >> ~/.bashrc""")
os.system("echo '}' >> ~/.bashrc")
#os.system("echo 'xsetroot -cursor_name left_ptr &' >> ~/.config/bspwm/bspwmrc")

os.system("mkdir -p ~/.config/rofi/themes")
os.system("cp ~/Descargas/blue-sky/nord.rasi ~/.config/rofi/themes")

os.system("wget https://github.com/sharkdp/bat/releases/download/v0.22.1/bat_0.22.1_amd64.deb")
os.system('sudo dpkg -i bat_0.22.1_amd64.deb')
os.system("echo '#Custom Aliases' >> ~/.bashrc")
os.system("echo 'alias cat='/bin/bat'' >> ~/.bashrc")
os.system("echo 'alias catn='/bin/cat'' >> ~/.bashrc")
os.system("echo 'alias catnl='/bin/bat --paging=never'' >> ~/.bashrc")

os.system('update-alternatives --config java')

os.system('sudo apt install wmname -y')
os.system("sudo apt install ranger -y")

os.system("sudo apt-get install gedit -y") if os.system("gedit --version") else None
os.system("sudo apt-get install ffuf -y") if os.system("ffuf --version") else None
os.system("sudo apt-get install wpscan -y") if os.system("wpscan --version") else None
os.system("sudo apt-get install sqlmap -y") if os.system("sqlmap --version") else None
os.system("sudo apt-get install hash-identifier -y")
os.system("sudo apt-get install sublist3r -y") if os.system("sublist3r --version") else None

if os.path.exists("Downloads/tools"):
    pass
else:
    os.system("mkdir ~/Downloads/tools")
    time.sleep(1)
    os.system("wget https://github.com/carlospolop/PEASS-ng/releases/tag/20230101/linpeas.sh -P ~/Downloads/tools/")
    time.sleep(1)
    os.system("wget https://github.com/carlospolop/PEASS-ng/releases/tag/20230101/winPEASx64.exe -P ~/Downloads/tools/")
    os.system("mv ~/Downloads/tools/winPEASx64.exe ~/Downloads/tools/winpeas.exe")
    
os.system('python3 ~/autoParrot/firefoxInstall.py')

os.system('rofi-theme-selector')
os.system('exec bash')
import subprocess

'''
Esto se ejecuta la primera vez que realizas la instalacion de Parrot
ESTO NO ES PARA ACTUALIZAR FIREFOX
Actualizar firefox es distinto y tiene que ser manual

Reemplazar los 'apollo' por el nombre de usuario de sus maquinas

ACTUALIZAR EL NOMBRE DEL FIREFOX QUE INSTALEN DE LA PAGINA OFICIAL
LINK = https://www.mozilla.org/es-ES/firefox/new/
Instalar el firefox en la carpeta Descargas
'''
username = "apollo"
firefox_f = "firefox-110.0.1.tar.bz2"

print('-----------------------------------------------------------')
print('---------------------ASIGNANDO PERMISOS--------------------')
print('-----------------------------------------------------------')

subprocess.run(['sudo', 'chown', f'{username}:{username}', '../../opt/'])

print('-----------------------------------------------------------')
print('---------------------INSTALANDO FIREFOX--------------------')
print('-----------------------------------------------------------')

subprocess.run(['sudo','-u','apollo','mv', f'/home/{username}/Descargas/{firefox_f}', '../../opt'])
subprocess.run(['sudo','-u','apollo','tar', '-xjf', f'../../opt/{firefox_f}','-C','/opt/'])
subprocess.run(['sudo','-u','apollo','rm', f'../../opt/{firefox_f}'])

print('-----------------------------------------------------------')
print('---------------------FIREFOX INSTALADO---------------------')
print('-----------------------------------------------------------')

# instalar firejail con apt
subprocess.run(['sudo', 'apt', 'install', 'firejail', '-y'])

print('-----------------------------------------------------------')
print('---------------------FIREJAIL INSTALADO--------------------')
print('-----------------------------------------------------------')

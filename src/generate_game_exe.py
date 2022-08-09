import os
import shutil
import PyInstaller.__main__


game_path = 'game.py'

PyInstaller.__main__.run([
    game_path,
    '--name=pacman',
    '--onefile',
    '--windowed'
])

shutil.move('dist/pacman.exe', 'pacman.exe')
os.remove('pacman.spec')
os.rmdir('dist')
shutil.rmtree('build')

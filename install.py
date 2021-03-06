# install script from within the repository. don't forget to create a virtual env or use anaconda!

import sys
import os
from shutil import copyfile

root_location = sys.exec_prefix
install_location = "lib/python3.7/site-packages/retro/data/stable"

full_install_location = os.path.join(root_location, install_location)
full_install_location = os.path.abspath(full_install_location)
full_install_location = os.path.join(full_install_location, "NbaJamTE-Snes")

retro_install_cmd = 'python -m retro.import rom' 

current_location = os.getcwd()

nba_jam_file_location = "nba_jam_retro_gym"
nba_jam_file_location = os.path.join(current_location, nba_jam_file_location)

files_to_copy = ["data.json",
                 "lakers-pacers-peeler-divac.state",
                 "metadata.json",
                 "reward.json",
                 "rom.sha",
                 "scenario.json"]

print(full_install_location)
if (os.path.exists(full_install_location)):
    print('Folder exits. Rewriting files')
else:
    os.mkdir(full_install_location)
for i in files_to_copy:
    copyfile(os.path.join(nba_jam_file_location, i), os.path.join(full_install_location, i))

os.system(retro_install_cmd)

#
# Copyright (c) 2020 Andrew Cottam.
#
# This file is part of marxanweb/general
# (see https://github.com/marxanweb/general).
#
# License: European Union Public Licence V. 1.2, see https://opensource.org/licenses/EUPL-1.2
#
import batchHelpers
from batchHelpers import Registry
#run with:
#python -W ignore update_database.py 

#create a new Registry object
reg = Registry()
#iterate through the Marxan Servers
for server in reg.MarxanServers:
    longest = sorted([len(m.name) for m in reg.MarxanServers])[-1]
    print(server.name + ((longest - len(server.name)) + 5) * " ", end=' ', flush=True )
    try:
        server.authenticate()
    except Exception as e:
        pass
    else:
        server.runSQL('/home/ubuntu/environment/marxanweb/general/client-apps/server-management/update.sql')
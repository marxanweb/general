import batchHelpers
from batchHelpers import Registry

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
        server.runSQL('/home/ubuntu/environment/marxanweb/general/client-apps/batch-requests/update.sql')
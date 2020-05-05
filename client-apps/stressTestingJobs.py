JOB_00 = [
    ("GET",'getProjects?user=admin'),
    ("GET",'getProjects?user=jennifer'),
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
];
JOB_01 = [
    #if you start and stop this you get task pending and unclosed connection errors on the server
    ("GET",'getProjects?user=admin'),
    ("GET",'getProjects?user=jennifer'),
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
    ("WebSocket",'runMarxan?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'runMarxan?user=admin&project=Coral%20Triangle%20Case%20Study'),
    ("WebSocket",'runMarxan?user=admin&project=Fiji%20NBSAP'),
    ("WebSocket",'runMarxan?user=admin&project=Tonga%20Marine%20NBSAP'),
    ("WebSocket",'runMarxan?user=andrew&project=Start%20project'),
    ("WebSocket",'runMarxan?user=andrew&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'preprocessFeature?user=andrew&project=Start%20project&planning_grid_name=pu_ton_marine_hexagon_50&feature_class_name=volcano&alias=volcano&id=63408475'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=110&shape=hexagon'),
    ("WebSocket",'preprocessPlanningUnits?user=admin2&project=Start%20project'),
    ("WebSocket",'preprocessPlanningUnits?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=100&shape=hexagon'),
];
JOB_02 = [
    #if you start and stop this you get task pending and unclosed connection errors on the server
    ("GET",'getProjects?user=admin'),
    ("GET",'getProjects?user=jennifer'),
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
    ("WebSocket",'runMarxan?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'runMarxan?user=admin&project=Coral%20Triangle%20Case%20Study'),
    ("WebSocket",'runMarxan?user=admin&project=Fiji%20NBSAP'),
    ("WebSocket",'runMarxan?user=admin&project=Tonga%20Marine%20NBSAP'),
    ("WebSocket",'runMarxan?user=andrew&project=Start%20project'),
    ("WebSocket",'runMarxan?user=andrew&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'preprocessFeature?user=andrew&project=Start%20project&planning_grid_name=pu_ton_marine_hexagon_50&feature_class_name=volcano&alias=volcano&id=63408475'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=110&shape=hexagon'),
    ("WebSocket",'preprocessPlanningUnits?user=admin2&project=Start%20project'),
    ("WebSocket",'preprocessPlanningUnits?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'preprocessProtectedAreas?user=admin&project=Start%20project&planning_grid_name=pu_ton_marine_hexagon_50'),
    ("WebSocket",'runGapAnalysis?user=admin&project=Start%20project'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=100&shape=hexagon'),
];
JOB_03 = [
    #if you start and stop this you get task pending and unclosed connection errors on the server
    ("GET",'getProject?user=admin&project=Start%20project'),
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
    ("WebSocket",'runMarxan?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'runMarxan?user=admin&project=Coral%20Triangle%20Case%20Study'),
    ("WebSocket",'preprocessFeature?user=andrew&project=Start%20project&planning_grid_name=pu_ton_marine_hexagon_50&feature_class_name=volcano&alias=volcano&id=63408475'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=110&shape=hexagon'),
    ("WebSocket",'preprocessPlanningUnits?user=admin2&project=Start%20project'),
    ("WebSocket",'preprocessPlanningUnits?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=100&shape=hexagon'),
];
JOB_04 = [
    #if you start and stop this you get task pending and unclosed connection errors on the server - if you're quick!
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
    ("WebSocket",'runMarxan?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'preprocessFeature?user=andrew&project=Start%20project&planning_grid_name=pu_ton_marine_hexagon_50&feature_class_name=volcano&alias=volcano&id=63408475'),
    ("WebSocket",'preprocessPlanningUnits?user=admin2&project=Start%20project'),
    ("WebSocket",'preprocessPlanningUnits?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=100&shape=hexagon'),
];
JOB_05 = [
    #if you start and stop this you get task pending and unclosed connection errors on the server - if you're quick!
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
    ("WebSocket",'runMarxan?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'preprocessPlanningUnits?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=100&shape=hexagon'),
];
JOB_06 = [
    #if you start and stop this you get task pending and unclosed connection errors on the server - if you're quick!
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
    ("WebSocket",'preprocessPlanningUnits?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=100&shape=hexagon'),
];
JOB_07 = [
    #doesnt raise task pending and unclosed connection errors on the server
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
    ("WebSocket",'preprocessPlanningUnits?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
];
JOB_08 = [
    #yes!!! task pending and unclosed connection errors on the server
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=100&shape=hexagon'),
];
JOB_09 = [
    #doesnt raise task pending and unclosed connection errors on the server
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=100&shape=hexagon'),
];
JOB_10 = [
    #doesnt raise task pending and unclosed connection errors on the server
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
];
JOB_11 = [
    #yes errors
    ("GET",'deletePlanningUnitGrid?planning_grid_name=pu_arg_terrestrial_hexagon_110'),
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
    ("WebSocket",'runMarxan?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'runMarxan?user=admin&project=Coral%20Triangle%20Case%20Study'),
    ("WebSocket",'preprocessFeature?user=andrew&project=Start%20project&planning_grid_name=pu_ton_marine_hexagon_50&feature_class_name=volcano&alias=volcano&id=63408475'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=110&shape=hexagon'),
    ("WebSocket",'preprocessPlanningUnits?user=admin2&project=Start%20project'),
    ("WebSocket",'preprocessPlanningUnits?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
];
JOB_12 = [
    #yes errors
    ("GET",'deletePlanningUnitGrid?planning_grid_name=pu_arg_terrestrial_hexagon_110'),
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
    ("WebSocket",'runMarxan?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'runMarxan?user=admin&project=Coral%20Triangle%20Case%20Study'),
    ("WebSocket",'preprocessFeature?user=andrew&project=Start%20project&planning_grid_name=pu_ton_marine_hexagon_50&feature_class_name=volcano&alias=volcano&id=63408475'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=110&shape=hexagon'),
    ("WebSocket",'preprocessPlanningUnits?user=admin&project=Start%20project'),
    ("WebSocket",'preprocessPlanningUnits?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
];
JOB_13 = [
#yes when there were 2 idel postgres processes
    ("GET",'deletePlanningUnitGrid?planning_grid_name=pu_arg_terrestrial_hexagon_110'),
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
    ("WebSocket",'preprocessFeature?user=andrew&project=Start%20project&planning_grid_name=pu_ton_marine_hexagon_50&feature_class_name=volcano&alias=volcano&id=63408475'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=110&shape=hexagon'),
    ("WebSocket",'preprocessPlanningUnits?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
];
JOB_14 = [
#1 no after restarting marxan-server and starting the run after a couple of minutes
#2 no after restarting marxan-server and starting the run straight away
#3 yes after restarting marxan-server and starting the run straight away
#4 no
#5 no
#6 yes
#7 yes
#8 no
#9 yes and immediately closed the createPlanningUnitGrid
#10 no
    ("GET",'deletePlanningUnitGrid?planning_grid_name=pu_arg_terrestrial_hexagon_110'),
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
    ("WebSocket",'preprocessFeature?user=andrew&project=Start%20project&planning_grid_name=pu_ton_marine_hexagon_50&feature_class_name=volcano&alias=volcano&id=63408475'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=110&shape=hexagon'),
];
JOB_15 = [
#1 yes and with this error
# [E 02-05-20 08:19:59.942] Uncaught exception GET /marxan-server/preprocessFeature?user=andrew&project=Start%20project&planning_grid_name=pu_ton_marine_hexagon_50&feature_class_name=volcano&alias=volcano&id=63408475 (78.134.66.124)
#     HTTPServerRequest(protocol='https', host='andrewcottam.com:443', method='GET', uri='/marxan-server/preprocessFeature?user=andrew&project=Start%20project&planning_grid_name=pu_ton_marine_hexagon_50&feature_class_name=volcano&alias=volcano&id=63408475', version='HTTP/1.1', remote_ip='78.134.66.124')
#     Traceback (most recent call last):
#       File "/home/a_cottam/miniconda3/lib/python3.7/site-packages/tornado/web.py", line 1699, in _execute
#         result = await result
#       File "/home/a_cottam/miniconda3/lib/python3.7/site-packages/tornado/websocket.py", line 278, in get
#         await self.ws_connection.accept_connection(self)
#       File "/home/a_cottam/miniconda3/lib/python3.7/site-packages/tornado/websocket.py", line 881, in accept_connection
#         await self._accept_connection(handler)
#       File "/home/a_cottam/miniconda3/lib/python3.7/site-packages/tornado/websocket.py", line 964, in _accept_connection
#         await self._receive_frame_loop()
#       File "/home/a_cottam/miniconda3/lib/python3.7/site-packages/tornado/websocket.py", line 1118, in _receive_frame_loop
#         await self._receive_frame()
#       File "/home/a_cottam/miniconda3/lib/python3.7/site-packages/tornado/websocket.py", line 1130, in _receive_frame
#         data = await self._read_bytes(2)
#       File "/home/a_cottam/miniconda3/lib/python3.7/site-packages/tornado/websocket.py", line 1124, in _read_bytes
#         data = await self.stream.read_bytes(n)
#       File "/home/a_cottam/miniconda3/lib/python3.7/site-packages/tornado/iostream.py", line 441, in read_bytes
#         self._try_inline_read()
#       File "/home/a_cottam/miniconda3/lib/python3.7/site-packages/tornado/iostream.py", line 831, in _try_inline_read
#         pos = self._read_to_buffer_loop()
#       File "/home/a_cottam/miniconda3/lib/python3.7/site-packages/tornado/iostream.py", line 761, in _read_to_buffer_loop
#         if self._read_to_buffer() == 0:
#       File "/home/a_cottam/miniconda3/lib/python3.7/site-packages/tornado/iostream.py", line 856, in _read_to_buffer
#         bytes_read = self.read_from_fd(buf)
#       File "/home/a_cottam/miniconda3/lib/python3.7/site-packages/tornado/iostream.py", line 1586, in read_from_fd
#         return self.socket.recv_into(buf, len(buf))
#       File "/home/a_cottam/miniconda3/lib/python3.7/ssl.py", line 1052, in recv_into
#         return self.read(nbytes, buffer)
#       File "/home/a_cottam/miniconda3/lib/python3.7/ssl.py", line 911, in read
#         return self._sslobj.read(len, buffer)
#     ssl.SSLError: [SSL] shutdown while in init (_ssl.c:2488)
#2 yes
#3 no
#4 yes - createPlanningUnitGrid terminated
#5 no
#6 yes - deletePlanningUnitGrid terminated
#7 yes - createPlanningUnitGrid terminated
#8 no
#9 no
#10 yes
    ("GET",'deletePlanningUnitGrid?planning_grid_name=pu_arg_terrestrial_hexagon_110'),
    ("WebSocket",'preprocessFeature?user=andrew&project=Start%20project&planning_grid_name=pu_ton_marine_hexagon_50&feature_class_name=volcano&alias=volcano&id=63408475'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=110&shape=hexagon'),
];
JOB_16 = [
#1 no
#2 no
#3 no or 4,5,6
    ("GET",'deletePlanningUnitGrid?planning_grid_name=pu_arg_terrestrial_hexagon_110'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=110&shape=hexagon'),
];
JOB_17 = [
#no errors where i didnt restart the marxan-server
#then when i restarted it - error in createPlanningUnitGrid
#2 yes - preprocessPlanningUnits stopped
#3 no
#4 no
#5 yes - deletePlanningUnitGrid stopped and the client had a timeout error after 20s
    ("GET",'deletePlanningUnitGrid?planning_grid_name=pu_arg_terrestrial_hexagon_300'),
    ("WebSocket",'preprocessFeature?user=andrew&project=Start%20project&planning_grid_name=pu_ton_marine_hexagon_50&feature_class_name=volcano&alias=volcano&id=63408475'),
    ("WebSocket",'createPlanningUnitGrid?iso3=ARG&domain=Terrestrial&areakm2=300&shape=hexagon'),
];
JOB_18 = [
#no errors in 10 tests
    ("WebSocket",'runMarxan?user=admin&project=Start%20project'),
    ("WebSocket",'runMarxan?user=admin&project=British%20Columbia%20Marine%20Case%20Study'),
    ("WebSocket",'runMarxan?user=admin&project=Coral%20Triangle%20Case%20Study'),
];
JOB_19 = [
    ("WebSocket",'runMarxan?user=USER&project=PROJECT'),
];

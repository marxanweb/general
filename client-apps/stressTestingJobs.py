LOGIN_USER = "admin"
LOGIN_PASSWORD = "password"
JOB_01 = [
    ("GET",'getProjects?user=' + LOGIN_USER), 
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
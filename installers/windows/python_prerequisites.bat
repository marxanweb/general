CALL conda.bat create --name marxan -y
CALL conda.bat activate marxan
"%~dp0\Miniconda3\Scripts\conda" install -y tornado psycopg2 pandas gdal colorama psutil
"%~dp0Miniconda3\Scripts\pip" install mapbox -q
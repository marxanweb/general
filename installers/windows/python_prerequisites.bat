CALL conda.bat activate base
"%~dp0Miniconda3\Scripts\conda" install -y tornado psycopg2 pandas gdal colorama psutil sqlalchemy 
"%~dp0Miniconda3\Scripts\pip" install mapbox -q

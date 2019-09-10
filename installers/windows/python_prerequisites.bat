CALL conda.bat activate base
"%~dp0\Miniconda3\Scripts\conda" install -y tornado psycopg2 pandas gdal colorama
"%~dp0Miniconda3\Scripts\pip" install mapbox -q
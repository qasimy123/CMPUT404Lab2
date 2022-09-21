python proxyserver.py &
PID=$!

python proxyclient.py & 
python proxyclient.py & 
python proxyclient.py & 
python proxyclient.py & 
kill $PID
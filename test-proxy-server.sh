python proxyserver.py &
PID=$!
sleep 1
python proxyclient.py & 
PID2=$!
python proxyclient.py & 
PID3=$!
python proxyclient.py & 
PID4=$!
python proxyclient.py & 
PID5=$!
# wait for all the clients to finish
wait $PID2
wait $PID3
wait $PID4
wait $PID5
# kill the server
kill $PID



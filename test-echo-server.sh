python echoserver.py &
PID=$!
sleep 1
echo "Foobar1" | nc localhost 8001 -q 1 & 
PID2=$!
echo "Foobar2" | nc localhost 8001 -q 1 & 
PID3=$!
echo "Foobar3" | nc localhost 8001 -q 1 & 
PID4=$!
echo "Foobar4" | nc localhost 8001 -q 1 & 
PID5=$!
# wait for all the clients to finish
wait $PID2
wait $PID3
wait $PID4
wait $PID5
# kill the server
kill $PID



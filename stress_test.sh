
curl -s "http://54.193.1.16:5000?[1-300]" &
pidlist="$pidlist $!" 
curl -s "http://54.193.1.16:5000?[1-300]" &
pidlist="$pidlist $!" 
curl -s "http://54.193.1.16:5000?[1-300]" &
pidlist="$pidlist $!" 
curl -s "http://54.193.1.16:5000?[1-300]" &
pidlist="$pidlist $!" 
curl -s "http://54.193.1.16:5000?[1-300]" &
pidlist="$pidlist $!" 
curl -s "http://54.193.1.16:5000?[1-300]" &
pidlist="$pidlist $!" 
curl -s "http://54.193.1.16:5000?[1-300]" &
pidlist="$pidlist $!"  

for job in $pidlist do 
  echo $job     
  wait $job || let "FAIL+=1" 
done  

if [ "$FAIL" == "0" ]; then 
  echo "YAY!" 
else 
  echo "FAIL! ($FAIL)" 
fi
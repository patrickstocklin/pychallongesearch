HTTPSTATUS=`curl -s -o /dev/null -L -w "%{http_code}" -H "Accept: application/json" -H "Content-type: application/json" http://localhost:9200/_cluster/health`
if [ $HTTPSTATUS -eq 200 ]; then
  echo "Healthy Cluster"
fi
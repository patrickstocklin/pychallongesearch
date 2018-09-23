#How to kill
pid=$(cat /tmp/elasticsearch-pid && echo)
echo "Shutting down Elasticsearch Cluster"
kill -SIGTERM $pid
deactivate

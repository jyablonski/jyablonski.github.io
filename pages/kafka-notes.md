title: Kafka Notes
date: 2022-04-03
description: Personal Kafka Notes

`docker-compose run mzcli`

`exit` to exit the cli

\timing to activate timing

press `q` to exit a terminal end view.

`CREATE MATERIALIZED VIEW mv_stream_15min AS` is a sliding window, 15 minutes wide, that will automatically
get rid of 15 min old data and keep the present stuff, without you needing to rerun the query every time to do that.

`http://localhost:6875/hierarchical-memory`


CREATE TABLE twitch_data_1 (game_id string, game_name string, id string, viewer_count int);

https://python-twitch-client.readthedocs.io/en/latest/
https://github.com/tsifrer/python-twitch-client
https://github.com/confluentinc/confluent-kafka-python

helix is newer, api v5 is older for twitch

CREATE table mv_agg_stream_game AS
SELECT game_id,
       game_name,
       COUNT(id) AS cnt_streams,
       SUM(viewer_count) AS agg_viewer_cnt
FROM v_twitch_stream
WHERE game_id IS NOT NULL
GROUP BY game_id, game_name;

create table mv_agg_stream_game_table (game_id string, game_name string, cnt_streams string, agg_viewer_cnt int);

COPY (SELECT * FROM mv_agg_stream_game) TO STDOUT;


#### The actual project
Kafka is just built w/ docker-compose.  It needs Zookeeper for synchronization & node status purposes and it also keeps track of kafka topics, partitions etc.

Zookeeper storse metadata about the location of the partitions and configuration of the topics.  This 2 part system leads to duplication, leading to additional complexity and more network communication, security, and monitoring that is required.  And when a new kafka cluster must be elected to the leader, the controller has to load the full state of the cluster from zookeeper, so as metadata grows this process takes longer.  There is also de-sync issues to worry about, where the 2 systems "diverge" in state.

Then there are 2 python containers.  1 is a generator, 1 is a consumer.

The producer creates a topic called twitch-streams and connects to the Twitch Helix API to start retrieving data from there, encoding it, and sending it to the Kafka Topic.

The consumer reads from that topic, decodes the message, aggregates the messages, turns them into a Pandas DataFrame instead of staying in JSON, and then writes to SQL for permanent storage.

The Kafka offset is how to keep track of what messages consumers have seen, incase a consumer stops then boots back up again.  It's a pointer to the last message read or consumed by a consumer.

There are various schools of thought in terms of how to handle the offset.  
https://dzone.com/articles/kafka-clients-at-most-once-at-least-once-exactly-o
    * At Least Once
      * The easiest, messages can be duplicated so teh consumer has to be able to deal with that.  There should be idempotent behavior downstream.
    * At Most Once
      * Chance messages might not actually ever make it.
    * Exactly Once
      * The most difficult to implement

`json.dump` turns a python dictioanry into a str object.
`json.load` loads a str object into a python dictionary.
utf-8 encoding is then used to serialize this str object and send it to Kafka
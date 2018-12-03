import json

data = {
	"connections": [{
		"producer_process_name": "node_1",
		"consumer_process_name": "node_2",
		"content_type": "ROSMSG",
		"content_name": "Msg1"
	},
	{
		"producer_process_name": "node_2",
		"consumer_process_name": "node_3",
		"content_type": "ROSMSG",
		"content_name": "Msg2"
	},
	{
		"producer_process_name": "node_3",
		"consumer_process_name": "node_1",
		"content_type": "ROSMSG",
		"content_name": "Msg3"
	}]
}

#json_dump = json.dump(data)
with open('data.json','w') as outfile:
	json.dump(data, outfile)
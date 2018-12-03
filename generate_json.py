import json

simple_data = {
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

data_with_components = {
	"connections": [{
		"producer_process_name": "node_11",
		"producer_process_component": "C1",
		"consumer_process_name": "node_12",
		"consumer_process_component": "C1",
		"content_type": "ROSMSG",
		"content_name": "Msg1"
	},
	{
		"producer_process_name": "node_21",
		"producer_process_component": "C2",
		"consumer_process_name": "node_22",
		"consumer_process_component": "C2",
		"content_type": "ROSMSG",
		"content_name": "Msg1"
	},
	{
		"producer_process_name": "node_31",
		"producer_process_component": "C3",
		"consumer_process_name": "node_32",
		"consumer_process_component": "C3",
		"content_type": "ROSMSG",
		"content_name": "Msg1"
	},
	{
		"producer_process_name": "node_31",
		"producer_process_component": "C3",
		"consumer_process_name": "node_22",
		"consumer_process_component": "C2",
		"content_type": "ROSMSG",
		"content_name": "Msg1"
	},
	{
		"producer_process_name": "node_31",
		"producer_process_component": "C3",
		"consumer_process_name": "node_11",
		"consumer_process_component": "C1",
		"content_type": "ROSMSG",
		"content_name": "Msg1"
	},
	{
		"producer_process_name": "node_22",
		"producer_process_component": "C2",
		"consumer_process_name": "node_11",
		"consumer_process_component": "C1",
		"content_type": "ROSMSG",
		"content_name": "Msg1"
	},
	{
		"producer_process_name": "node_12",
		"producer_process_component": "C1",
		"consumer_process_name": "node_22",
		"consumer_process_component": "C2",
		"content_type": "ROSMSG",
		"content_name": "Msg1"
	},
	{
		"producer_process_name": "node_31",
		"producer_process_component": "C3",
		"consumer_process_name": "node_12",
		"consumer_process_component": "C1",
		"content_type": "ROSMSG",
		"content_name": "Msg1"
	}]
}

with open('data.json','w') as outfile:
	json.dump(data_with_components, outfile)
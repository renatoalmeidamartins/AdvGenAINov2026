# Use the native inference API to send a text message to Amazon Titan Text.

import boto3
import json

from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

#model_id = "amazon.nova-pro-v1:0"
model_id = "global.anthropic.claude-sonnet-4-6" 

# Define the prompt for the model.
prompt = "Write an image resizing program in Python. Give me detailed explanation of how it works."


def parse_nova_lite_response(response_body):
    """Parse the response from Nova Lite."""
    if 'output' in response_body and 'message' in response_body['output']:
        message = response_body['output']['message']
        if 'content' in message and isinstance(message['content'], list):
            # Extract text from each content item
            texts = []
            for content_item in message['content']:
                if isinstance(content_item, dict) and 'text' in content_item:
                    texts.append(content_item['text'])
            return ' '.join(texts)
    
    # Fallback if the response format is different
    return str(response_body)

# Format the request payload using the model's native structure.
native_request = {
       "messages": [
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 10000,
            "temperature": 0,
            "topP": 0.9
        }
}


# Convert the native request to JSON.
request = json.dumps(native_request)

# # regular invoke
# try:
#     # Invoke the model with the request.
#     response = client.invoke_model(modelId=model_id, body=request)

# except (ClientError, Exception) as e:
#     print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
#     exit(1)

# # Regular, non-streamed response
# # Decode the response body.
# model_response = json.loads(response["body"].read())
# response_text = parse_nova_lite_response(model_response)
# print(response_text)


# invoking as a stream
try:
    # Invoke the model with the request.
    response = client.invoke_model_with_response_stream(modelId=model_id, body=request)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)

stream = response.get('body')

for event in stream:
    chunk = event.get('chunk')
    if chunk:
        chunk_obj = json.loads(chunk.get('bytes').decode())
        # Extract text from Nova Lite's response format
        if 'contentBlockDelta' in chunk_obj and 'delta' in chunk_obj['contentBlockDelta']:
            text = chunk_obj['contentBlockDelta']['delta'].get('text', '')
            print(text)
            #output.append(text)



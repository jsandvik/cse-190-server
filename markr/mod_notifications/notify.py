from Pubnub import Pubnub

## Initiate Class
pubnub = Pubnub( publish_key='pub-c-0e4726e8-2544-41f3-9cad-48cedc7a026a', subscribe_key='sub-c-5c598d92-d344-11e3-a531-02ee2ddab7fe', ssl_on=False )

## Publish Example
info = pubnub.publish({
    'channel' : 'hello_world',
    'message' : {
        'some_text' : 'Hello my World'
    }
})
print(info)

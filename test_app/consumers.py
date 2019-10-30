# In consumers.py
from channels import Group, Channel
from channels.sessions import channel_session
import json
from channels.auth import channel_session_user, channel_session_user_from_http, http_session_user

# Connected to websocket.connect
@http_session_user
@channel_session_user_from_http
@channel_session
def ws_connect(message):
    # Accept connection
    message.reply_channel.send({"accept": True})
    # Work out room name from path (ignore slashes)
    #print message.http_session.items()
    room = message.content['path'].strip("/")+str(message.http_session.get('lecture_id'))
    #import pdb; pdb.set_trace();
    print message.keys(), room      
    # Save room in session and add us to the group
    message.channel_session['room'] = room
    message.channel_session['user'] = message.http_session.get('username')
    Group("chat-%s" % room).add(message.reply_channel)

# Connected to websocket.receive
@channel_session
def ws_message(message):
    #print message.channel_session['room'], message['text']
    #import pdb; pdb.set_trace();
    
    #print message.keys(), message.get('method'), message.reply_channel, message.get('path'), message.get('order'), message.get('reply_channel')
    Group("chat-%s" % message.channel_session['room']).send({
        "text": message.channel_session['user']+ ": "+message['text'],
    })

# Connected to websocket.disconnect
@http_session_user
@channel_session_user_from_http
@channel_session
def ws_disconnect(message):
    #import pdb; pdb.set_trace();
    Group("chat-%s" % message.channel_session['room']).discard(message.reply_channel)

from nose.tools import *
from app import app
from tests.tools import assert_response

client = app.test_client() # create a testing client (a fake browser)
client.testing = True # enable this so that exceptions in your code bubble up to the test client

def test_index():
    global clientresp
    resp = client.get('/') # with this client you can do all kinds of stuff
    assert_response(resp, status=302) # the root url should give back a redirect

    resp = client.get('/game')
    assert_response(resp, status=200) # just make sure we got a valid response

    resp = client.post('/game') # use POST, but provide no data
    assert_response(resp, contains="You Died!")

    # Scene: tell a joke
    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Laser Weapon Armory")

    # From there, go to yet another scene
    testdata = {'userinput': '132'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="The Bridge")

    testdata = {'userinput': 'slowly place the bomb'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Escape Pod")

    testdata = {'userinput': 'throw the bomb'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Death")

    testdata = {'userinput': '2'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="You made it!")

    testdata = {'userinput': '*'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="...")

    # Scene: shoot
    testdata = {'userinput': 'shoot'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="One bullet to go")

    # From there, go to yet another scene
    testdata = {'userinput': 'left'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="You have control")

    testdata = {'userinput': 'right'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="You got tied")

    testdata = {'userinput': 'laser weapon armory'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Laser Weapon Armory")

    testdata = {'userinput': 'home'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="...")

    testdata = {'userinput': 'first drawer'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="You have control")

    testdata = {'userinput': 'second drawer'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Phone")

    testdata = {'userinput': '112'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Death")

    testdata = {'userinput': '648394794801'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Head Quarter has control")

    testdata = {'userinput': 'third drawer'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Death")

    # Scene: dodge
    testdata = {'userinput': 'dodge'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Welcome to Magic Island")

    # From there, go to yet another scene
    testdata = {'userinput': 'apples'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Healthy again")

    testdata = {'userinput': 'leave'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Escape Pod")

    testdata = {'userinput': 'stay'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="...")

    testdata = {'userinput': 'mushrooms'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="You got some magic power")

    testdata = {'userinput': 'central corridor'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Central Corridor")

    testdata = {'userinput': 'island'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Welcome to Magic Island")

    testdata = {'userinput': 'unfinished proper meal'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Death")

from app.main import foo

def test_foo():
    assert foo('bar') == 'foobar'

def test_false_foo():
    assert foo('foo') != 'foobar'


from babs_package.lib import days_left, try_me

def test_try_me():
    assert try_me() != ""
    assert type(days_left()) == str
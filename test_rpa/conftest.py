import pytest


@pytest.fixture(scope='session')
def get_headers():
    headers = {
        'Authorization': "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxIiwiZXhwIjoxNTgzMTQ3MTM5LCJ1c2VySWQiOjEsImlhdCI6MTU4MzEzOTkzOSwiYWNjb3VudCI6ImFkbWluIiwidXNlcktleSI6Inh4eHgifQ.u6vphh-zSBF1ymuIhCH2NgwPVpa8L9cTEJoDor2OdvLR3b7ZaLCjiIVSGJZpInRgAgZ8kN9OJGWPEcdgHEAEhA",
        'x-access-token': 'yJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxIiwiZXhwIjoxNTgzMTQ3MTM5LCJ1c2VySWQiOjEsImlhdCI6MTU4MzEzOTkzOSwiYWNjb3VudCI6ImFkbWluIiwidXNlcktleSI6Inh4eHgifQ.u6vphh-zSBF1ymuIhCH2NgwPVpa8L9cTEJoDor2OdvLR3b7ZaLCjiIVSGJZpInRgAgZ8kN9OJGWPEcdgHEAEhA'
        }
    yield headers
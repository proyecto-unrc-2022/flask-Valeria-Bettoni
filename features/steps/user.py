import json
from behave import *
from application import USERS

@given('some users are in the system')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})

@when(u'I retrieve the customer \'jasonb\'')
def step_impl(context):
    context.page = context.client.get('/users/{}'.format('jasonb'))
    assert context.page

@then(u'I should get a \'200\' response')
def step_impl(context):
    assert context.page.status_code is 200

@then(u'the following user details are returned')
def step_impl(context):
    # assert context.table[0].cells[0] in context.page.text
    assert "Jason Bourne" in context.page.text

#----------------------------------------------------------------------
# Scenario: Add new user
@given('a user that is not in the system')
def step_impl(context):
    user_in = USERS.get('katyp', 'Not in')
    assert user_in is 'Not in'

@when(u'add the new user \'Katy Perry\'')
def step_impl(context):
    body = {'katyp':{'name': 'Katy Perry'}}
    headers = {'Content-Type': 'application/json'}
    context.res = context.client.post('/users/logguser', data=json.dumps(body), headers=headers)
    print(context.res.text)
    assert context.res

@then(u'get a \'200\' response')
def step_impl(context):
    assert context.res.status_code is 200

@then(u'the following user are returned')
def step_impp(context):
    assert "Katy Perry" in context.res.text

#----------------------------------------------------------------------
# Scenario: Update a user from USERS
@given('A list of users and a new data from users')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})
    context.user_info = json.dumps({'name': 'Jhon Bourne'})
    context.headers = {'Content-Type': 'application/json'}
    context.url = '/users/update/{}'.format('jasonb')

@when('I update customer')
def step_impl(context):
    context.page = context.client.put(context.url, data=context.user_info, headers = context.headers)
    assert context.page

@then('I should get a \'200\' response')
def step_impl(context):
    print("code = ", context.page.status_code)
    assert context.page.status_code is 200

@then('update user details are returned')
def step_impl(context):
    assert 'Jhon Bourne' in context.page.text

#----------------------------------------------------------------------
# Scenario: Delete a existing user
@given('A list of users and a user to delete')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})
    USERS.update({'jhonL': {'name': 'Jhon Lenon'}})
    context.headers= {'Content-Type': 'application/json'}
    context.url = '/users/delete/{}'.format('jasonb')

@when('delete user')
def step_impl(context):
    context.page = context.client.delete(context.url, headers = context.headers)
    assert context.page

@then('I should get a \'200\' response')
def step_impl(context):
    print("code = ", context.page.status_code)
    assert context.page.status_code is 200

@then('user are not in the list of users')
def step_impl(context):
    assert 'jasonb' not in context.page.text

#----------------------------------------------------------------------
# Scenario: List all users
@given('a list of users stored in the system')
def step_impl(context):
    assert USERS

@when(u'i want to show them')
def step_impl(context):
    context.list = context.client.get('/users/all/{}'.format(USERS))
    assert context.list

@then(u'i want a \'200\' response')
def step_impl(context):
    assert context.list.status_code is 200

@then(u'the following list')
def step_impl(context):
    assert USERS
    
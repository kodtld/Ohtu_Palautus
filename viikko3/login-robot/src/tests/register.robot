*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kella  kella123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username too short
    
Register With Valid Username And Too Short Password
    Input Credentials  kalle  kake123
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kantsu  kalleyykaaoo
    Output Should Contain  Password too wack

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
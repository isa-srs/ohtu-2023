*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pentti  pentti10
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  matti  matti123
    Output Should Contain  User with username matti already exists

Register With Too Short Username And Valid Password
    Input Credentials  jb  justin95
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  jerkko13  jerkonsalasana1
    Output Should Contain  Username must only contain letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  jorma  jorma1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  maiju  maijunsalasana
    Output Should Contain  Password must not contain only letters

*** Keywords ***
Create User And Input New Command
    Create User  matti  matti123
    Input New Command
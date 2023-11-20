*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  jb
    Set Password  bieber123
    Set Password Confirmation  bieber123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Invalid Password
    Set Username  eemeli
    Set Password  eemelinsalasana
    Set Password Confirmation  eemelinsalasana
    Submit Credentials
    Register Should Fail With Message  Password must not contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  eemeli
    Set Password  eemeli123
    Set Password Confirmation  eemeli456
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation must match

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed
    Go To Main Page
    Logout
    Set Username  kalle
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  eemeli
    Set Password  eemelinsalasana
    Set Password Confirmation  eemelinsalasana
    Submit Credentials
    Register Should Fail With Message  Password must not contain only letters
    Go To Login Page
    Set Username  eemeli
    Set Password  eemelinsalasana
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Go To Main Page
    Click Link  Continue to main page

Go To Login Page
    Click Link  Login

Logout
    Click Button  Logout

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  martti  martti123
    Go To Register Page
    Register Page Should Be Open

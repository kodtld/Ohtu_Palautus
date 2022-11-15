*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kxsalmi
    Set Password  abcdefg1
    Set Conf Password  abcdefg1
    Submit Credentials
    Register Should Succeed


Register With Too Short Username And Valid Password
    Set Username  kx
    Set Password  abcdefg1
    Set Conf Password  abcdefg1
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kxsalmi
    Set Password  a1
    Set Conf Password  a1
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kxsalmi
    Set Password  abcdefg1
    Set Conf Password  abcdefg2
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  keijovara
    Set Password  abcdefg1
    Set Conf Password  abcdefg1
    Submit Credentials
    Go To Login Page
    Set Username  keijovara
    Set Password  abcdefg1
    Submit Login Credentials
    Login Should Succeed


Login After Failed Registration
    Set Username  testipete
    Set Password  ab2
    Set Conf Password  ab2
    Submit Credentials
    Go To Login Page
    Set Username  testipete
    Set Password  ab2
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Page Should Contain  Welcome

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Conf Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
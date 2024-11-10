*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Variables ***
${TITLE}                          Welcome to Ohtu Application!
${OHTU_TITLE}                     Ohtu Application main page
${USERNAME_MESSAGE}               Invalid username
${PASSWORD_MESSAGE}               Invalid password
${PASSWORD_CONFIRMATION_MESSAGE}  Password must match password confirmation

*** Test Cases ***

Register With Valid Username And Password
    Set Username  user
    Set Password  sala9sana
    Set Password Confirmation  sala9sana
    Click Button  Register
    Title Should Be  ${TITLE}

Register With Too Short Username And Valid Password
    Set Username  us
    Set Password  sala9sana
    Set Password Confirmation  sala9sana
    Click Button  Register
    Page Should Contain  ${USERNAME_MESSAGE}

Register With Valid Username And Too Short Password
    Set Username  user
    Set Password  sala9sa
    Set Password Confirmation  sala9sa
    Click Button  Register
    Page Should Contain  ${PASSWORD_MESSAGE}

Register With Valid Username And Invalid Password
    # salasana ei sisällä halutunlaisia merkkejä
    Set Username  user
    Set Password  salasana
    Set Password Confirmation  salasana
    Click Button  Register
    Page Should Contain  ${PASSWORD_MESSAGE}

Register With Nonmatching Password And Password Confirmation
    Set Username  user
    Set Password  sala9sana
    Set Password Confirmation  juustokakku
    Click Button  Register
    Page Should Contain  ${PASSWORD_CONFIRMATION_MESSAGE}

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Page Should Contain  ${USERNAME_MESSAGE}

Login After Successful Registration
    Set Username  user
    Set Password  sala9sana
    Set Password Confirmation  sala9sana
    Click Button  Register
    Go To Main Page
    Click Button  Logout
    Set Username  user
    set Password  sala9sana
    Click Button  Login
    Title Should Be  ${OHTU_TITLE}

Login After Failed Registration
    Set Username  user
    Set Password  salainensana
    Set Password Confirmation  salainensana
    Click Button  Register
    Go To Login Page
    Set Username  user
    set Password  salainensana
    Click Button  Login
    Title Should Be  Login


*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}
    
Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
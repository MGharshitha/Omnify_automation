Feature: Login functionality
  As a customer
  In order to use the application
  I want to login with email and password

#  Scenario: Logging in with valid credentials
#    Given Lunch the chrome browser
#    Given I am at the Account/Login page
#    When I fill the account email textbox with value 'myname@mymail.com'
#    And I fill the password textbox with value 'mypassword'
#    And I click the login button
#    Then I should be at the home page

#  Scenario Outline: Login failed
#    Given I am on the login page
#    When I enter invalid credentials "<username>", "<email>", and "<password>"
#    Then I should see an error message


  Scenario Outline: Logging in with valid credentials
    Given Lunch the chrome browser
    Given I am at the Account/Login page
    When I fill the account email textbox with value 'myname@mymail.com'
    And I fill the password textbox with value 'mypassword'
    And I click the login button
    Then I should be at the home page

    Examples:
      | email             | password  |
      | user1@example.com | password1 |
      | user2@example.com | password2 |
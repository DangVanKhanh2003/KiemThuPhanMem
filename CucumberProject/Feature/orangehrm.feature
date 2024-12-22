Feature: Verify elements on the OrangeHRM homepage

  Scenario: Verify elements on the login page of OrangeHRM
    Given launch Eage browser
    When open orange hrm homepage
    Then verify that the logo is present on the page
    And verify that the username text is present on the page
    And verify that the password text is present on the page
    And verify that the login button is present on the page
    And verify that the username input is present on the page
    And verify that the password input is present on the page
    Then close browser

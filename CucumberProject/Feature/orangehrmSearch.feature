Feature: Search functionality on OrangeHRM homepage

  Scenario: Verify the Search input field is displayed
    Given I launch the browser
    When I open the OrangeHRM homepage
    And I enter username "Admin" and password "admin123"
    And Click on Login button
    And I click on the Search input
    Then I should see the Search input field
    And I close the browser

  Scenario Outline: Test the Search input with various inputs
    Given I launch the browser
    When I open the OrangeHRM homepage
    And I enter username "Admin" and password "admin123"
    And Click on Login button
    And I click on the Search input
    Then I enter "<input_value>" in the Search input
    And I should see "<xpath_result>" in the results
    And I close the browser
    Examples:
      | input_value | xpath_result                                                                              |
      | a           | //*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul//span[text()='Admin']                    |
      | admin       | //*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul//span[text()='Admin']                    |
      | a           | //*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul//span[text()='Leave']                    |
      | a           | //*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul//span[text()='Performance']              |
      | a           | //*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul//span[text()='Dashboard']                |
      | a           | //*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul//span[text()='Maintenance']              |
      | a           | //*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul//span[text()='Claim']                    |
      | B           | //*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul//span[text()='Buzz']                     |
      | B           | //*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul//span[text()='Dashboard']                |
      | aDmin       | //*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul//span[text()='Admin']                    |

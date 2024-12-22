Feature: Admin User Management functionality

  Scenario: Verify the presence of elements on the Admin/User Management page
    Given I launch the browser amdin
    When I open the OrangeHRM homepage
    Then I navigate to the Admin menu
    Then I should see all the elements on the Admin/User Management page
    Then I close the browser admin

  Scenario: Verify the functionality of the "Search" button
    Given I launch the browser amdin
    When I open the OrangeHRM homepage
    Then I navigate to the Admin menu
    Then I search for a user with username "Admin"
    Then I should see results matching "Admin"
    Then I close the browser admin

  Scenario: Verify the "Reset" button functionality
    Given I launch the browser amdin
    When I open the OrangeHRM homepage
    Then I navigate to the Admin menu
    Then I fill the search fields with test data
    Then I reset the search fields
    Then I should see all fields cleared
    Then I close the browser admin

  Scenario: Verify the "+ Add" button functionality
    Given I launch the browser amdin
    When I open the OrangeHRM homepage
    Then I navigate to the Admin menu
    Then I click on the "+ Add" button
    Then I should be redirected to the Add User page
    Then I close the browser admin

  Scenario: Verify "No Records Found" message when no search results
    Given I launch the browser amdin
    When I open the OrangeHRM homepage
    Then I navigate to the Admin menu
    Then I search for a user with username "xyz123"
    Then I should see "No Records Found"
    Then I close the browser admin

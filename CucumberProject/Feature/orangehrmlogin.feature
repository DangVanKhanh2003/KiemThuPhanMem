Feature: OrangeHRM Login
 Scenario Outline: Login with valid and invalid credentials
  Given I launch Eage browser
  When I open orange HRM Homepage
  And I enter username "<username>" and password "<password>"
  And Click on Login button
  Then User must successfully login to the Dashboard page

  Examples:
    | username    | password    |
    | Admin       | admin123    |
    | ADmin       | admin123    |
    | ADMIN       | admin123    |

Scenario Outline: invalid credentials
  Given I launch Eage browser
  When I open orange HRM Homepage
  And I enter username "<username>" and password "<password>"
  And Click on Login button
  Then Login Invalid

  Examples:
    | username    | password    |
    |  adminxyz   |  admin123   |
    |    ''       |  adminxyz   |
    |  'Tàikhoản'|  'admin123'  |
    |  Admin      |     ''      |
    |  Admin      | select * from User |
    |  Admin      |  @$%^^&&34  |
    |  Admin      |  435435435  |
    |  Admin      | 'Khánhabc'  |
    |  ADmin      |  Admin12    |



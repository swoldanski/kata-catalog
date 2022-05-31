Feature: A Character cannot Deal Damage to itself.


  Scenario: Damage is subtracted from Health only when dealt by others
    Given a character enters the world with the following attributes
      | name | health | level | alive |
      | John | 1000   | 1     | True  |

    When the character receives damage from
      | name | damage |
      | John | 330    |
      | Bob  | 100    |
      | Mary | 270    |
      | John | 300    |

    Then the character health is
      | health |
      | 630    |

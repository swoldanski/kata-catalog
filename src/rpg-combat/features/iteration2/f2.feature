Feature: A Character can only Heal itself.


  Scenario: Healing cannot be done by others 
    Given a character enters the world with the following attributes
      | name | health | level | alive |
      | John | 1000   | 1     | True  |

    When the character receives damage
      | damage |
      | 999    |

    And the character receives health from
      | name | health |
      | John | 330    |
      | Mary | 270    |
      | John | 350    |
      | Bob  | 100    |

    Then the character health is
      | health |
      | 681    |

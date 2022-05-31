Feature: A Character can Heal a Character.
    - Dead characters cannot be healed
    - Healing cannot raise health above 1000


  Scenario: Dead characters cannot be healed 
    Given a character enters the world with the following attributes
      | name | health | level | alive |
      | John | 1000   | 1     | True  |

    When the character receives damage
      | damage |
      | 1000   |
    
    And the character receives health
      | health |
      | 1      |

    Then the character is Dead


  Scenario: Healing cannot raise health above 1000 
    Given a character enters the world with the following attributes
      | name | health | level | alive |
      | John | 1000   | 1     | True  |

    When the character receives damage
      | damage |
      | 999    |

    And the character receives health
      | health |
      | 100    |
      | 1000   |
      | 100    |
      | 10     |
      | 1      |

    Then the character health is
      | health |
      | 1000   |

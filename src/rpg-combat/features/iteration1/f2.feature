Feature: Characters can Deal Damage to Characters.
    - Damage is subtracted from Health
    - When damage received exceeds current Health, Health becomes 0 and the character dies


  Scenario: Damage is subtracted from Health 
    Given a character enters the world with the following attributes
      | name | health | level | alive |
      | John | 1000   | 1     | True  |

    When the character receives damage
      | damage |
      | 330    |
      | 100    |
      | 270    |

    Then the character health is
      | health |
      | 300    |


  Scenario: When damage received exceeds current Health, Health becomes 0 and the character dies 
    Given a character enters the world with the following attributes
      | name | health | level | alive |
      | John | 1000   | 1     | True  |

    When the character receives damage
      | damage |
      | 330    |
      | 100    |
      | 270    |
      | 500    |

    Then the character health is
      | health |
      | 0    |

    And the character is Dead
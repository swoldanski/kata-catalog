Feature: When dealing damage:
    - If the target is 5 or more Levels above the attacker, Damage is reduced by 50%
    - If the target is 5 or more Levels below the attacker, Damage is increased by 50%


  Scenario: Damage is dealt by enemy with comparable level 
    Given a character enters the world with the following attributes
      | name | health | level | alive |
      | John | 1000   | 1     | True  |

    And the character current level is 10  

    When the character receives damage from others with some level
      | damage | level |
      | 330    | 6     |
      | 50     | 10    |
      | 270    | 14    |

    Then the character health is
      | health |
      | 350    |

  Scenario: Damage is dealt by enemy with low level 
    Given a character enters the world with the following attributes
      | name | health | level | alive |
      | John | 1000   | 1     | True  |

    And the character current level is 10  

    When the character receives damage from others with some level
      | damage | level |
      | 330    | 5     |
      | 50     | 1     |
      | 270    | 3     |

    Then the character health is
      | health |
      | 675    |

  Scenario: Damage is dealt by enemy with high level 
    Given a character enters the world with the following attributes
      | name | health | level | alive |
      | John | 1000   | 1     | True  |

    And the character current level is 10  

    When the character receives damage from others with some level
      | damage | level |
      | 330    | 99    |
      | 50     | 15    |
      | 270    | 30    |

    Then the character health is
      | health |
      | 25    |

  Scenario: Damage is dealt by enemy with different level 
    Given a character enters the world with the following attributes
      | name | health | level | alive |
      | John | 1000   | 1     | True  |

    And the character current level is 10  

    When the character receives damage from others with some level
      | damage | level |
      | 330    | 99    |
      | 50     | 15    |
      | 270    | 30    |
      | 24     | 5     |
      | 12     | 1     |
      | 6      | 3     |

    Then the character health is
      | health |
      | 4      |

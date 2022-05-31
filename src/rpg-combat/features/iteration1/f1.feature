Feature: All Characters, when created, have:
    - Health, starting at 1000
    - Level, starting at 1
    - May be Alive or Dead, starting Alive (Alive may be a true/false)


  Scenario: Create new character
    Given a character enters the world with the following attributes

      | name | health | level | alive |
      | John | 0      | 0     | False |
      | Wu   | 1      | 1     | True  |
      | Mary | 500    | 1     | False |
      | Dex  | 1001   | 2     | True  |

     Then the new character has these initial attributes
    
      | health | level | alive |
      | 1000   | 1     | True  |

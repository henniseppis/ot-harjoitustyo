 ```mermaid
 classDiagram
      Players "*" --> "2-8" Board
      Man "*" --> "1" Players
      Man "*" --> "1" Square
      Squares "*" --> "40" Board
      Man"*" --> "1" Squares
      Dices"*" --> "2" Board
      class Game
      class Board
      class Players
      class Dices
      class Streets
      class Squares
      class Man
         

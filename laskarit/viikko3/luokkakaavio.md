 ```mermaid
 classDiagram
      Board "1" -- "1" Game
      Players "2-8" -- "1" Game
      Man "1" --> "1" Players
      Man "1" --> "1" Squares
      Squares "40" -- "1" Board
      Dices"2" -- "1" Game
      class Game
      class Board
      class Players
      class Dices
      class Squares
      class Man
         

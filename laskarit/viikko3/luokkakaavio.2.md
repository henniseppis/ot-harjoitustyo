 ```mermaid
 classDiagram
      Board "1" --> "1" Game
      Players "2..8" --> "1" Game
      Man "1" --> "1" Players
      Man "1" --> "1" Squares
      Squares "40" --> "1" Board
      Dices"2" --> "1" Game
      Houses"4" --> "1" Street
      Street "*" --> "1" Players
      Players "*" --> "*" Money
      Cards "*" --> Squares: + Coincidence & TogetherLand
      
      
      class Game
      class Board
      class Players
      class Dices
      class Squares
      Squares: + Start()
      Squares: + Prison()
      Squares: + Coincidence & TogetherLand()
      Squares: + Station & Institute()
      class Street
      
      
      class Man
      class Houses
 ```


....Nää jäi vähän kesken niin on varmasti vähän vääränlaisia:D

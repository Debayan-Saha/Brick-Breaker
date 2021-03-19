# Brick Breaker

This is an implementation of an arcade game in Python3 inspired from the old classic brick breaker game. This is implemented from scratch without the use of PyGame library. Only numpy and colorama are the major libraries used. 

## Running
1. Install the requirements using the code below:
 `pip3 install colorama`
 `pip3 install numpy`
2. Run game using
` python3 main.py`

## Instructions

1. `A` to move the paddle left.
2. `D` to move the paddle right.
3. `S` to release the ball from the paddle.
4. `Q` to quit the game.
5. You get 3 lives in the game.
6. Increase your score by breaking the bricks.
7. Each brick has different colour showing different properties.
8. `Cyan` coloured brick shows unbreakable brick. This brick has no points.
9. `Blue` coloured brick shows level 3 brick. After breaking this brick, player get 5 points and colour change to `Magenta`.
10. `Magenta` coloured brick shows level 2 brick. After breaking this brick, player get 5 points and colour change to `Red`.
11. `Red` coloured brick shows level 1 brick. After breaking this brick, player get 5 points and the brick disappears.
12. `Yellow` coloured brick shows explosion brick. This brick has no points. After breaking this brick, all the adjacent bricks(diagonally, vertically and horizontally) disappears.
13. `Rainbow` brick are brick which changes colour every frame of the game. When the ball hits this brick the colour becomes constant and degrades from the colour in which it was hit.
14. The game ends when player defeats the boss enemy i.e. the UFO.
15. The game has 3 levels. The last level is the boss level.
16. `X` to skip the levels.
17. After 20 seconds in each level the bricks start to fall down.
18. Once the lowest brick in the current brick layout reaches the paddle level, the game is over

## Boss level
1. The final level of the game has the boss enemy along with a few unbreakable bricks.
2. The boss enemy is a UFO which flies at the top of the screen and follows the paddle
3. The UFO drops bombs in regular intervals onto the paddle, on being hit by these bombs the paddle loses one life.
4. The UFO has a health which reduces on hitting it directly will the ball 
5. The UFO will spawn defensive bricks around it

## Assignment related stuff

1. **Polymorphism** - Ball, Brick and Object have the `render` but it behaves differently in all of them, however, it is execueted in the same way.
2. **Inheritance** - Paddle, Ball, Brick and Bomb are inherited from same parent class `Object` and Rainbow & Boss are inherited from same parent class `Brick`
3. **Encapsulation** - Every component on the board is an object of a class. This instantiation encapsulates the methods and attributes of the objects.
4. **Abstraction** - The functions of each class hide the inner details of the function enabling users to use just the function name.



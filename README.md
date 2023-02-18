# battleship_algorithm

Algorithm:
- center = higher probability
- if cell = miss, cells around it -> lower probability
- if ship hit -> look in 4 directions to find rest of ship
- if ship sunk -> cells around the ship -> 0 probability (cannot place ships adjacent to each other)

Humans takes > 78 shots 99% of the time in order to win (https://datagenetics.com/blog/december32011/index.html).
This algorithm takes < 45 shots to win (over 6700 runs).

Here is a visual demonstration of the algorithm:

https://user-images.githubusercontent.com/60311384/219883945-27c8802b-032d-405c-87b0-c55998651bca.mov

-- String permutations

import Data.List

perms :: [a] -> [[a]]
permute [] = [[]]
permute xs = [y | prefix <- xs, y <- map (prefix:) $ permute $ xs \\ [prefix]]


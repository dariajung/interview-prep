-- String permutations

import Data.List

permute :: Eq a => [a] -> [[a]]
permute [] = [[]]
permute xs = [y | prefix <- xs, y <- map (prefix:) $ permute $ xs \\ [prefix]]


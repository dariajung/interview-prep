import Data.List

permute [] = [[]]
permute str = nub $ [ p | prefix <- str, let rest = str \\ [prefix], p <- map (prefix:) (permute rest) ]
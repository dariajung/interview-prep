graph = [[1, 2, 3], [], [3], [0], [3], [4]]

type Node = Int
type Graph = [[Integer]]

sort :: Graph -> [Integer] -> [Integer] -> [Integer]
sort graph visited [] = visited
sort graph visited (x:xs)
    | x `elem` visited      = sort graph visited xs
    | otherwise             = sort graph (visited ++ [x]) ((graph !! (fromIntegral x)) ++ xs)
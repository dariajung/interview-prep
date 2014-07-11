-- return the last index of n
-- id: lastIndexOf 5 [1,2,5,6,5] is 4

helper n [] index = index
helper n ((i,x):xs) curIndex  
   | x == n     = helper n xs i
   | otherwise  = helper n xs curIndex

indexLastOf arr n =
    let zipped = zip [0..] arr
    in helper n zipped (-1)



memoized_fib :: Int -> Integer
memoized_fib =
    let fib 0 = 0
        fib 1 = 1
        fib x = memoized_fib (x - 1) + memoized_fib (x - 2)
    in (map fib [0..] !!)

naive_fib :: Int -> Int
naive_fib x
    | x == 0    = 0
    | x == 1    = 1
    | otherwise = naive_fib (x - 1) + naive_fib (x - 2)

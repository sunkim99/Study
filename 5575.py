for _ in range(3):
    i_h, i_m, i_s, o_h, o_m, o_s = map(int,input().split())
    in_time = i_h * 3600 + i_m * 60 + i_s 
    out_time = o_h * 3600 + o_m * 60 + o_s

    gap = out_time - in_time

    h = gap // 3600
    m = (gap % 3600) // 60
    s = (gap % 3600) % 60

    print(h, m, s)



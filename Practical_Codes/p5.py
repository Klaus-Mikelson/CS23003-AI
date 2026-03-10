def constrain_satisfraction(char1,char2,res):
    for S in range(1, 10):          
        for E in range(10):
            if E == S:
                continue
            for N in range(10):
                if N in (S, E):
                    continue
                for D in range(10):
                    if D in (S, E, N):
                        continue
                    for M in range(1, 10):  
                        if M in (S, E, N, D):
                            continue
                        for O in range(10):
                            if O in (S, E, N, D, M):
                                continue
                            for R in range(10):
                                if R in (S, E, N, D, M, O):
                                    continue
                                for Y in range(10):
                                    if Y in (S, E, N, D, M, O, R):
                                        continue
                                    SEND = 1000*S + 100*E + 10*N + D
                                    MORE = 1000*M + 100*O + 10*R + E
                                    MONEY = 10000*M + 1000*O + 100*N + 10*E + Y
                                    if SEND + MORE == MONEY:
                                        print("Solution found:")
                                        print(f"S={S}, E={E}, N={N}, D={D}")
                                        print(f"M={M}, O={O}, R={R}, Y={Y}")
                                        print(f"SEND = {SEND}")
                                        print(f"MORE = {MORE}")
                                        print(f"MONEY = {MONEY}")
                                        return
constrain_satisfraction("SEND","MORE","MONEY")
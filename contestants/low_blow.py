def strategy(last_results):
        if len(last_results) <= 3:
                return 99

        first = list(map(lambda a: a[0], last_results[:3 ]))
        
        if first == [99, 98, 98]: return 1
        if first == [27, 99, 27]: return 26
        if first == [50, 50, 50]: return 49
        if first == [ 1,  1,  1]: return 1
        if first == [69, 69, 69]: return 68
        if first == [65, 65, 65]: return 64

        if len(last_results) > 420 and first == [69, 69, 69]:
                return 67

        if len(last_results) > 5:
                last = list(map(lambda a: a[0], last_results[-5:]))
                deltas = []
                for x, y in zip(last, last[1:]):
                        deltas.append(x - y)

                if deltas != [0, 0, 0, 0]:
                        return 1

        return 99

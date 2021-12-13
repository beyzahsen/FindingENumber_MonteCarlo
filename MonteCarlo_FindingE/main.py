from baa import TicToc, FindE
from threading import Thread
import os

if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    n = 100000000
    find_es = []
    threads = []
    for i in range(os.cpu_count()):
        find_es.append(FindE())
        threads.append(Thread(target=find_es[i].throw_points, args=(n,)))
        print("Started thread number %d" % i)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    inner = 0
    total = 0
    for find_e in find_es:
        inner += find_e.i
        total += find_e.n

    e = inner / total
    print("E= %.8f  | TIME = %.5f seconds" % (e, tt.toc()))

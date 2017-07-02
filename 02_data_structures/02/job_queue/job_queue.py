# python3

from heapq import heappush, heappop

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        #print('# workers', self.num_workers)

        scheduler = []

        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)


        free_workers = self.num_workers

        for i in range(0, len(self.jobs)):
            #print(i, self.jobs[i])

            job_time = 0

            if free_workers > 0:
                heappush(scheduler, (self.jobs[i], i))
                free_workers -= 1
                worker_id = i
            else:
                job_time, worker_id = heappop(scheduler)

                heappush(scheduler, (self.jobs[i] + job_time, worker_id))

            self.assigned_workers[i] = worker_id
            self.start_times[i] = job_time


    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

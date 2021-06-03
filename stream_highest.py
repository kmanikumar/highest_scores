from heapq import heappush, heappushpop
import sys, json

class stream_highest:
    def __init__(self, k):
        self.min_heap = []
        self.map = {}
        self.k = k

    def process_record(self, record):
        key, value = record.split(': ', 1)
        key = int(key)
        if key not in self.map:
            self.map[key]=value
            if len(self.min_heap) < k:
                heappush(self.min_heap, key)
            else:
                del self.map[heappushpop(self.min_heap, key)]
        else:
            self.map[key]=value

    def highest_k_ids(self):
        try:
            ret = [{'score':score, 'id':json.loads(self.map[score])['id']} for score in sorted(self.min_heap)]
        except:
            print("invalid json format No JSON object could be decoded")
            sys.exit(1)

        ret.sort(key=lambda x:x['score'], reverse=True)
        return ret

if __name__ == "__main__":
    # parsing and validating command line args
    try:
        open_file = open(sys.argv[1])
    except:
        print("INVALID FILENAME ARG")
        sys.exit(1)
    try:
        k = int(sys.argv[2]) # assumption: k < # scores
    except:
        print("INVALID K ARG")
        sys.exit(1)

    sh = stream_highest(k)
    for line in open_file:
        sh.process_record(line)
    print(json.dumps(sh.highest_k_ids(), indent=4, sort_keys=True))

import json
import sys

def partition(a, l, r):
    x = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1

def quickselect(a, k):
    l, r = 0, len(a) - 1
    pivot = partition(a, l, r)
    if pivot == r - k + 1:
        return a[pivot]
    elif pivot > r - k + 1:
        return quickselect(a[:pivot], k - (r - pivot + 1))
    else:
        return quickselect(a[pivot + 1:r + 1], k)

def batch_highest(open_file, k):
    data = {}
    for line in open_file:
        key, value = line.split(': ', 1)
        data[int(key)] = value.replace('\n','')

    scores = list(data.keys())
    kth_val = quickselect(scores, k)

    ret = []
    for score in scores:
        if score >= kth_val:
            try:
                id = json.loads(data[score])['id']
            except:
                print("invalid json format No JSON object could be decoded\n" + data[score])
                sys.exit(1)

            ret.append({'score':score, 'id':id})

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

    print(json.dumps(batch_highest(open_file, k), indent=4, sort_keys=True))

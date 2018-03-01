from __future__ import division

import operator

def from_file(file_obj):
    line_iter = iter(file_obj)

    counts_line = next(line_iter).strip()

    videos_line = next(line_iter).strip()
    obj.videos = tuple(
        Video(id=index, size=int(size_mb), possible_caches={})
        for index, size_mb in enumerate(videos_line.split(' '))
    )

    obj.caches = tuple(
        Cache(id=index, size=obj.cache_size_mb, stored_videos={}, endpoints={}, possible_videos={},
              sorted_possible_videos=[], done=False, first_time=True)
        for index in range(obj.caches_count)
    )

    for endpoint_id in range(obj.endpoints_count):
        endpoint_desc_line = next(line_iter).strip()
        dc_latency, caches_count = map(int, endpoint_desc_line.split(' '))
        endpoint = Endpoint(id=endpoint_id, dc_latency=dc_latency, caches_count=caches_count, caches_latencies={})
        obj.endpoints.append(endpoint)

        for cache in range(caches_count):
            cache_desc_line = next(line_iter).strip()
            cache_id, latency = map(int, cache_desc_line.split(' '))
            endpoint.caches_latencies[cache_id] = latency
            obj.caches[cache_id].endpoints[endpoint_id] = latency

    obj.process_requests(line_iter)

    return obj


from sys import argv
filename = argv[1]
with open(filename) as file_obj:
    print 'Start', filename
    w = from_file(file_obj)
    # w.process_requests()
    count = 1
    print "************** Processing all #", count, "**************\nProcessing Cache # ",
    while not w.process_caches():
        print
        print "Done Processing all #", count
        print "Caches remaining size",
        for cache in w.caches:
            print "Full" if cache.done else cache.size,
        count += 1
        print
        print "************** Processing all #", count, "**************\nProcessing Cache # ",
    w.output_result(filename.replace('.in', '.out'))
    print 'Done', filename
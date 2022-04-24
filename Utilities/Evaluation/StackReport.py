    print(f"**** aside ****")
    frame_count = 0
    for frame_info in stack():
        trace_count = 0
        print(f"FrameInfo[ {frame_count} ]:")
        for trace_info in frame:
            print(f"  TraceInfo[ {trace_count} ]:")
            trace_list_cunter = 0
            for trace_info_data in frame:
                print(f"    trace_info_data[ {trace_list_cunter} ]:")
                print(f"      {frame_info}")
                trace_list_cunter += 1
            trace_count += 1
        frame_count += 1
        print()

    print(f"**** aside ****")
    frame_count = 0
    for frame_info in stack():
        trace_count = 0
        print(f"FrameInfo[ {frame_count} ]:")
        trace_info_count = 0
        for trace_info in frame_info:
            print(f"  trace_info[ {trace_info_count} ]:")
            #print(f"    {frame_info[trace_count]}")
            #print(f"    {frame_info}")
            trace_info_count += 1
            frame_trace_info_count = 0
            for frame_trace_info in frame_info:
                print(f"    frame_trace_info[ {frame_trace_info_count} ]:")
                print(f"      {frame_trace_info}")
                frame_trace_info_count += 1
        frame_count += 1
    print()


    print(f"**** aside ****")
    frame_count = 0
    for frame_info in stack():
        trace_count = 0
        print(f"FrameInfo[ {frame_count} ]:")
        trace_info_count = 0
        for trace_info in frame_info:
            print(f"  trace_info[ {trace_info_count} ]:")
            #print(f"    {frame_info[trace_count]}")
            print(f"    {frame_info}")
            trace_info_count += 1
            frame_trace_info_count = 0
            #for frame_trace_info in frame_info:
                #print(f"    frame_trace_info[ {frame_trace_info_count} ]:")
                #print(f"      {frame_trace_info}")
                ##if frame_trace_info_count == 0:
                    ##frame_trace_info_list_count = 0
                    ##for frame_trace_info_list in frame_trace_info:
                        ##print(f"    frame_trace_info_list[ {frame_trace_info_list_count} ]:")
                        ##print(f"      {frame_trace_info_list}")
                    ##frame_trace_info_list_count += 1
                #frame_trace_info_count += 1
        frame_count += 1
    print()

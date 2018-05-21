def summarize_generator(key_in):
    # create summarize plane data from type Plane_id:number count, for query data passed
    summarize = {}
    counter = 1
    for key in key_in:
        planes_count = 0
        aircraft_pk = key.aircraftid
        if aircraft_pk in summarize:
            planes_count = summarize[aircraft_pk]
        planes_count += 1
        summarize[aircraft_pk] = planes_count
        counter += 1

    return summarize, counter


def summarize_time_generator(key_in, start_or_end):
    # summarize by hour with "start" parameter(for take-offs) and "end" parameter for landings
    summarize = {}
    counter = 1
    if start_or_end == "start":
        for key in key_in:
            planes_counter = 0
            hour = key.starttime.hour
            if hour in summarize:
                planes_counter = summarize[hour]
            planes_counter += 1
            summarize[hour] = planes_counter
            counter += 1
    elif start_or_end == "end":
        for key in key_in:
            planes_counter = 0
            hour = key.endtime.hour
            if hour in summarize:
                planes_counter = summarize[hour]
            planes_counter += 1
            summarize[hour] = planes_counter
            counter += 1
    return summarize, counter

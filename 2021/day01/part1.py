#!/usr/bin/env python

with open('day1.txt') as f:
    data = f.read().splitlines() 
    previous = None
    increased = 0

    for line in data:
        # If there's no previous value, assume it's first
        if not previous:
            print(f"{line} (N/A - no previous measurement)")
            previous = line
        # Otherwise, determine if value is larger
        else:
            if int(line) > int(previous):
                increased += 1
                print(f"{line} (increased)")
            else:
                print(f"{line} (decreased)")
            previous = line

print(increased)

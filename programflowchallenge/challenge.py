address = input("enter "
                "ip address: ")
if address[-1] != '.':
  address += '.'
num_segments = 1
segment_len = 0
i = 0
for i in address:
    if i in "0123456789":
        segment_len += 1
        continue
    else:
        print("Segment {} contains {} characters".format
              (num_segments, segment_len))
        num_segments += 1
        segment_len = 0
#if i != ".":
#   print("Segment {} contains {} characters".format(num_segments, segment_len))

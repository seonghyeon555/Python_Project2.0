class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("NOT SUPPORTED")
        else:
            print("Read from",src)

print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")
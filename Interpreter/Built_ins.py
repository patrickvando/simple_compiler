class Built_ins:
    funcs = ["print"]

    def interpret_func(func_name, args):
        if func_name == "print":
            Built_ins.print_func(args)

    def print_func(args):
        if not args:
            print()
            return
        st = ""
        for arg in args:
            st += str(arg) + ", "
        print(st[:-2])

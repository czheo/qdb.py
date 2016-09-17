import sys
import os
class QDB:
    def __init__(self):
        self.db= {
        }
        self.src = [
'import sys',
'import os',
'class QDB:',
'    def __init__(self):',
'        self.db= {',
'        }',
'        self.src = [',
'        ]',
'    def db_src(self):',
'        retval = ""',
'        for k, v in self.db.items():',
'            retval += "            %r: %r,\\n" % (k, v)',
'        return retval',
'    def write_db(self):',
'        with open(os.path.realpath(__file__), "w") as f:',
'            f.write(self.gen_src())',
'    def gen_src(self):',
'        output = "".join(map(lambda l: l + "\\n", self.src[:5]))',
'        output += self.db_src()',
'        output += "".join(map(lambda l: l + "\\n", self.src[5:7]))',
'        output += "".join(map(lambda l: "%r,\\n" % l, self.src))',
'        output += "".join(map(lambda l: l + "\\n", self.src[7:]))',
'        return output',
'    def run(self):',
'        if len(sys.argv) > 1:',
'            cmd = sys.argv[1]',
'            if cmd == "get":',
'                val = self.db.get(sys.argv[2])',
'                if val:',
'                    print(val)',
'            elif cmd == "set":',
'                self.db[sys.argv[2]] = sys.argv[3]',
'                self.write_db()',
'            elif cmd == "delete":',
'                del self.db[sys.argv[2]]',
'                self.write_db()',
'            elif cmd == "dump":',
'                for k, v in self.db.items():',
'                    print(k, "\\t=>\\t",v)',
'            elif cmd == "flushdb":',
'                self.db = {}',
'                self.write_db()',
'        else:',
'            print(self.gen_src(), end="")',
'if __name__ == "__main__":',
'    db = QDB()',
'    db.run()',
        ]
    def db_src(self):
        retval = ""
        for k, v in self.db.items():
            retval += "            %r: %r,\n" % (k, v)
        return retval
    def write_db(self):
        with open(os.path.realpath(__file__), "w") as f:
            f.write(self.gen_src())
    def gen_src(self):
        output = "".join(map(lambda l: l + "\n", self.src[:5]))
        output += self.db_src()
        output += "".join(map(lambda l: l + "\n", self.src[5:7]))
        output += "".join(map(lambda l: "%r,\n" % l, self.src))
        output += "".join(map(lambda l: l + "\n", self.src[7:]))
        return output
    def run(self):
        if len(sys.argv) > 1:
            cmd = sys.argv[1]
            if cmd == "get":
                val = self.db.get(sys.argv[2])
                if val:
                    print(val)
            elif cmd == "set":
                self.db[sys.argv[2]] = sys.argv[3]
                self.write_db()
            elif cmd == "delete":
                del self.db[sys.argv[2]]
                self.write_db()
            elif cmd == "dump":
                for k, v in self.db.items():
                    print(k, "\t=>\t",v)
            elif cmd == "flushdb":
                self.db = {}
                self.write_db()
        else:
            print(self.gen_src(), end="")
if __name__ == "__main__":
    db = QDB()
    db.run()

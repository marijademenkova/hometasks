import psutil
import datetime
import json
import time

class writer:
        def read_num(self, path):
                pass
        def save(self, data, path):
                pass

class json_writer(writer):

        def read_num(self, path):
                return sum(1 for line in open(path)) + 1

        def save(self, data, path):
                with open(path, "a") as f:
                        json.dump(data, f, sort_keys=True)
                        f.write('\n')

                pass

class text_writer(writer):
        def read_num(self, path):
                return sum(1 for line in open(path)) / 5 + 1

        def save(self, data, path):
                with open(path, 'a') as outfile:
                        outfile.write(data)


class common:

        def __init__(self):
                self.json_writer = json_writer()
                self.text_writer = text_writer()

        def config_parse(self):
                with open('config.txt') as config:
                        lines = config.readlines()
                self.interval = int(lines[2].split()[-1])
                self.format = lines[1].split()[-1]

        def main(self):
                while True:
                        self.config_parse()

                        cpu = psutil.cpu_times()
                        vm = psutil.virtual_memory()
                        mem = psutil.swap_memory()
                        io = psutil.disk_io_counters()
                        net = psutil.net_io_counters()
                        timestamp = datetime.datetime.now()

                        if self.format == 'text':
                                data = ''.join(('SNAPSHOT '+str(self.text_writer.read_num('result.txt'))+': ', str(timestamp)+': ', str(cpu)+'\n', str(vm)+'\n', str(mem)+'\n', str(io)+'\n', str(net)+'\n'))
                                self.text_writer.save(data, 'result.txt')

                        elif self.format == 'json':
                                data = {'SNAPSHOT'+str(self.json_writer.read_num('result.json')): (str(timestamp), 'CPU: ' + str(cpu), 'VM: '+str(vm), 'Mem: '+str(mem), 'IO: '+str(io), 'Net: '+str(net))}
                                self.json_writer.save(data, 'result.json')

                        time.sleep(self.interval)
a = common()
a.main()

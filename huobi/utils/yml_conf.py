import yaml

class Yml:
    def get_application_conf(self, file):
        f = open(file)
        yml = yaml.load(f, Loader=yaml.FullLoader)
        return yml
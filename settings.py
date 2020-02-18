import os, yaml

def getdire():
    dire=os.path.split(__file__)[0]
    if dire != "":
        os.chdir(dire)
    return dire

dire=getdire()

def getSettings(section = None):
    if section == None:
        return yaml.load(open('settings.yaml'),Loader=yaml.FullLoader)
    return yaml.load(open('settings.yaml'),Loader=yaml.FullLoader)[section]

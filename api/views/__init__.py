from api.views.server import Server
from api.views.account import Account
from api.views.upload import Upload
from api.views.project import Project
from api.views.datacenter import DataCenterView as DataCenter
from api.views.machineroom import MachineRoomView as MachineRoom
from api.views.cabinet import CabinetView as Cabinet
from api.views.group import GroupView as Group
from api.views.dashboard import Dashboard

__all__ = ["Server", "Account", "Upload", "Project", "DataCenter", "MachineRoom", "Cabinet", "Group", "Dashboard"]

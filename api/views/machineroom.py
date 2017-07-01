from api.libs.base import CoreView
from cmdb.models import MachineRoom, DataCenter
from account.models import UserProfile
from django.db.utils import IntegrityError


class MachineRoomView(CoreView):
    """
    机房视图类
    """
    def get_list(self):
        per_page = self.parameters("per_page")
        if per_page:
            machineroom_objs = self.page_split(MachineRoom.objects.all())
        else:
            machineroom_objs = MachineRoom.objects.all()

        machineroom_list = []
        for machineroom_obj in machineroom_objs:
            machineroom_list.append(machineroom_obj.get_info())
        self.response_data["data"] = machineroom_list

    def post_create(self):
        try:
            name = self.parameters("name")
            contact = self.parameters("contact")
            memo = self.parameters("memo")
            address = self.parameters("address")
            admin_id = int(self.parameters("admin"))
            datacenter_id = int(self.parameters("datacenter"))
            admin_obj = UserProfile.objects.filter(id=admin_id).first()
            datacenter_obj = DataCenter.objects.filter(id=datacenter_id).first()
            if admin_obj and admin_obj.user:
                new_machineroom_obj = MachineRoom(name=name, contact=contact, memo=memo, admin=admin_obj.user, address=address, center=datacenter_obj)
            else:
                new_machineroom_obj = MachineRoom(name=name, contact=contact, memo=memo, address=address, center=datacenter_obj)
            new_machineroom_obj.save()
            self.response_data['data'] = new_machineroom_obj.get_info()
        except IntegrityError:
            self.response_data['status'] = False
            self.status_code = 416
import datetime

from django.db import models

# Create your models here.
class User(models.Model):
    SEX=(
        ("male","男"),("female","女"),
    )
    LOCATION=(
        ("上海","上海"),
        ("北京","北京"),
        ("广州","广州"),
        ("深圳","深圳"),
        ("合肥","合肥"),
        ("南京","南京"),
        ("西安","西安"),
    )
    phonenum=models.CharField(max_length=16,unique=True,db_index=True,
                              verbose_name="手机号")
    nickname=models.CharField(max_length=32,verbose_name="昵称")
    sex=models.CharField(max_length=8,choices=SEX,default="male",verbose_name="性别")
    birthday=models.DateField(default="1990-1-1",verbose_name="出生日期")
    location=models.CharField(max_length=16,choices=LOCATION,verbose_name="居住地")
    avatar=models.CharField(max_length=256,verbose_name="个人形象")
    def to_dict(self):
        return {
            "uid":self.pk,
            "phonenum":self.phonenum,
            "nickname":self.nickname,
            "sex":self.sex,
            "birthday":str(self.birthday),
            "location":self.location,
            "avatar":self.avatar
        }


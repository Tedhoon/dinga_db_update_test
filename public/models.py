from django.db import models

class PublicData(models.Model):
    id = models.TextField(primary_key=True)

    pb_name = models.TextField(blank=True)
    pb_goal = models.TextField(blank=True)
    pb_target = models.TextField(blank=True)
    pb_criteria = models.TextField(blank=True)
    pb_support_desc = models.TextField(blank=True)
    pb_online_url = models.TextField(blank=True)
    pb_submit_step = models.TextField(blank=True)
    pb_submit_date = models.TextField(blank=True)
    pb_need_paper = models.TextField(blank=True)
    pb_manage_department_type = models.TextField(blank=True)
    pb_manage_department_name = models.TextField(blank=True)
    pb_qna_department_name = models.TextField(blank=True)
    pb_qna_department_call = models.TextField(blank=True)
    pb_qna_department_url = models.TextField(blank=True)
    pb_category = models.TextField(blank=True)
    pb_target_agerange = models.TextField(blank=True)
    pb_target_area = models.TextField(blank=True)
    pb_support_type = models.TextField(blank=True)
    pb_disclosuer = models.TextField(blank=True)

    pb_benefit_info = models.TextField(blank=True)
    pb_sub_business = models.TextField(blank=True)
    pb_statute = models.TextField(blank=True)
    pb_manage_department_detail_part = models.TextField(blank=True)
    pb_target_type = models.TextField(blank=True)
    pb_support_cate = models.TextField(blank=True)


    # pb_update_date = models.DateTimeField(auto_now = True )

    pb_dinga_agerange = models.TextField(null=True, blank=True)
    pb_dinga_type = models.TextField(null=True, blank=True)

    pb_update_check = models.BooleanField(default="False")



class PublicUpdate(models.Model):
    id = models.TextField(primary_key=True)

    pb_name = models.TextField(blank=True)
    pb_goal = models.TextField(blank=True)
    pb_target = models.TextField(blank=True)
    pb_criteria = models.TextField(blank=True)
    pb_support_desc = models.TextField(blank=True)
    pb_online_url = models.TextField(blank=True)
    pb_submit_step = models.TextField(blank=True)
    pb_submit_date = models.TextField(blank=True)
    pb_need_paper = models.TextField(blank=True)
    pb_manage_department_type = models.TextField(blank=True)
    pb_manage_department_name = models.TextField(blank=True)
    pb_qna_department_name = models.TextField(blank=True)
    pb_qna_department_call = models.TextField(blank=True)
    pb_qna_department_url = models.TextField(blank=True)
    pb_category = models.TextField(blank=True)
    pb_target_agerange = models.TextField(blank=True)
    pb_target_area = models.TextField(blank=True)
    pb_support_type = models.TextField(blank=True)
    pb_disclosuer = models.TextField(blank=True)

    pb_benefit_info = models.TextField(blank=True)
    pb_sub_business = models.TextField(blank=True)
    pb_statute = models.TextField(blank=True)
    pb_manage_department_detail_part = models.TextField(blank=True)
    pb_target_type = models.TextField(blank=True)
    pb_support_cate = models.TextField(blank=True)
    #밑의 컬럼은 import시 없애고 시작해야함
    pb_dinga_agerange = models.TextField(null=True, blank=True)
    pb_dinga_type = models.TextField(null=True, blank=True)


    


class CascadeTest(models.Model):
    nickname = models.CharField('닉네임',max_length=40)
    belong_public = models.ForeignKey(PublicData,related_name="public_qna", null = True,on_delete=models.CASCADE)


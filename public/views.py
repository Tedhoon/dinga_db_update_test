from django.shortcuts import render
from .models import PublicData , PublicUpdate

def comparemachine(request):
    publicdata = PublicData.objects.all().order_by("id")
    publicupdate = PublicUpdate.objects.all().order_by("id")


    #처음에 update check를 false로 초기화시킵니당
    for data in publicdata:
        data.pb_update_check = "False"
        data.save()

    for update in publicupdate:
        for data in publicdata:
            if data.id == update.id:
                print(update.id+"의 id를 가진 일치하는 데이터가 있습니다. 정책을 업데이트하고 다음 목록으로 넘어갑니다.")
                new_data = PublicData(id=update.id,
                pb_benefit_info=update.pb_benefit_info,
                pb_sub_business=update.pb_sub_business,
                pb_name=update.pb_name,
                pb_goal=update.pb_goal,
                pb_statute=update.pb_statute,
                pb_target=update.pb_target,
                pb_criteria=update.pb_criteria,
                pb_support_desc=update.pb_support_desc,
                pb_online_url=update.pb_online_url,
                pb_submit_step=update.pb_submit_step,
                pb_submit_date=update.pb_submit_date,
                pb_need_paper=update.pb_need_paper,
                pb_manage_department_type=update.pb_manage_department_type,
                pb_manage_department_name=update.pb_manage_department_name,
                pb_manage_department_detail_part=update.pb_manage_department_detail_part,
                pb_qna_department_name=update.pb_qna_department_name,
                pb_qna_department_call=update.pb_qna_department_call,
                pb_qna_department_url=update.pb_qna_department_url,
                pb_category=update.pb_category,
                pb_target_agerange=update.pb_target_agerange,
                pb_target_area=update.pb_target_area,
                pb_target_type=update.pb_target_type,
                pb_support_cate=update.pb_support_cate,
                pb_support_type=update.pb_support_type,
                pb_disclosuer=update.pb_disclosuer,
                pb_dinga_agerange=update.pb_dinga_agerange,
                pb_dinga_type=update.pb_dinga_type,
                pb_update_check="True")
                new_data.save()
                break
            elif data.id != update.id:
                # 다른 경우 지우거나 업데이트인데. 일단 업데이트 시켜놓아도 중복데이터가 계속 들어가지 않아서 괜찮다.
                print(update.id + "의 id를 가진 정책이 업데이트 됩니다.")
                new_data = PublicData(id=update.id,
                pb_benefit_info=update.pb_benefit_info,
                pb_sub_business=update.pb_sub_business,
                pb_name=update.pb_name,
                pb_goal=update.pb_goal,
                pb_statute=update.pb_statute,
                pb_target=update.pb_target,
                pb_criteria=update.pb_criteria,
                pb_support_desc=update.pb_support_desc,
                pb_online_url=update.pb_online_url,
                pb_submit_step=update.pb_submit_step,
                pb_submit_date=update.pb_submit_date,
                pb_need_paper=update.pb_need_paper,
                pb_manage_department_type=update.pb_manage_department_type,
                pb_manage_department_name=update.pb_manage_department_name,
                pb_manage_department_detail_part=update.pb_manage_department_detail_part,
                pb_qna_department_name=update.pb_qna_department_name,
                pb_qna_department_call=update.pb_qna_department_call,
                pb_qna_department_url=update.pb_qna_department_url,
                pb_category=update.pb_category,
                pb_target_agerange=update.pb_target_agerange,
                pb_target_area=update.pb_target_area,
                pb_target_type=update.pb_target_type,
                pb_support_cate=update.pb_support_cate,
                pb_support_type=update.pb_support_type,
                pb_disclosuer=update.pb_disclosuer,
                pb_dinga_agerange=update.pb_dinga_agerange,
                pb_dinga_type=update.pb_dinga_type,
                pb_update_check="True")
                new_data.save()
                break
      
    publicdata_absent = publicdata.filter(pb_update_check = "False")
    publicdata_absent.delete()   
    # 이렇게 진행하면 on_delete=CASCADE도 작용
    pass



def deletemachine(request):
    publicdata = PublicData.objects.all().order_by("pb_name")
    hello = []
    hello2 = []
    for i in publicdata:
        for j in publicdata:
            if i.id!=None and j.id!=None:   
                if i.id != j.id and i.pb_name == j.pb_name and i.pb_target_area == j.pb_target_area:
                    #왠만하면 pb_department_name이 긴걸 지우면 더 큰 관할 기관 정책이 남게된다.
                    if len(i.pb_manage_department_name) > len(j.pb_manage_department_name) and j.pb_manage_department_name!="":
                        hello.append(i.id)
                        print(f"{i.pb_name} 정책이 지워집니다. 관할기관은 {i.pb_manage_department_name}입니다.")
                        i.delete()
                        publicdata.filter(id=i.id).delete()
                    else:
                        hello.append(j.id)
                        print(f"{j.pb_name} 정책이 지워집니다. 관할기관은 {j.pb_manage_department_name}입니다.")
                        publicdata.filter(id=j.id).delete()
                else:
                    pass
            else:
                pass
    print(hello)
    print(hello2)

    
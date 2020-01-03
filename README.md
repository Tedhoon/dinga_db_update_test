```sql




DELETE FROM public_publicdata WHERE pb_disclosuer='미표출';

delete from public_publicdata where pb_name like '%금연%';
delete from public_publicdata where pb_name like '%흡연%';
delete from public_publicdata where pb_name like '%자살%';
delete from public_publicdata where pb_name like '%심뇌%';
delete from public_publicdata where pb_name like '%고령%';
delete from public_publicdata where pb_name like '%고혈%';
delete from public_publicdata where pb_name like '%군인%';

insert into publicdata_temp
select * from public_publicdata where pb_name like '%아동%';
delete from public_publicdata where pb_name like '%아동%';
insert into publicdata_temp
select * from public_publicdata where pb_name like '%유아%';
delete from public_publicdata where pb_name like '%유아%';
insert into publicdata_temp
select * from public_publicdata where pb_name like '%육아%';
delete from public_publicdata where pb_name like '%육아%';
insert into publicdata_temp
select * from public_publicdata where pb_name like '%출산%';
delete from public_publicdata where pb_name like '%출산%';
insert into publicdata_temp
select * from public_publicdata where pb_name like '%결혼%';
delete from public_publicdata where pb_name like '%결혼%';
insert into publicdata_temp
select * from public_publicdata where pb_name like '%임신%';
delete from public_publicdata where pb_name like '%임신%';
insert into publicdata_temp
select * from public_publicdata where pb_name like '%출생%';
delete from public_publicdata where pb_name like '%출생%';
insert into publicdata_temp
select * from public_publicdata where pb_name like '%임산부%';
delete from public_publicdata where pb_name like '%임산부%';
insert into publicdata_temp
select * from public_publicdata where pb_name like '%어린이%';
delete from public_publicdata where pb_name like '%어린이%';

DELETE FROM public_publicdata WHERE pb_target_agerange LIKE '노년기';

insert into publicdata_temp
select * from public_publicdata where pb_category like '%예방%' and pb_target_agerange like '%유아%' and pb_support_cate like '%의료%';
delete from public_publicdata where pb_category like '%예방%' and pb_target_agerange like '%유아%' and pb_support_cate like '%의료%';

delete from public_publicdata where pb_category like '%육아%' and pb_category like '%보훈%';

delete from public_publicdata where pb_category like '%평생%';

delete from public_publicdata where pb_category like '%행정기관정보%';

delete from public_publicdata where pb_category like '%대학%';

delete from public_publicdata where pb_category like '%기술%';

insert into publicdata_temp
select * from public_publicdata where pb_category like '%육아%';
delete from public_publicdata where pb_category like '%육아%';




delete from public_publicdata;

insert into public_publicdata
select * from publicdata_temp;

drop table publicdata_temp;


```

```sql

UPDATE public_publicdata SET pb_dinga_agerange = pb_dinga_agerange||'|임신·출산' 
WHERE 
(
pb_name like '%임신%' 
or pb_name like '%임산%'
or pb_name like '%출산%'
or pb_name like '%출생%'
or pb_name like '%산모%'

or pb_goal like '%임신%'
or pb_goal like '%임산%'
or pb_goal like '%출산%'
or pb_goal like '%출생%'
or pb_goal like '%산모%'

or pb_target like '%임신%' 
or pb_target like '%임산%'
or pb_target like '%출산%'
or pb_target like '%출생%'
or pb_target like '%산모%'

or pb_category like '%출산%'
or pb_category like '%임산%'
)

and pb_dinga_agerange not like ''
and pb_name not like '%아이돌봄%'
and pb_name not like '%보육%'
and pb_name not like '%소년소녀%';



UPDATE public_publicdata SET pb_dinga_agerange = pb_dinga_agerange||'임신·출산' 
WHERE 
(pb_name like '%임신%' 
or pb_name like '%임산%'
or pb_name like '%출산%'
or pb_name like '%출생%'
or pb_name like '%산모%'


or pb_goal like '%임신%'
or pb_goal like '%임산%'
or pb_goal like '%출산%'
or pb_goal like '%출생%'
or pb_goal like '%산모%'

or pb_target like '%임신%' 
or pb_target like '%임산%'
or pb_target like '%출산%'
or pb_target like '%출생%'
or pb_target like '%산모%'

or pb_category like '%출산%')

and pb_dinga_agerange like ''
and pb_name not like '%아이돌봄%'
and pb_name not like '%보육%'
and pb_name not like '%소년소녀%';



UPDATE public_publicdata SET pb_dinga_agerange = pb_dinga_agerange||'|영·유아' 
WHERE 
(
pb_name like '%유아%'
or pb_name like '%육아%'
or pb_name like '%보육%'
or pb_name like '%신생%' 
or pb_name like '%아이돌봄%'
or pb_name like '%어린이%'
or pb_name like '%양육%'


or pb_target_agerange like '영·유아'
or pb_target like '%유아%'
)
and pb_dinga_agerange not like ''
and pb_name not like '%아동%';


UPDATE public_publicdata SET pb_dinga_agerange = pb_dinga_agerange||'영·유아' 
WHERE 
(
pb_name like '%유아%'
or pb_name like '%육아%'
or pb_name like '%보육%'
or pb_name like '%신생%' 
or pb_name like '%아이돌봄%'
or pb_name like '%어린이%'
or pb_name like '%양육%'
 
or pb_target_agerange like '영·유아'
or pb_target like '%유아%'
)
and pb_dinga_agerange like ''
and pb_name not like '%아동%';
 


UPDATE public_publicdata SET pb_dinga_agerange = pb_dinga_agerange||'|아동·청소년' 
WHERE 
(
pb_name like '%어린이%'
or pb_name like '%아동%'
or pb_name like '%소년%'
or pb_name like '%소녀%'
or pb_name like '%자녀%'
or pb_name like '%학교%'
or pb_name like '%어린이%'



or pb_category like '%중학교%' 
or pb_target_agerange like '아동·청소년'

or pb_goal like '%소년%'
or pb_goal like '%소녀%'
)
and pb_dinga_agerange not like '';





UPDATE public_publicdata SET pb_dinga_agerange = pb_dinga_agerange||'아동·청소년' 
WHERE 
(
pb_name like '%어린이%'
or pb_name like '%아동%'
or pb_name like '%소년%'
or pb_name like '%소녀%'
or pb_name like '%자녀%'
or pb_name like '%학교%'
or pb_name like '%어린이%'


or pb_target_agerange like '아동·청소년'

or pb_goal like '%소년%'
or pb_goal like '%소녀%'
)
and pb_dinga_agerange like '';

 
 

```

```sql
UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'|다문화' 
WHERE
(
pb_name like '%다문화%'
or pb_name like '%이민%'
or pb_goal like '%다문화%'
or pb_category like '%다문화%'
)
and pb_dinga_type not like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'다문화' 
WHERE
(
pb_name like '%다문화%'
or pb_name like '%이민%'
or pb_goal like '%다문화%'
or pb_category like '%다문화%'
)
and pb_dinga_type like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'|다자녀' 
WHERE
(
pb_name like '%다자녀%'
or pb_name like '%다둥%'
or pb_goal like '%다자녀%'
or pb_category like '%다자녀%'
)
and pb_dinga_type not like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'다자녀' 
WHERE
( 
pb_name like '%다자녀%'
or pb_name like '%다둥%'
or pb_goal like '%다자녀%'
or pb_category like '%다자녀%'
)
and pb_dinga_type like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'|소년·소녀' 
WHERE
(
pb_name like '%소년소녀%'
or pb_goal like '%소년소녀%'
or pb_category like '%소년소녀%'
)
and pb_dinga_type not like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'소년·소녀' 
WHERE
( 
pb_name like '%소년소녀%'
or pb_goal like '%소년소녀%'
or pb_category like '%소년소녀%'
)
and pb_dinga_type like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'|입양' 
WHERE
(
pb_name like '%입양%'
or pb_goal like '%입양아%'
or pb_category like '%입양%'
)
and pb_dinga_type not like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'입양' 
WHERE
(
pb_name like '%입양%'
or pb_goal like '%입양아%'
or pb_category like '%입양%'
)
and pb_dinga_type like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'|장애인' 
WHERE
(
pb_name like '%장애%'
or pb_name like '%난청%'
or pb_goal like '%장애%'
or pb_category like '%장애%'
)
and pb_dinga_type not like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'장애인' 
WHERE
(
pb_name like '%장애%'
or pb_name like '%난청%'
or pb_goal like '%장애%'
or pb_category like '%장애%'
)
and pb_dinga_type like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'|저소득' 
WHERE
(
pb_name like '%저소득%'
or pb_goal like '%저소득%'
or pb_goal like '%중위소득%'
or pb_category like '%저소득%'
)
and pb_dinga_type not like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'저소득' 
WHERE
(
pb_name like '%저소득%'
or pb_goal like '%저소득%'
or pb_goal like '%중위소득%'
or pb_category like '%저소득%'
)
and pb_dinga_type like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'|폭력' 
WHERE
(
pb_category like '%폭력%'
or pb_name like '%폭력%'
or pb_name like '%학대%'
)
and pb_dinga_type not like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'폭력' 
WHERE
(
pb_category like '%폭력%'
or pb_name like '%폭력%'
or pb_name like '%학대%'
)
and pb_dinga_type like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'|한부모·조손' 
WHERE
(
pb_name like '%한부모%'
or pb_name like '%조손%'
or pb_goal like '%한부모%'
or pb_goal like '%조손%'
or pb_goal like '%한부모%'
or pb_category like '%조손%'
)
and pb_dinga_type not like '';


UPDATE public_publicdata SET pb_dinga_type = pb_dinga_type||'한부모·조손' 
WHERE
(
pb_name like '%한부모%'
or pb_name like '%조손%'
or pb_goal like '%한부모%'
or pb_goal like '%조손%'
or pb_goal like '%한부모%'
or pb_category like '%조손%'
)
and pb_dinga_type like '';



```

```sql
<<중복데이터 분류 쿼리>>

1. 전국이 포함된 데이터 중 행안부~ 이런 것만 조회합니다. 335개
SELECT *
FROM public_publicdata
WHERE 
pb_target_area like '전국' 
and (
pb_manage_department_name like '%부%'
or pb_manage_department_name like '%체육인재%'
or pb_manage_department_name like '%건설%'
or pb_manage_department_name like '%경찰%'
or pb_manage_department_name like '%공정거래%'
or pb_manage_department_name like '%국가%'
or pb_manage_department_name like '%국립%'
or pb_manage_department_name like '%국민%'
or pb_manage_department_name like '%국제%'
or pb_manage_department_name like '%근로%'
or pb_manage_department_name like '%녹색%'
or pb_manage_department_name like '%대한%'
or pb_manage_department_name like '%도로%'
or pb_manage_department_name like '%독립%'
or pb_manage_department_name like '%문화재청%'
or pb_manage_department_name like '%방송%'
or pb_manage_department_name like '%북한%'
or pb_manage_department_name like '%사회보장%'
or pb_manage_department_name like '%새만금%'
or pb_manage_department_name like '%시청자%'
or pb_manage_department_name like '%식품의약%'
or pb_manage_department_name like '%예금보험%'
or pb_manage_department_name like '%재외동포%'
or pb_manage_department_name like '%축산물%'
or pb_manage_department_name like '%통계청%'
or pb_manage_department_name like '%학교법인%'
or pb_manage_department_name like '%한국%'
or pb_manage_department_name like '%해양환경%'
)

and pb_manage_department_name not like '%부산%'
and pb_manage_department_name not like '%부평%'
and pb_manage_department_name not like '%부안%'

order by pb_manage_department_name asc;

2. 전국이 포함된 데이터 중 위의 데이터가 아닌 것들을 조회합니다 754개

SELECT *
FROM public_publicdata
WHERE 
pb_target_area like '전국' 
and not(
pb_manage_department_name like '%고용노동부%'
or pb_manage_department_name like '%과학기술정보통신부%'
or pb_manage_department_name like '%기획재정부%'
or pb_manage_department_name like '%교육부%'
or pb_manage_department_name like '%국토교통부%'
or pb_manage_department_name like '%농림축산식품부%'
or pb_manage_department_name like '%문화체육관광부%'
or pb_manage_department_name like '%법무부%'
or pb_manage_department_name like '%보건복지부%'
or pb_manage_department_name like '%여성가족부%'
or pb_manage_department_name like '%중소벤처기업부%'
or pb_manage_department_name like '%통일부%'
or pb_manage_department_name like '%해양수산부%'
or pb_manage_department_name like '%행정안전부%'
or pb_manage_department_name like '%환경부%'
or pb_manage_department_name like '%체육인재%'
or pb_manage_department_name like '%건설%'
or pb_manage_department_name like '%경찰%'
or pb_manage_department_name like '%공정거래%'
or pb_manage_department_name like '%국가%'
or pb_manage_department_name like '%국립%'
or pb_manage_department_name like '%국민%'
or pb_manage_department_name like '%국제%'
or pb_manage_department_name like '%근로%'
or pb_manage_department_name like '%녹색%'
or pb_manage_department_name like '%대한%'
or pb_manage_department_name like '%도로%'
or pb_manage_department_name like '%독립%'
or pb_manage_department_name like '%문화재청%'
or pb_manage_department_name like '%방송%'
or pb_manage_department_name like '%북한%'
or pb_manage_department_name like '%사회보장%'
or pb_manage_department_name like '%새만금%'
or pb_manage_department_name like '%시청자%'
or pb_manage_department_name like '%식품의약%'
or pb_manage_department_name like '%예금보험%'
or pb_manage_department_name like '%재외동포%'
or pb_manage_department_name like '%축산물%'
or pb_manage_department_name like '%통계청%'
or pb_manage_department_name like '%학교법인%'
or pb_manage_department_name like '%한국%'
or pb_manage_department_name like '%해양환경%'
)
order by pb_manage_department_name asc;


3. 2번 친구들의 pb_target_area를 다 pb_manage_department_name으로 치환해줍니다.


UPDATE public_publicdata SET pb_target_area = pb_manage_department_name
WHERE 
pb_target_area like '전국' 
and not(
pb_manage_department_name like '%고용노동부%'
or pb_manage_department_name like '%과학기술정보통신부%'
or pb_manage_department_name like '%기획재정부%'
or pb_manage_department_name like '%교육부%'
or pb_manage_department_name like '%국토교통부%'
or pb_manage_department_name like '%농림축산식품부%'
or pb_manage_department_name like '%문화체육관광부%'
or pb_manage_department_name like '%법무부%'
or pb_manage_department_name like '%보건복지부%'
or pb_manage_department_name like '%여성가족부%'
or pb_manage_department_name like '%중소벤처기업부%'
or pb_manage_department_name like '%통일부%'
or pb_manage_department_name like '%해양수산부%'
or pb_manage_department_name like '%행정안전부%'
or pb_manage_department_name like '%환경부%'
or pb_manage_department_name like '%체육인재%'
or pb_manage_department_name like '%건설%'
or pb_manage_department_name like '%경찰%'
or pb_manage_department_name like '%공정거래%'
or pb_manage_department_name like '%국가%'
or pb_manage_department_name like '%국립%'
or pb_manage_department_name like '%국민%'
or pb_manage_department_name like '%국제%'
or pb_manage_department_name like '%근로%'
or pb_manage_department_name like '%녹색%'
or pb_manage_department_name like '%대한%'
or pb_manage_department_name like '%도로%'
or pb_manage_department_name like '%독립%'
or pb_manage_department_name like '%문화재청%'
or pb_manage_department_name like '%방송%'
or pb_manage_department_name like '%북한%'
or pb_manage_department_name like '%사회보장%'
or pb_manage_department_name like '%새만금%'
or pb_manage_department_name like '%시청자%'
or pb_manage_department_name like '%식품의약%'
or pb_manage_department_name like '%예금보험%'
or pb_manage_department_name like '%재외동포%'
or pb_manage_department_name like '%축산물%'
or pb_manage_department_name like '%통계청%'
or pb_manage_department_name like '%학교법인%'
or pb_manage_department_name like '%한국%'
or pb_manage_department_name like '%해양환경%'
)


```

```sql
-> 본 쿼리는 중복데이터 +  전국을 대상으로 하는 정책일 때 온라인 신청이 가능한 친구들을
전국 하나 빼고 다 지워주는 쿼리입니당

1. 위의 친구들을 찾습니다.
---조회---
SELECT *
FROM public_publicdata
WHERE (pb_name IN (
SELECT pb_name
FROM public_publicdata
GROUP BY pb_name
HAVING COUNT(*) > 1
))
and pb_submit_step like '%온라인%'
and pb_target_area like '전국'

order by pb_name asc

------> 나온 목록들 (얼마안됨)

가정양육수당 지원
기초생활보장 수급자 교육급여 지원
만 0-5세 보육료 지원
만 3~5세 유치원 유아 학비 지원
산모 신생아 건강관리 서비스 제공
아이돌봄 서비스 제공
여성장애인 출산비용 지원
장애인 정보화 교육
저소득층 자녀 고교 학비 지원
지역공동체 일자리 제공
청소년 산모 의료비 지원
초, 중, 고 학생 교육 정보화 지원
행복출산 원스톱서비스 제공

2. 이 친구들을 조회해봅니다.
SELECT *
FROM public_publicdata
WHERE pb_name like '%가정양육수당 지원%'
or pb_name like '%기초생활보장 수급자 교육급여 지원%'
or pb_name like '%만 0-5세 보육료 지원%'
or pb_name like '%만 3~5세 유치원 유아 학비 지원%'
or pb_name like '%산모 신생아 건강관리 서비스 제공%'
or pb_name like '%아이돌봄 서비스 제공%'
or pb_name like '%여성장애인 출산비용 지원%'
or pb_name like '%장애인 정보화 교육%'
or pb_name like '%저소득층 자녀 고교 학비 지원%'
or pb_name like '%지역공동체 일자리 제공%'
or pb_name like '%청소년 산모 의료비 지원%'
or pb_name like '%초, 중, 고 학생 교육 정보화 지원%'
or pb_name like '%행복출산 원스톱서비스 제공%'
order by pb_name asc;


========> 총 1686개...;;;;;;;;;;;;;; 이게 문제였군요!


3. 이 친구들을 전국 빼고 다 지워버립시다. (지울 것 1672개)



DELETE FROM public_publicdata
WHERE (pb_name like '%가정양육수당 지원%'
or pb_name like '%기초생활보장 수급자 교육급여 지원%'
or pb_name like '%만 0-5세 보육료 지원%'
or pb_name like '%만 3~5세 유치원 유아 학비 지원%'
or pb_name like '%산모 신생아 건강관리 서비스 제공%'
or pb_name like '%아이돌봄 서비스 제공%'
or pb_name like '%여성장애인 출산비용 지원%'
or pb_name like '%장애인 정보화 교육%'
or pb_name like '%저소득층 자녀 고교 학비 지원%'
or pb_name like '%지역공동체 일자리 제공%'
or pb_name like '%청소년 산모 의료비 지원%'
or pb_name like '%초, 중, 고 학생 교육 정보화 지원%'
or pb_name like '%행복출산 원스톱서비스 제공%'
)
and not pb_target_area = '전국';

```

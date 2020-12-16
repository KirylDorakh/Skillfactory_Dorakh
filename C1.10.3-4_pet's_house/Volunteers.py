from house_for_pets import Volunteer

vasiliy_nikolaev = Volunteer('Василий Николаев', 'Москва', 'Наставник')
nikolay_sobolev = Volunteer('Николай Соболев', 'Питер', 'Спикер')
aleksey_kvashonkin = Volunteer('Алексей Квашонкин', 'Киев', 'Ученик')
alex_andreev = Volunteer('Алексей Андреев', 'Львов', 'Мастер')

corporate_list = [vasiliy_nikolaev, nikolay_sobolev, aleksey_kvashonkin, alex_andreev]

print('\nСписок для корпоратива:')
for volonter in corporate_list:
    print(volonter.info())
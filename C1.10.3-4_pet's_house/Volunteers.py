from house_for_pets import Volunteer, GuestList

vasiliy_nikolaev = Volunteer('Василий Николаев', 'Москва', 'Наставник')
nikolay_sobolev = Volunteer('Николай Соболев', 'Питер', 'Спикер')
aleksey_kvashonkin = Volunteer('Алексей Квашонкин', 'Киев', 'Ученик')
alex_andreev = Volunteer('Алексей Андреев', 'Львов', 'Мастер')

list_of_guest = GuestList()

corporate_list = [vasiliy_nikolaev, nikolay_sobolev, aleksey_kvashonkin, alex_andreev]

for volonter in corporate_list:
    list_of_guest.getGuest(volonter)
    
print(list_of_guest.getGuestList())

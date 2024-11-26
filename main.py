import json

file = "dump.json"
nomer = str(input("Введите номер профессии: "))
skills = False

with open(file, 'r', encoding='utf-8') as file: 
    data = json.load(file) 
    for skill in data:
        if skill.get("model") == "data.skill":
            if skill["fields"].get("code") == nomer :
                sk_code = skill["fields"].get("code")
                sk_title = skill["fields"].get("title")
                skills = True

                for profecia in data :
                    if profecia.get("model") == "data.specialty":
                        prof_code = profecia["fields"].get("code")
                        if prof_code in nomer:
                            prof_title = profecia["fields"].get("title")
                            prof_type = profecia["fields"].get("c_type")
                            break
            
                break

if not skills:
    print("=============== Не Найдено ===============") 
    
    
else:
    print("=============== Найдено ===============") 
    print(f"{prof_code} >> Специальность {prof_title} , {prof_type}")
    print(f"{sk_code} >> Квалификация {sk_title}")
    
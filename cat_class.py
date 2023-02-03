from cat import Cat

#импортируем и зоздаем объект Cat

cat_1 = Cat(name='Барон', gender='мальчик', age=2)
cat_2 = Cat(name='Сэм', gender='мальчик', age=2)

print(cat_1.getName(),
      cat_1.getGender(),
      cat_1.getAge())
print(cat_2.getName(),
      cat_2.getGender(),
      cat_2.getAge())
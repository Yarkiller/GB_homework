"""Задача 1. Урок информатики 2
Что нужно сделать
В прошлый раз учитель написал программу, которая выводит числа в формате плавающей точки, однако он вспомнил,
 что не учёл одну важную вещь: числа-то могут идти от нуля.

Задано положительное число x (x > 0). Ваша задача — преобразовать его в формат плавающей точки,
 то есть x = a * 10^b, где 1 ≤ a < 10. Обратите внимание, что x теперь больше нуля,
  а не больше единицы. Обеспечьте контроль ввода."""

# x = input('Введите x: ')
# print(f'Формат плавающей точки: x ={'.'join(x[])}')
# Функция для преобразования числа в формат плавающей точки
# import math
#
#
# def convert_to_float_point(x):
#     power = int(math.log10(x))
#     coefficient = x / (10 ** power)
#     return coefficient, power
#
#
# x = float(input("Введите число: "))
# if x > 0:
#     coefficient, power = convert_to_float_point(x)
#     print(f"Формат плавающей точки: {coefficient} * 10^({power})")
# else:
#     print("Число должно быть положительным.")
########################################################################################################################
"""Задача 2. Функция максимума
Что нужно сделать
Юра пишет различные полезные функции для Python, чтобы остальным программистам стало проще работать.
 Он захотел написать функцию, которая будет находить максимум из перечисленных чисел.
  Функция для нахождения максимума из двух чисел у него уже есть. Юра задумался: может быть,
   её можно как-то использовать для нахождения максимума уже от трёх чисел?

Помогите Юре написать программу, которая находит максимум из трёх чисел.
 Для этого используйте только функцию нахождения максимума из двух чисел.

По итогу в программе должны быть реализованы две функции:

1. maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
2. maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх);
 при этом она должна использовать для сравнений первую функцию maximum_of_two."""

# def maximum_of_two(first, second):
#     """It's founding maximum of two numbers."""
#     return first if first > second else second  # return max(first, second)
#
#
# def maximum_of_three(first, second, third):
#     local_max = maximum_of_two(first, second)
#     return local_max if local_max > third else third
#######################################################################################################################
"""Задача 3. Число наоборот 2
Что нужно сделать
Пользователь вводит два числа: N и K. Напишите программу, которая заменяет каждое число на число,
 которое получается из исходного записью его цифр в обратном порядке, затем складывает их,
  снова переворачивает и выводит ответ на экран."""

# first_num = int(input('Введите первое число: ')[::-1])
# second_num = int(input('Введите второе число: ')[::-1])
# print(first_num)
# print(f'Первое число наоборот: {first_num}')
# print(f'Второе число наоборот: {second_num}')
# sum = first_num + second_num
# print(f'Сумма: {sum}\nСумма наоборот: {str(sum)[::-1]}')
########################################################################################################################
"""Задача 4. Недоделка 2
Что нужно сделать
Вы всё так же работаете в конторе по разработке игр и смотрите различные программы прошлого горе-программиста.
 В одной из игр для детей, связанной с мультяшной работой с числами, вам нужно было написать код согласно следующим
  условиям: программа получает на вход два числа; в первом числе должно быть не менее трёх цифр,
   во втором — не менее четырёх, иначе программа выдаёт ошибку. Если всё нормально,
    то в каждом числе первая и последняя цифры меняются местами, а затем выводится их сумма.

И тут вы натыкаетесь на программу, которая была написана предыдущим программистом и которая как раз решает такую задачу.
 Однако старший программист попросил вас немного переписать этот код, чтобы он не выглядел так ужасно.
  Да и вам самим становится, мягко говоря, не по себе от него.

Постарайтесь разделить логику кода на три отдельные логические части (функции):

count_numbers — получает число и возвращает количество цифр в числе;
change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
main — функция ничего не получает на вход, внутри она запрашивает нужные данные от пользователя,
 выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи (проверки и изменения двух чисел).
Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше.
 Также сделайте, чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы."""

# def count_numbers(number: str) -> int:
#     """It's not correct but to do the loop or to use integers is worse, isn't it?"""
#     return len(number)
#
#
# def change_number(mod_number: str) -> int:
#     """ It changes the first and last digit of mod_number."""
#     mod_number = list(str(mod_number))
#     mod_number[0], mod_number[-1] = mod_number[-1], mod_number[0]
#     return int(''.join(mod_number))
#
#
# def main()-> None:
#     """The main function. It h"""
#     num_1 = input("Введите первое число: ")
#     if count_numbers(num_1) < 2:
#         print("В первом числе меньше трёх цифр.")
#         return
#     num_1 = change_number(num_1)
#     print('Изменённое первое число:', num_1)
#     num_2 = input("Введите второе число: ")
#     if count_numbers(num_2) < 3:
#         print("Во втором числе меньше трёх цифр.")
#         return
#     num_2 = change_number(num_2)
#     print('Изменённое второе число:', num_2)
#     print('Сумма чисел:', num_1 + num_2)
#
#
# main()
########################################################################################################################
"""Задача 5. Маятник
Что нужно сделать
Известно, что амплитуда качающегося маятника с каждым разом затухает на 8,4% от амплитуды предыдущего колебания.
 Если качнуть маятник, то, строго говоря, он не остановится никогда, просто амплитуда будет постоянно уменьшаться
  до тех пор, пока мы не сочтём такой маятник остановившимся. Напишите программу, определяющую,
   сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится.

Программа получает на вход начальную амплитуду колебания в сантиметрах и конечную амплитуду колебаний,
 которая считается остановкой маятника. Обеспечьте контроль ввода."""

# amplitude_st = float(input('Введите начальную амплитуду: '))
# stop_ampl = float(input('Введите амплитуду остановки: '))
# counter = 0
# while amplitude_st > stop_ampl:
#     counter += 1
#     amplitude_st -= amplitude_st  * 8.4/100
# print(f'Маятник считается остановившимся через {counter} колебаний ')
########################################################################################################################
"""Задача 6. Яйца
Что нужно сделать
В рамках программы колонизации Марса компания «Спейс Инжиниринг» вывела особую породу черепах, которые,
 по задумке, должны размножаться, откладывая яйца в марсианском грунте. Откладывать яйца слишком близко
  к поверхности опасно из-за радиации, а слишком глубоко — из-за давления грунта и недостатка кислорода.
   Вообще, факторов очень много, но специалисты проделали большую работу и предположили,
    что уровень опасности для черепашьих яиц рассчитывается по формуле: D = x^3 − 3x^2 − 12x + 10,
     где x — глубина кладки в метрах, а D — уровень опасности в условных единицах. Для тестирования гипотезы
      нужно взять пробу грунта на безопасной, согласно формуле, глубине.

Напишите программу, находящую такое значение глубины х, при котором уровень опасности как можно более близок к нулю.
 На вход программе подаётся максимально допустимое отклонение уровня опасности от нуля,
  а программа должна рассчитать приблизительное значение х, удовлетворяющее этому отклонению.
   Известно, что глубина точно больше нуля и меньше четырёх метров. Обеспечьте контроль ввода. """

# def danger_level(x):
#     """It looks for level of danger"""
#     return x**3 - 3*x**2 - 12*x + 10
# 
# 
# def find_safe_depth(max_level):
#     """It looks for safe depth by binary search"""
#     left = 0
#     right= 4
#     while right - left > 1e-15:
#         mid = (left + right) / 2
#         if danger_level(mid) >= max_level:
#             left = mid
#         else:
#             right = mid
#     return mid
# 
# 
# max_danger = float(input("Введите максимально допустимый уровень опасности: "))
# safe_depth = find_safe_depth(max_danger)
# print(f"Приблизительная глубина безопасной кладки: {safe_depth} м")

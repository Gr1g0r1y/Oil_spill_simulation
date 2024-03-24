**#|#|#|#|#   *EN*   #|#|#|#|#**

We have created a program to simulate the process of spreading an oil slick. The Python programming language was chosen to write the program, since this language has a huge number of libraries, both built-in and created by other people, which help a lot when writing programs.

The program is created according to the rules of object-oriented programming, that is, the program is divided into objects (classes), each of which has its own set of functions and properties. For example, the program has an “Oil” class that is responsible for an oil slick, and this class has functions: “draw”, which graphically displays the slick by parameters, “get_new_V”, in which all calculations are performed and the results of which are used in the draw function, and so on. The written program can be divided into 2 main blocks: the first is responsible for the table of values, and the second displays a spot based on these values.

Mainly 2 external libraries were used to write the code. The first of them is PyGame. It was used to graphically depict the oil spill process, as this library has built-in objects, the use of which facilitates the programming process for the developer and improves the user experience. The second is PyQt5, which was used to create a table in which the user can write data to change various parameters of the initial conditions of an oil spill. This library allows you to create a simple and intuitive interface.

To run the program, you need to run the file “main_menu.py ”, it is also necessary to pre-install the libraries: PyGame, PyQt5. A window will appear in front of you in which there will be standard values for all variables on which oil spreading depends (density, viscosity of oil and water, wind and current speeds, geographical latitude of the oil spill site, etc.). They can be changed depending on what parameters oil, water and the environment have taken by the user. 

![img1](https://github.com/Gr1g0r1y/Oil_spill_simulation/assets/131547274/282f5ee0-88fa-42f3-afcc-7d939f28caca)

After entering all the data, you need to click the “Start generation” button, and the simulation will start in a new window (for ease of display, the total vector of the spreading direction of the spot is located horizontally). The scale will be written in the upper right corner, and in the lower left some parameters of the system, namely t is the time elapsed since the oil spill stopped, L is the length of the spot at a certain point in time and S is the area of the spilled oil.

![img2](https://github.com/Gr1g0r1y/Oil_spill_simulation/assets/131547274/5aa935f6-8879-4a7f-b7c6-e8aa997887e3)

Read more in the our article: [insert link]

**#|#|#|#|#   *RU*   #|#|#|#|#**

Нами была создана программа для моделирования процесса растекания нефтяного пятна. Для написания программы был выбран язык программирования Python, так как у этого языка есть огромное множество библиотек как встроенных, так и созданных другими людьми, которые очень сильно помогают при написании программ.

Программа создана по правилам объектно ориентированного программирования, то есть программа разделена на объекты (классы), каждый из которых имеет свой набор функций и свойств. К примеру в программе есть класс “Oil”, который отвечает за нефтяное пятно, и у этого класса есть функции: “draw”, которая графически отображает пятно по параметрам, “get_new_V”, в которой проводятся все вычисления и результаты которых используются в функции draw, и так далее. Написанную программу можно разделить на 2 основных блока: первый отвечает за таблицу значений, а второй отображает по этим значениям пятно.

Для написания кода были использованы в основном 2 внешние библиотеки. Первая из них – PyGame. Она использовалась для того, чтобы графически изобразить процесс разлива нефти, так как эта библиотека имеет встроенные объекты, использование которых облегчает процесс программирования для разработчика и улучшает пользовательский опыт. Вторая – PyQt5, с помощью которой создавалась таблица, в которую пользователь может записывать данные для изменения различных параметров начальных условий разлива нефти. Данная библиотека позволяет создавать простой и понятный интерфейс.

Для запуска программы необходимо запустить файл “main_menu.py”, также необходимо предварительно установить библиотеки: PyGame, PyQt5. Перед вами появится окно, в котором будут стандартные значения для всех переменных, от которых зависит растекание нефти (плотность, вязкость нефти и воды, скорости ветра и течения, географическая широта места разлива нефти и др.). Их можно менять в зависимости от того, какими параметрами обладают нефть, вода и окружающая среда, взятые пользователем. 

![img1](https://github.com/Gr1g0r1y/Oil_spill_simulation/assets/131547274/282f5ee0-88fa-42f3-afcc-7d939f28caca)

После ввода всех данных, необходимо нажать кнопку “Начать генерацию”, и симуляция запустится в новом окне (для удобства отображения, суммарный вектор направления растекания пятна располагается горизонтально). В правом верхнем углу будет написан масштаб, а в левом нижнем некоторые параметры системы, а именно t – время прошедшее с момента прекращения выливания нефти, L – длина пятна в определенный момент времени и S – площадь разлившейся нефти.

![img2](https://github.com/Gr1g0r1y/Oil_spill_simulation/assets/131547274/5aa935f6-8879-4a7f-b7c6-e8aa997887e3)

Подробнее в нашей статье: [вставить ссылку]

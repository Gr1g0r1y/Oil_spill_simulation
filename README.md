      *1) Introduction*   
Using these formulas, a program was created to simulate the oil slick plant process. The Python programming language was chosen to write the program, since this language has a huge number   of libraries, both built-in and created by other people, with which you can write realistic, efficient,
a program that is understandable for the average user.
The program was created according to the rules of object-oriented programming, that is, the program is divided into objects (classes), each of which has its own set of functions and         properties. For example, the program has the “Oil” class, which is responsible for the oil slick itself, and this class has the following functions: “draw”,
which graphically displays the spot by parameters, “get_new_V”, in which all calculations are carried out and the results of which are used in the draw function, and others. The written     program can be divided into 2 main blocks: the first of them creates a table of values, and the second displays a spot based on these values.
Mainly 2 libraries were used to write the code. The first of them is PyGame, in order to depict the process of an oil spill itself, since this library has built-in objects, the use of       which makes the programming process easier for the developer and improves the user experience. The second is PyQt5,
which was used to create a table in which the user can record data to change various parameters of the initial conditions of an oil spill. This library allows you to create a simple and     intuitive interface.
      *2) How to use*
To run the program, you need to open the “menu.py” file and run it. A window will appear in front of you (screenshot below) in which there will be standard values ​​for all variables on       which the spreading of oil depends (a table like in the program with an explanation of the variables, add it and a link to the table). They can be changed depending on
what parameters do oil, water and the environment have, taken by the user.

![image](https://github.com/Gr1g0r1y/Oil_spill_simulation/assets/131547274/5af7608d-dc15-4382-9426-c9c622b66aa1)

After entering all the data, you must click the “Start generation” button and the program will start. The scale will be written in the upper right corner, and in the lower left some         parameters of the slick, which we considered the most important, namely t - the time elapsed since the beginning of the slick spill,
L is the length of the slick at a certain point in time (hereinafter in formula (16)) and S is the area of ​​spilled oil (hereinafter in formula (17)).
  
![image](https://github.com/Gr1g0r1y/Oil_spill_simulation/assets/131547274/7b226df0-0b31-4b84-89a1-6c9ca9a48935)

      *3) How it works*

  ![image](https://github.com/Gr1g0r1y/Oil_spill_simulation/assets/131547274/42fa4056-ee45-40a5-800a-e20114b8f8b2)
  
Designations: O - the center of the circle, K - the exact beginning of the spreading of the spot, KP and KQ - tangents to the circle with the center at point O and the radius at a certain   point in time.
Having considered the movement of an oil slick on the surface of the water, described in article [4], a model was chosen that most closely describes this movement, namely,
that the spot itself expands around the circumference, and the current carries it away, and the shape of the spot is approximately described as tangents from the point of release of the     spot to a floating and simultaneously expanding circle. Let's consider the process of displaying a spot. Based on formulas (1 – 3) we obtain that:
 
 (13)   S_x = (u_d + U_0)t   S_y = (v_d + U_0)t   
 
Based on this, we find α through the tangent: α = arctan(S_y / S_x) and find that the coordinate of the center using formula (13):  
 
 (14)   x_centre = √(S_x^2 + S_y^2) / cos⁡α    

And find the radius of our circle:
 
 (15)   R = S_y / cos⁡a    

Now that we have found all the necessary data for constructing the spot, let’s find some parameters of the spot:
  
  1) length of the spot along the x-axis – L, using formulas (14) and (15):
  
     (16)   L = x_center + R = (S_y + √(S_x^2 + S_y^2 )) / cosa    
  
  2) spot area S (angles are indicated clockwise):
     
     (17) S = S_KPOQ + S_sector
    
    where S_sector is the area of ​​the PQO sector of the circle. Let's find the angle using formula (18) and substitute it into formula (19) and get the area of ​​the sector:
     
     (18) ∠POQ = 2π - 2 * (π / 2 - a) = π - 2a
     
     (19) S_sector = πR^2 * (∠POQ / 2π) = R^2 * ((π - 2a) / 2) = ((S_y + √(S_x^2 + S_y^2 )) / cosa)^2 * ((π - 2a) / 2)
      
    The area of ​​the quadrilateral KPOQ is equal to the area of ​​two triangles KOQ:
     
     (20) S_KPOQ = S_x * cos⁡α * S_y * cos⁡α
    
    By substituting formulas (20) and (19) into formula (17) we find the total area of ​​the spot.

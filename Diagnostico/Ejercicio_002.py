print("¿Cuál es tu nombre(s)?")
nombre = input()
print("¿Cuál es tu primer apellido?")
apellido_p = input()
print("¿Cuál es tu segundo apellido?")
apellido_m = input()
print("¿En qué año naciste?")   
anio = input()
print("¿En qué mes y día naciste? (en el siguiente formato “mm-dd”)")
dia_mes = input()

nombre_mayus= nombre.upper() +" "+apellido_p.upper()+" "+apellido_m.upper()
nombre_minus= nombre.lower() +" "+apellido_p.lower()+" "+apellido_m.lower()

print("A.   Este es tu nombre completo en mayúsculas:", nombre_mayus)
print("B.	Este es tu nombre completo en minúsculas:", nombre_minus)
print("C.	Esta es tu fecha de nacimiento:",dia_mes+"-"+anio)
anio_actual = 2022 
edad = anio_actual-(int(anio))
print("D.	Esta es tu edad:",edad)
print("E.	Tu nombre completo tiene _________ vocales.")
print("F.	Tu nombre completo tiene _________ letras.")
print("G.	¿Tu edad es un carácter de tipo número?")
if int(anio) == int :
    v_anio = True
    print(v_anio)
else :
    v_anio = False
    print(v_anio)
print("H.	¿Tu nombre completo es un carácter de tipo alfanumérico? ___True____ ")
print("I.	Tu edad en 10 años será:",edad+10)
print("J.	La media de tu edad actual y tu edad en 20 años es:", (edad + (edad+20))/2)

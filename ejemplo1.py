import os
os.system('cls')
participante1Str = input('nombre de l participante  1 -> ')
numeroP1Int = input( 'numero del participantye 1 -> ')
participante2Str =  input('nombre del particiante 2 -> ')
numeroP2Int = input( 'numero del participantye 2  -> ')
var_acumuladoInt1 = 0
var_acumuladoInt2 = 0

controlInt = True
while controlInt ==True:
    os.system ('cls') 

    print('>>>>>>>>>>>>>>>>MENU DE OPCIONES  \n\n')
    print('1.',participante1Str, 'No,',numeroP1Int, ' ', var_acumuladoInt1,'km\n2.',participante2Str,'No.',numeroP2Int,' ', var_acumuladoInt2,'Km\n3. finalizar')
    opcionInt = int(input('\señleccione el participante  ->'))
    if  opcionInt >=1  and opcionInt <=2:
        var_reccorridoEtapaInt = int(input('ingrese km recorridos -> '))
        if opcionInt == 1:
            var_acumuladoInt1 += var_reccorridoEtapaInt
        if opcionInt == 2:
            var_acumuladoInt2 += var_reccorridoEtapaInt
           
    if opcionInt == 3:
       os.system('cls')
       print('>>>>>>>REPORTE DE  COMPETENCIA<<<<<<<<<<<<<<')
       print('participante No.1',participante1Str,'recorrido:',var_reccorridoEtapaInt,'km')
       print('participante No.2',participante2Str,'recorrido:',var_reccorridoEtapaInt,'Km')
       enter = input('\n>enter  para continuar')
       opcionInt  = False
    
   
   
    
    













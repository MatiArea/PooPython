# Una farmacia guarda información de las ventas de medicamentos (nombre, droga, obra
# social, plan, importe, fecha y hora de venta) que se vendieron dentro del último mes. Se
# deberá desarrollar una aplicación, utilizando las clases que crea necesarios (fecha y hora
# deberán ser tenidas en cuenta), que resuelva las funcionalidades que se muestra en
# el siguiente menú:
# a) Agregar venta de medicamento
# b) Modificar venta de medicamento por nombre
# c) Eliminar venta de medicamento por nombre
# d) Modificar importe con un 20 % de descuento a medicamentos de un plan determinado
from clases import Farmacia, Venta
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    os.system('pause')


if __name__ == "__main__":
    
    print("="*40)
    print("          Creando Farmacia")
    print('='*40)
    nombre = input("Ingrese nombre de la farmacia: ")
    farmacia = Farmacia(nombre)
    print("="*40)
    pause()

    rta = 1
    while rta != 0:

        clear()

        print("============Bienvenido===========")
        print("1- Agregar venta")
        print("2- Modificar venta")
        print("3- Eliminar venta")
        print("4- Aplicar descuento")
        print("5- Listar ventas")
        print("0- Salir")
        rta = int(input("Ingrese una opcion: "))

        if rta == 1:

            clear()
            
            print("------Nueva Venta------")
            nombre = input("Ingrese nombre: ")
            droga = input("Ingrese droga: ")
            obraSocial = input("Ingrese obra social: ")
            plan = input("Ingrese plan de obra social: ")
            importe = float(input("Ingrese importe: "))
            venta = Venta(nombre, droga, obraSocial, plan, importe)
            farmacia.agregarVenta(venta)
            
            pause()

        elif rta == 2:
        
            clear() 
            ventas = farmacia.verVentas()
            nombreMedicamento = input("Ingrese nombre a modificar: ")

            for venta in ventas:
                if venta.nombreMedicamento == nombreMedicamento:
                    print("1- Nombre medicamento")
                    print("2- Droga")
                    print("3- Obra social")
                    print("4- Plan obra social")
                    print("5- Importe venta")
                    opcion = int(input("Ingrese una opcion: "))
                    if opcion == 1:
                        nombre = input("Ingrese nuevo nombre medicamento: ")
                        venta.nombreMedicamento = nombre
                    elif opcion == 2:
                        droga = input("Ingrese nueva droga: ")
                        venta.droga = droga
                    elif opcion == 3:
                        obraSocial = input("Ingrese nueva obra social: ")
                        venta.obraSocial = obraSocial
                    elif opcion == 4:
                        plan = input("Ingrese nuevo plan de obra social: ")
                        venta.plan = plan
                    else:    
                        importe = float(input("Ingrese nuevo importe: "))
                        venta.importe = importe
        
        elif rta == 3:

            clear() 

            nombreMedicamento = input("Ingrese nombre a eliminar: ")
            total = farmacia.totalVentas()
            i = 0
            
            while(i < total):
                venta = farmacia.recuperarVenta(i)
                if venta.nombreMedicamento == nombreMedicamento:
                    farmacia.eliminarVenta(i)
                    total -= 1
                i += 1
        
        elif rta == 4:
            
            clear() 
            ventas = farmacia.verVentas()
            plan = input("Ingrese nombre del plan de obra social: ")
            desc = int(input("Ingrese descuento a realizar (1-100): "))

            for venta in ventas:
                if venta.plan == plan:
                    venta.importe = venta.importe * (desc/100)

        elif rta == 5: 
            
            clear()
            
            ventas = farmacia.verVentas()
            for i,venta in enumerate(ventas):
                print("="*30)
                print(f"Venta numero {i}")
                print("Nombre Medicamento: ",venta.nombreMedicamento)
                print("Droga: ",venta.droga)
                print("Obra Social: ",venta.obraSocial)
                print("Plan Obra social: ",venta.plan)
                print("Importe: ",venta.importe)
                print("Fecha de venta: ",venta.fechaVenta)
                print("Hora de venta: ",venta.horaVenta)

            pause()

        elif rta == 0:

            print("Terminando ejecucion...")
        
        else:
            print("Opción incorrecta, intente nuevamente")
            os.system('pause')

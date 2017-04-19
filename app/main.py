'''
Calculadora de comisiones 
Este programa permite calcular las comisiones de los trabajadores de la empresa ABC de acuerdo a sus ventas mensuales
'''
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def inicio():
    '''
    Funcion inicial que muestra el formulario a llenar a fin de calcular las comisiones
    
    :return: Carga el 'index.html' 
    '''
    return render_template('index.html')

@app.route('/comision', methods=['POST'])
def comision():
    '''
    Esta funcion recibe los datos del formulario, realiza los calculos de las comisiones, muestra los resultados y los guarda en el archivo
    
    :return: Muestra 'comision.html' con los resultados
    '''
    if request.method == 'POST':
        nombre = str(request.form.get("nombre"))
        apellido = str(request.form.get("apellido"))
        ventas = float(request.form.get("ventas"))

        if ventas > 100000:
            comi = ventas*0.15
            porcentaje = 15
        elif ventas > 75000:
            comi = ventas*0.1
            porcentaje = 10
        elif ventas > 50000:
            comi = ventas*0.07
            porcentaje = 7
        elif ventas > 25000:
            comi = ventas*0.05
            porcentaje = 5
        elif ventas == 0:
            comi = 0
            porcentaje = 0
        else:
            comi = ventas*0.03
            porcentaje = 3

        try:
            archivo = open("docs/registro.csv", "a", newline='')
            archivo.write(apellido + ", " + nombre + ", " + str(ventas) + ", " + str(comi) + "\n")
            archivo.close()
        except FileNotFoundError:
            return render_template("error.html", er="No existe el archivo")
        except:
            return render_template("error.html", er="Error General")

        return render_template('comision.html', nom=nombre, ape=apellido, ven=ventas, com=comi, por=porcentaje)

if __name__ == "__main__":
    app.run()

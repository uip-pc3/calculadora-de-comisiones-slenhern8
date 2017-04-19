from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/comision', methods=['POST'])
def comision():
    if request.method == 'POST':
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
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

        '''try: Esto me esta jodiendo :'(    si alguien ve esto envien ayuda XD
            archivo = open("docs/registro.csv", "w")
            archivo.write(apellido + ", " + nombre + ", " + ventas)
            archivo.close()
        except FileNotFoundError:
            return render_template("error.html", er="No existe el archivo")
        except:
            return render_template("error.html", er="Error General")'''

        return render_template('comision.html', nom=nombre, ape=apellido, ven=ventas, com=comi, por=porcentaje)

if __name__ == "__main__":
    app.run()

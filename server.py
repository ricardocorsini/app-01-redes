from flask import Flask, render_template, jsonify, request, send_file
from waitress import serve
from DimCis import Beam
from EstacaZero import wordExport

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/EstacaZero')
def estaca_zero():
    return render_template('estacaZero.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():

    if request.method == 'POST':

        name = str(request.form.get('name'))
        bw = float(request.form.get('bw'))
        d = float(request.form.get('d'))
        vk = float(request.form.get('vk'))
        gama_c = float(request.form.get('gama_c'))
        gama_c2 = float(request.form.get('gama_c2'))
        fywk = float(request.form.get('fywk'))
        gama_s = float(request.form.get('gama_s'))
        fck = float(request.form.get('fck'))
        stittupleg = float(request.form.get('stittupleg'))

        BeamCreated = Beam(name, bw, d, vk, gama_c, gama_c2, fywk, gama_s, fck, stittupleg)
        BeamCreated.generate_memory()

        path_memory = name + '_' + 'cis' + '.docx'
       
        print(f"Recebido: {name}, {bw}, {d}, {vk}, {gama_c}, {gama_c2}, {fywk}, {gama_s}, {fck}, {stittupleg}")

        return send_file(path_memory, as_attachment=True, download_name=path_memory)
    
@app.route('/submitEstaca', methods=['POST', 'GET'])
def submitEstaca():

    if request.method == 'POST':

        listaSolos = str(request.form.get('listaSolos'))
        listaSolos_str = listaSolos.split(",")
        listaSolos_int = [int(num.strip()) for num in listaSolos_str]


        listaNspt = str(request.form.get('listaNspt'))
        listaNspt_str = listaNspt.split(",")
        listaNspt_int = [int(num.strip()) for num in listaNspt_str]


        tipoEstaca = str(request.form.get('tipoEstaca'))
        diametroEstaca = float(request.form.get('diametroEstaca'))
        cargaAdmissivel = float(request.form.get('cargaAdmissivel'))
        nivelAgua = float(request.form.get('nivelAgua'))
        fileName = str(request.form.get('fileName'))
                      
       
        wordExport(listaSolos_int, tipoEstaca, diametroEstaca, listaNspt_int, cargaAdmissivel, nivelAgua, fileName)
        print(f"Recebido: {listaSolos_int}, {listaNspt_int}, {tipoEstaca}, {diametroEstaca}, {cargaAdmissivel}")

        path_memory = fileName + '.docx'

        return send_file(path_memory, as_attachment=True, download_name=path_memory)
        

if __name__ == '__main__':
    #local use
    app.run(debug=True)
    #Server use
    #serve(app, host='0.0.0.0', port=5000)




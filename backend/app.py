from flask import Flask, render_template

from agendamentos import buscar_agendamento, listarPorStatus, listar_agendamentos


app = Flask(__name__)


@app.route('/')
def index():
	agendamentos = listar_agendamentos()
	return render_template('index.html', nome_barbearia='DHA - Barbearia', agendamentos=agendamentos)


@app.route('/agendamentos')
def agendamentos():
	return render_template('agendamentos.html', agendamentos=listar_agendamentos())


@app.route('/agendamentos/status/<status>')
def agendamentos_por_status(status):
	return render_template(
		'agendamentos.html',
		agendamentos=listarPorStatus(status),
		status_atual=status,
	)

@app.route('/agendamento/novo', methods=['GET', 'POST'])
def novo_agendamento():
    if request.method == 'POST':
        # 1. Captura os dados do formulário HTML (os names do formulário devem bater com estas chaves)
        novo = Agendamento(
            cliente=request.form['cliente'],
            telefone=request.form['telefone'],
            servico=request.form['servico'],
            preco=float(request.form['preco']),
            barbeiro=request.form['barbeiro'],
            data=request.form['data'],
            horario=request.form['horario'],
            status=request.form.get('status', 'Pendente')
        )
        
        # 2. Chama a função que insere no banco de dados
        cadastrar_agendamento(novo)

        # 3. Redireciona o usuário para a lista de agendamentos
        return redirect(url_for('agendamentos'))

    # Se a requisição for GET, exibe o formulário de cadastro
    return render_template('cadastrar.html')

@app.route('/agendamento/<int:id>')
def detalhe(id):
	resultados = buscar_agendamento(id)
	agendamento = resultados[0] if resultados else None
	return render_template('detalhes.html', agendamento=agendamento)


if __name__ == '__main__':
	app.run(debug=True)

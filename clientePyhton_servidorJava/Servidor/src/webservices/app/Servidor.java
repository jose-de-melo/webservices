package webservices.app;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/**
 * Classe responsável por criar o servidor e executar as ações do mesmo.
 */
public class Servidor {
	/**
	 * Inicia a aplicação servidor. 
	 */
	public static void main(String[] args) {
		new Servidor().servidor();
		System.exit(0);
	}
	
	/**
	 * Cria o socket do servidor e espera pelo contato do cliente para exibir informações sobre os
	 * dados que foram recebidos do mesmo.
	 */
	public void servidor(){
		ServerSocket servidor = null;
		try {
			servidor = new ServerSocket(1717);
			servidor.setSoTimeout(60000);
			System.out.println("Servidor ouvindo a porta 1717...");

			Socket cliente = servidor.accept();
			System.out.println("Cliente conectado >>> " + cliente.getInetAddress().getHostAddress());
			Scanner entrada = new Scanner(cliente.getInputStream());

			String dados = "";

			while(entrada.hasNextLine()) {
				dados = entrada.nextLine();
			}

			JSONObject jsonObj = new JSONObject(dados);
			JSONArray jsonArray = jsonObj.getJSONArray("Alunos");

			Turma turma = new Turma();
			turma.setAno(jsonObj.getInt("Ano"));
			turma.setCurso(jsonObj.getString("Curso"));
			turma.setId(jsonObj.getLong("Id"));

			//System.out.println(turma);

			Aluno aluno;
			JSONObject jsonAluno;
			for (int i = 0; i < jsonArray.length(); i++) {
				aluno = new Aluno();

				jsonAluno = jsonArray.getJSONObject(i);

				aluno.setIdTurma(jsonAluno.getLong("IdTurma"));
				aluno.setId(jsonAluno.getLong("Id"));
				aluno.setNome(jsonAluno.getString("Nome"));
				aluno.setMatriculado(jsonAluno.getBoolean("Matriculado"));
				turma.addAluno(aluno);
			}

			System.out.println(String.format("A turma %s de %d do curso %s possui %d alunos, dos quais %d estão devidamente matriculados.", turma.getCurso(), turma.getAno(), turma.getCurso(),turma.numeroDeAlunos(), turma.numeroDeAlunosMatriculados()));
			entrada.close();
			cliente.close();
			servidor.close();
		} catch (IOException e) {
			e.printStackTrace();
			try {
				if(servidor != null) {
					servidor.close();
				}
			} catch (IOException e1) {
				e1.printStackTrace();
			}
		} catch (JSONException e) {
			System.err.println("Erro de conversão JSON!");
			e.printStackTrace();
		}
	}


	/**
	 * Classe usada para manipular os dados de alunos.
	 *
	 */
	public static class Aluno{
		Long id, idTurma;
		String nome;
		boolean matriculado;

		public Aluno() {
		}


		public void setId(Long id) {
			this.id = id;
		}

		public Long getIdTurma() {
			return idTurma;
		}

		public void setIdTurma(Long idTurma) {
			this.idTurma = idTurma;
		}

		public String getNome() {
			return nome;
		}

		public void setNome(String nome) {
			this.nome = nome;
		}

		public boolean isMatriculado() {
			return matriculado;
		}

		public void setMatriculado(boolean matriculado) {
			this.matriculado = matriculado;
		}

		public Long getId() {
			return id;
		}


		@Override
		public String toString() {
			return nome;
		}


	}

	/**
	 * Classe usada para manipular os dados de turmas.
	 *
	 */
	public static class Turma{
		Long id;
		int ano;
		String curso;
		List<Aluno> alunos;

		public Turma() {
			alunos = new ArrayList<Aluno>();
		}

		public Long getId() {
			return id;
		}

		public void setId(Long id) {
			this.id = id;
		}

		public int getAno() {
			return ano;
		}

		public void setAno(int ano) {
			this.ano = ano;
		}

		public String getCurso() {
			return curso;
		}

		public void setCurso(String curso) {
			this.curso = curso;
		}



		public void addAluno(Aluno aluno) {
			alunos.add(aluno);	
		}

		public int numeroDeAlunos() {
			return alunos.size();
		}

		public int numeroDeAlunosMatriculados() {
			int nMatriculados = 0;

			for (Aluno aluno : alunos) {
				if(aluno.isMatriculado()) {
					nMatriculados++;
				}
			}

			return nMatriculados;

		}

		@Override
		public String toString() {
			return String.format("Curso : %s, Ano : %d",curso,ano);
		}


	}
}
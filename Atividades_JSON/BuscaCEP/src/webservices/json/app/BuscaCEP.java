package webservices.json.app;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

import javax.swing.JOptionPane;

import org.json.JSONException;
import org.json.JSONObject;

public class BuscaCEP {

	public static void main(String[] args) {
		new BuscaCEP().buscaCEP();
		System.exit(0);
	}
	
	public void buscaCEP(){
		String jsonSTR = lerDados();
		
		if(jsonSTR == null){
			JOptionPane.showMessageDialog(null, "CEP inválido!", "Resultado da Consulta", JOptionPane.INFORMATION_MESSAGE);
		}
		else if(jsonSTR.contains("erro")){
			JOptionPane.showMessageDialog(null, "CEP inválido!", "Resultado da Consulta", JOptionPane.INFORMATION_MESSAGE);
		}
		else{
			try {
				JSONObject jsonObj = new JSONObject(jsonSTR);
				
				String saida = "";
				saida += String.format("CEP: %s\n", jsonObj.getString("cep"));
				saida += String.format("Logradouro: %s\n", jsonObj.getString("logradouro"));
				saida += String.format("Bairro: %s\n", jsonObj.getString("bairro"));
				saida += String.format("Localidade: %s\n", jsonObj.getString("localidade"));
				saida += String.format("UF: %s\n", jsonObj.getString("uf"));
				saida += String.format("IBGE: %s\n", jsonObj.getString("ibge"));
				
				JOptionPane.showMessageDialog(null, saida, "Resultado da Consulta", JOptionPane.INFORMATION_MESSAGE);
				
			} catch (JSONException e) {
				System.err.println("Erro de conversão da string em JSON!");
				e.printStackTrace();
			}
		}
	}

	private String lerDados() {
		String url = "https://viacep.com.br/ws/";
		String complemento = "/json";
		String cep = JOptionPane.showInputDialog(null, "CEP (Sem hífen)", "Consultar CEP", JOptionPane.QUESTION_MESSAGE);
		
		url += cep + complemento;
		
		try {
			URL ur = new URL(url);
			URLConnection con = ur.openConnection();
			
			BufferedReader input = new BufferedReader(new InputStreamReader(con.getInputStream(), "utf-8"));
			
			String linha;
			StringBuilder source = new StringBuilder();
			
			while((linha = input.readLine()) != null){
				source.append(linha);
			}
			
			input.close();
			
			return source.toString();
			
		} catch (MalformedURLException e) {
			System.err.println("Formato de URL inválido!");
			e.printStackTrace();
		} catch (IOException e) {
			return null;
		}
		return null;
	}

}

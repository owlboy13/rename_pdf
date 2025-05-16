# **📂 PDF Organizer**  

**Script Python para extrair informações de PDFs e renomear os arquivos automaticamente.**  

🔹 **O que este script faz?**  
- Extrai textos específicos de arquivos PDF usando coordenadas (*bounding boxes*).  
- Renomeia os arquivos com base no conteúdo extraído (ex.: nomes de clientes, números de documento, etc.).  
- Gera um arquivo XML para análise estrutural do PDF (útil para ajustar as coordenadas de extração).  

---  

## **📋 Pré-requisitos**  
- Python 3.6+  
- Bibliotecas necessárias:  
  ```bash
  pip install pdfquery pandas tqdm
  ```  

---  

## **🛠 Como usar?**  

### **1. Estrutura de pastas**  
Crie duas pastas no mesmo diretório do script:  
- `./pdfs/` → Coloque aqui os PDFs que deseja processar.  
- `./xml/` → Pasta onde serão salvos os arquivos XML (para análise de estrutura).  

### **2. Configure as coordenadas de extração**  
Edite o dicionário `names_files` no script para definir:  
- **O nome do campo** (ex.: `'Nome'`).  
- **As coordenadas (*bbox*)** onde o texto está localizado no PDF (formato: `'x0, y0, x1, y1'`).  

Exemplo:  
```python
names_files = {
    'Nome': {
        'xml_codigo': [
            '204.777, 395.127, 435.936, 407.127',  # Coordenadas 1
            '239.875, 380.127, 432.994, 392.127',  # Coordenadas 2 (backup)
        ],
    },
}
```  

### **3. Execute o script**  
```bash
python nome_do_script.py
```  

✔ Os PDFs serão renomeados automaticamente com base no texto extraído.  
✔ Arquivos XML serão gerados em `./xml/` para ajudar no ajuste das coordenadas.  

---  

## **⚠️ Observações**  
- **Se o texto não for extraído**, verifique as coordenadas no XML gerado e ajuste `names_files`.  
- Se houver **arquivos com o mesmo nome**, o script pulará (evitando sobrescrita).  
- **Dica:** Use ferramentas como `pdfinspector` ou `Adobe Acrobat` para encontrar as coordenadas exatas do texto.  

---  

## **📄 Exemplo de Saída**  
```plaintext
Arquivo renomeado para "João Silva - Contrato.pdf"  
Arquivo renomeado para "Empresa XYZ - Nota Fiscal 1234.pdf"  
```  

---  

## **📌 Aplicações Úteis**  
✔ **Organizar contratos** por nome do cliente.  
✔ **Padronizar notas fiscais** por número/data.  
✔ **Extrair dados** de relatórios em lote.  

---  

**🔗 Quer personalizar?** Sinta-se à vontade para contribuir ou entrar em contato!  

🚀 **Happy Coding!**  

---  

### **📜 Licença**  
MIT License - Livre para uso e modificação.  

---  

Esse `README.md` está pronto para ser usado no GitHub ou como documentação interna. Se precisar de ajustes, é só pedir! 😊

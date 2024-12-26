## Funções e Seus Usos

### 1. `validar_diretorio(diretorio)`
- Verifica se o diretório existe e o cria caso não exista.
---

### 2. `listar_arquivos(diretorio)`
- Lista todos os arquivos presentes no diretório e seus subdiretórios.
---

### 3. `filtrar_arquivos_por_data(arquivos, limite_tempo)`
- Separa os arquivos em duas categorias:
  - Arquivos para cópia: data de criação menor ou igual ao limite de 3 dias.
  - Arquivos para remoção: data de criação superior ao limite de 3 dias.
---

### 4. `remover_arquivos(arquivos)`
- Remove arquivos com data de criação superior a 3 dias.
---

### 5. `copiar_arquivos(arquivos, destino)`
- Copia arquivos para o diretório de destino.
---

### 6. `inicializar_logger(caminho_log)`
- Configura o sistema de logs para registrar as operações realizadas.
- Gera registros das listagens, cópias e remoções.
---

### 7. `main()`
- Coordena todas as operações:
  - Valida os diretórios de origem e destino.
  - Lista e registra os arquivos encontrados.
  - Filtra os arquivos para cópia e remoção.
  - Remove arquivos desnecessários.
  - Copia arquivos importantes para o destino.
- Gera logs detalhados em:
  - `backupsFrom.log`: Informações sobre os arquivos na origem.
  - `backupsTo.log`: Registros das cópias realizadas.
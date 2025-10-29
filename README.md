# CPF Utils 🧮

Este projeto contém **utilitários em Python para CPFs**, incluindo:
- Geração de CPFs aleatórios
- Validação de CPFs
- Cálculo dos dois dígitos verificadores a partir dos 9 primeiros números

## 📝 Scripts incluídos

### 1️⃣ cpf_generator.py
Gera CPFs completos aleatórios e válidos.

**Exemplo de uso:**
```bash
Quantos CPFs você quer gerar: 1
12345678909
123.456.789-09
```
### 2️⃣ cpf_validator.py
Verifica se um CPF é válido conforme os dígitos verificadores.

Exemplo de uso:
```bash
Digite o CPF: 123.456.789-09
CPF inválido
```
### 3️⃣ cpf_check_digits.py
Calcula os dois últimos dígitos (verificadores) a partir dos 9 primeiros números do CPF.

Exemplo de uso:
```bash
Digite os 9 primeiros dígitos do CPF: 123456789
Dígitos verificadores: 0 9
CPF completo: 12345678909
```

⚙️ Como executar

Tenha o Python 3 instalado.

Clone ou baixe o repositório:
```bash
git clone https://github.com/seu-usuario/cpf-utils.git
```

Navegue até a pasta do script que deseja usar:
```bash
cd cpf-utils
python gerador_cpf.py
```

🧠 O que aprendi com este projeto

Lógica de programação e controle de fluxo (for, if, try/except)

Manipulação de strings e listas em Python

Implementação do cálculo de dígitos verificadores do CPF

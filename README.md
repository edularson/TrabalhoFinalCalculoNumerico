### `README.md`

# Trabalho de Cálculo Numérico em Python  

Este projeto contém implementações de **métodos numéricos para encontrar raízes de equações não lineares** e também do método **Gauss-Seidel** para resolução de sistemas lineares.  

## Estrutura do Projeto  

- `metodos_raizes.py`: Contém a implementação dos métodos para encontrar raízes de equações não lineares, incluindo:  
  - **Método da MIL** 
  - **Método da Bisseção**  
  - **Método da Regula Falsi**  
  - **Método da Secante**  
  - **Método de Newton-Raphson**  

- `gauss_seidel.py`: Implementação do método **Gauss-Seidel** para resolver sistemas lineares iterativamente.  

- `menu.py`: Um menu interativo que permite o usuário escolher qual método deseja utilizar.  

## Funcionalidades  

### Métodos para Encontrar Raízes  
Estes métodos recebem como entrada:  
- A função a ser analisada.  
- Intervalo inicial ou chute inicial (dependendo do método).  
- Precisão desejada para o critério de parada.  

### Gauss-Seidel  
O método Gauss-Seidel resolve sistemas lineares da forma \( Ax = b \), onde:  
- \( A \) é a matriz de coeficientes.  
- \( b \) é o vetor de constantes.  
- \( x \) é o vetor solução.  

A implementação verifica:  
- Critérios de convergência.  
- Erros e ajustes na solução iterativa.  

No menu, você poderá:  
- Escolher um dos métodos para encontrar raízes.  
- Resolver um sistema linear utilizando o Gauss-Seidel.  

## Linguagem Utilizada  

- **Python**  

## Autor  

Este projeto foi desenvolvido por Eduardo Larson "edularson" e Thiago Ceron de Almeida "thiagoceron".
